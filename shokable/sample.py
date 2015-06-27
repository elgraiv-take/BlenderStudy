'''
Created on 2015/06/26
@author: take
'''

#アドオンの情報
#今回は1ファイルだがモジュールとして作るときは__init__.pyに書けばいい
#必須なのはnameとcategory
bl_info = {
    "name": "Sample Add-on",
    "author": "Take",
    "blender": (2, 74, 0),
    "description": "Sample Blender Add-on for SHOKABLE",
    "category": "Sample"
}

import bpy

#オペレータのサンプル
class SampleOperator(bpy.types.Operator):
    bl_idname = "object.rename_sample"  #bpy.opsに追加される時の関数名
    bl_label = "Sample Operator"        #UIに表示される時の名前

    def execute(self, context):
        #ここに実行したいスクリプト
        context.object.name="sample";
        return {'FINISHED'}

#ダイアログを表示して値を設定できるオペレータのサンプル
#ちゃんとダイアログをキャンセルすれば実行もされない
class SampleOperator2(bpy.types.Operator):
    bl_idname = "object.rename_sample2"
    bl_label = "Sample of Dialog"

    #ダイアログで設定できる値
    sampleProp=bpy.props.StringProperty(name="name")

    def execute(self, context):
        context.object.name=self.sampleProp
        return {'FINISHED'}

    #executeの前に実行される関数
    #プロパティの初期化に使う
    def invoke(self,context,event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self) #ダイアログの呼び出し

#SampleOperator2のプロパティを増やした版
class SampleOperator2Ex(bpy.types.Operator):
    bl_idname = "object.rename_sample2ex"
    bl_label = "Sample of Dialog Ex"

    sampleProp0=bpy.props.StringProperty(name="String")

    #soft_min/soft_maxはドラッグ操作で変えられる範囲(手入力では超えられる)
    sampleProp1=bpy.props.IntProperty(name="Int", default=1,soft_min=0,soft_max=100,min=-100,max=1000)
    sampleProp2=bpy.props.IntVectorProperty(name="IntVector")
    sampleProp3=bpy.props.FloatProperty(name="Float", default=1.0,min=0.0, max=100.0)

    sampleProp4=bpy.props.FloatVectorProperty(name="FloatVector",size=3)

    #subtypeを設定すると値を操作するためのUIが変わる
    #subtypeをCOLORにすると色を選択するためのUIが使える
    #値の範囲は変わらないのでそのままだと使いづらい
    sampleProp5=bpy.props.FloatVectorProperty(name="FloatVector(Color)", subtype="COLOR",size=4,soft_min=0.0,soft_max=1.0)
    sampleProp6=bpy.props.BoolProperty(name="Bool")

    #普通のBoolVectorPropertyだとチェックボックスがずらっと並ぶがsubtypeにLAYERを指定するとタイル状に並ぶ
    sampleProp7=bpy.props.BoolVectorProperty(name="Bool Vector",size=16,subtype="LAYER")

    def execute(self, context):
        context.object.name=self.sampleProp0
        return {'FINISHED'}

    def invoke(self,context,event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

#ファイル選択画面を開く
class SampleOperator3(bpy.types.Operator):
    bl_idname = "object.rename_sample3"
    bl_label = "Sample of File Selector"

    filepath = bpy.props.StringProperty(subtype="FILE_PATH")
    def execute(self, context):
        context.object.name=self.filepath
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

#メニューを作る
#これだけだと表示されないので他のメニューにAddするか他のoperatorで呼ぶ必要がある
class SampleMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_object_rename_samples"   #Blender内部での名前
    bl_label = "Sample"
    def draw(self, context):
        layout = self.layout
        #上で作成したオペレータを追加
        #クラス名ではなくbl_idnameの値
        #既存のオペレータも追加できる(メニューやボタン上にカーソルを合わせた時に出てくる"Python: bpy.ops.***.***()")
        layout.operator("object.rename_sample")
        layout.operator("object.rename_sample2")
        layout.operator("object.rename_sample2ex")
        layout.operator("object.rename_sample3")

#UIのパネル上に表示するサンプル
#今回は
class SampleToolPanel(bpy.types.Panel):
    bl_idname="Sample_PT_Tool_Panel"    #Blender内部での名前
    bl_space_type = 'VIEW_3D'   #どのウィンドウで表示するか(他には)
    bl_region_type = 'TOOLS'    #3DViewの左のパネル
    bl_category = "Sample"      #Toolboxではタブ
    bl_context = "objectmode"   #どのモードの時に表示するか
    bl_label = "Sample Tools"   #パネルの表示名
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.operator("object.rename_sample")
        col.operator("object.rename_sample2")
        col.operator("object.rename_sample2ex")
        col.operator("object.rename_sample3")

#このAdd-onを有効にする時(チェックボックスをonにする時)に呼ばれる
def register():
    bpy.utils.register_module(__name__)

    #上で定義したメニューを3D Viewの下のメニューのobjectに追加する
    #selfとcontexを引数に取る関数であればいいので実はMenuクラスを作る必要はない
    #というよりこの方法が邪道かも
    bpy.types.VIEW3D_MT_object.append(SampleMenu.draw)

#無効にする時に呼ばれる関数
def unregister():
    bpy.types.VIEW3D_MT_object.remove(SampleMenu.draw)#メニューから削除
    bpy.utils.unregister_module(__name__)

#その他

#・既存UIのソース
#UI上で右クリックすると出てくるメニューのEdit Sourceを選択するとText EditorでそのUIのソースを見ることができる
#ただし3D ViewのTransformなどPythonで書かれていない(らしい)ものは開けない

#・サンプルコード
#Text EditorのTemplatesにいろんなAdd-onのひな形が入っている(重要)

#既存のUIの位置
#既存のパネルがどこにあるか(bl_space_type,bl_region_typeなど)知りたい時はソースを開いて
#それっぽいクラス(大体クラス名は[プロパティのタブ名]_PT_[ヘッダ名]とかになってる)がどうなってるか見れば良い
#ただしスーパークラスに定義されている場合もあるので注意
#メニューの場合はクラス名(大体は[なんとか]_MT_[なんとか])さえわかればいいので楽
#UIクラスを一覧したい場合は
#panels=[ pt for pt in dir(bpy.types) if pt.find("_PT_")>0]
#menus=[ pt for pt in dir(bpy.types) if pt.find("_MT_")>0]
#などで命名に則ったものは取れる

#ドキュメント
#http://www.blender.org/api/blender_python_api_2_74_release/bpy.props.html
#http://www.blender.org/api/blender_python_api_2_74_release/bpy.types.Operator.html
#http://www.blender.org/api/blender_python_api_2_74_release/bpy.types.Panel.html
#http://www.blender.org/api/blender_python_api_2_74_release/bpy.types.Menu.html