# This script is intended to facilitated easier positioning of the 3D cursor when drawing with blenders grease pencil tools.
# The 3d cursor is constrained to an object named "draw_location", which can then be manipulated using blenders built in 3d view gizmos

import bpy

def draw_callback_px(self, context):
    # Get the current view layer
    view_layer = bpy.context.view_layer

    for obj in view_layer.objects:
        if obj.name.startswith("draw_location"):
            draw_location_object = obj

    if draw_location_object:
        # Set 3D cursor location to the origin of the "draw_location" object
        bpy.context.scene.cursor.location = draw_location_object.location

    # Redraw the 3D view
    bpy.context.area.tag_redraw()

def register():
    bpy.app.timers.register(lambda: draw_callback_px(None, bpy.context), first_interval=0.3)
    bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, (None, bpy.context), 'WINDOW', 'POST_PIXEL')

def unregister():
    bpy.app.timers.unregister(lambda: draw_callback_px(None, bpy.context))
    bpy.types.SpaceView3D.draw_handler_remove(draw_callback_px, 'WINDOW')

if __name__ == "__main__":
    register()

