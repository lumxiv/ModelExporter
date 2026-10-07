import bpy
from bpy.props import (StringProperty, PointerProperty, IntProperty)                    
from bpy.types import (PropertyGroup, Operator)

import os
import glob

working_dir = dirname = os.path.dirname(os.path.abspath(__file__))
print(working_dir)
# ================================

class ModelFrameExportProperties(PropertyGroup):
    # Simple Export Anim
    start_frame: IntProperty(
        name = "Start Frame",
        default = 1,
        min = 1
    ) # type: ignore
    end_frame: IntProperty(
        name = "End Frame",
        default = 50,
        min = 5
    ) # type: ignore
    output_dir: StringProperty(
        name = "",
        default = working_dir + "/tmp/",
        maxlen = 1024,
        subtype = "DIR_PATH"
    ) # type: ignore

class ModelFrameExportOp(Operator):
    """Export model frame by frame"""
    bl_idname = "f_exporter_props.frame_exporter"
    bl_label = "Model Frame Export Operator"

    def execute(self, context):
        scene = context.scene
        state = scene.f_exporter_props

        output_dir = state.output_dir
        start_frame = state.start_frame
        end_frame = state.end_frame

        group_by = 8
        group = 0
        model = 1

        for frame in range(start_frame, end_frame + 1):
            if group == group_by:
                model += 1
            group %= group_by
            particle_count = str(model).zfill(2)
            filepath = output_dir + "particle " + particle_count + " - model " + str(group+1) + " - (frame " + str(frame) + ")"
            print("Exporting GLTF for frame " + str(frame) + ", as " + str(filepath))
            bpy.context.scene.frame_set(frame)
            bpy.ops.export_scene.gltf(filepath=filepath,
                                        use_selection=True, use_visible=True, export_morph=False,
                                        export_attributes=True, export_tangents=True, export_apply=True,
                                        export_animations=False, export_materials='NONE',
                                        export_skins=False, export_current_frame=True)
            group += 1

        return {'FINISHED'}
        
class ModelFrameExportPanel(bpy.types.Panel):
    bl_idname = "MFE_PT_Export"
    bl_label = "Model Frame Export"
    bl_category = "ModelExporter"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        state = scene.f_exporter_props

        if context.object != None and context.object.type == 'MESH':
            split = layout.row().split(factor=0.25)
            split.label(text="Target")
            split.label(text=context.object.name, icon='MESH_DATA')

            col = layout.column()
            col.label(text="Output Directory")
            col.prop(state, "output_dir", text="")

            box = layout.box()
            row = box.row(align=True)
            row.prop(state, "start_frame")
            row.prop(state, "end_frame")     

            layout.operator(ModelFrameExportOp.bl_idname, text="Export", icon="PLAY")
        else:
            layout.label(text='No mesh selected', icon='ERROR') 
    
# ================================
        
classes = (
    ModelFrameExportProperties,

    ModelFrameExportPanel,
    ModelFrameExportOp,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.f_exporter_props = PointerProperty(type=ModelFrameExportProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)  
    del bpy.types.Scene.f_exporter_props


if __name__ == "__main__":
    register()
