import bpy
import requests
import os
import hashlib
import random

bl_info = {
    "name": "animation utils",
    "author": "reijaff",
    "version": (1, 0),
    "blender": (3, 40, 0),
    "location": "Sequencer > Strip > animation utils",
    "description": "animate and stuff",
    "warning": "",
    "doc_url": "",
    "category": "Sequencer",
}


class AnimateZoomImageOperator(bpy.types.Operator):
    bl_idname = "vse.animate_zoom_image"
    bl_label = "Animate zoom image"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.space_data.type == "SEQUENCE_EDITOR"

    def execute(self, context):


        strip = context.scene.sequence_editor.active_strip

        if strip.type != "IMAGE":  # Simplified check
            self.report({"ERROR"}, "Can only remove background from image strips")
            return {"CANCELLED"}

        fs = strip.frame_start
        fe = strip.frame_final_end

        bpy.context.frame_current = fs

        strip.keyframe_insert(data_path="transform.scale_x")
        strip.keyframe_insert(data_path="transform.scale_y")

        strip.transform.scale_x = 2
        strip.transform.scale_y = 2

        bpy.context.frame_current = fe

        strip.keyframe_insert(data_path="transform.scale_y")
        strip.keyframe_insert(data_path="transform.scale_y")

        return {"FINISHED"}



def menu_anim_unils(self, context):
    self.layout.separator()
    self.layout.operator(AnimateZoomImageOperator.bl_idname, icon="OUTLINER_OB_IMAGE")


def register():
    bpy.utils.register_class(AnimateZoomImageOperator)
    bpy.types.SEQUENCER_MT_context_menu.append(menu_anim_utils)


def unregister():
    bpy.utils.unregister_class(AnimateZoomImageOperator)
    bpy.types.SEQUENCER_MT_context_menu.remove(menu_anim_utils)


if __name__ == "__main__":
    register()
