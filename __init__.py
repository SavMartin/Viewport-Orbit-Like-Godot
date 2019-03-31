import bpy
from bpy.types import Panel
from bl_ui.space_toolsystem_common import ToolSelectPanelHelper
import os
from itertools import cycle
import _thread,time




bl_info = {
    "name": "ViewPort Orbit Like Godot",
    "description": "ViewPort Orbit Like Godot configurator",
    "author": "Sav Martin",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "User"
}
def start_thread():
    _thread.start_new_thread(thrd_func,())

def thrd_func():
    time.sleep(.1)
    keymaps_default_manipulator(False)

def keymaps_default_manipulator(modo):

# Disable Keymaps
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    
    #Disable View Navigation

    wm.keyconfigs.default.keymaps['3D View'].keymap_items['view3d.navigate'].active = modo

    #Disable View 3D Walk Modal

    wm.keyconfigs.default.keymaps['View3D Walk Modal'].keymap_items[0].active = modo

    #Disable Call Menu Objet Mode

    for ki in  wm.keyconfigs.default.keymaps['Object Mode'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'VIEW3D_MT_object_context_menu':
                ki.active = modo
    
    #Disable Call Menu Edit Mode

    for ki in  wm.keyconfigs.default.keymaps['Mesh'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'VIEW3D_MT_edit_mesh_context_menu':
                ki.active = modo

    #Disable Call Menu Pose

    for ki in  wm.keyconfigs.default.keymaps['Pose'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'VIEW3D_MT_pose_context_menu':
                ki.active = modo

    #Disable Call Menu Shade Editor

    for ki in  wm.keyconfigs.default.keymaps['Node Editor'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'NODE_MT_context_menu':
                ki.active = modo

    #Disable Call Menu Curve

    for ki in  wm.keyconfigs.default.keymaps['Curve'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'VIEW3D_MT_edit_curve_context_menu':
                ki.active = modo

    #Disable Call Menu Armature

    for ki in  wm.keyconfigs.default.keymaps['Armature'].keymap_items:
        if "name" in ki.properties:
            if ki.properties.name == 'VIEW3D_MT_armature_context_menu':
                ki.active = modo 

    #Disable Call Menu Weight Paint

    wm.keyconfigs.default.keymaps['Weight Paint'].keymap_items['wm.call_panel'].active = modo

    #Disable Call Menu Vertex Paint

    wm.keyconfigs.default.keymaps['Vertex Paint'].keymap_items['wm.call_panel'].active = modo              


addon_keymaps = []


def register_keymap():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    # Leftclik Keymap configuration     ************************************************************************************************************************************

#Add View Navigation

    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D", region_type='WINDOW')
    kmi = km.keymap_items.new("view3d.navigate", 'EVT_TWEAK_R', 'ANY')
    addon_keymaps.append((km, kmi))

    #Add View 3D Walk Modal

    km = kc.keymaps.new(name='View3D Walk Modal', space_type='VIEW_3D', region_type='WINDOW', modal=True)
    kmi = km.keymap_items.new_modal('CONFIRM', 'RIGHTMOUSE', 'RELEASE')
    addon_keymaps.append((km, kmi))
        
    #Add Call Menu In Objetc Mode

    km = kc.keymaps.new(name="Object Mode", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'VIEW3D_MT_object_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Edit Mode

    km = kc.keymaps.new(name="Mesh", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'VIEW3D_MT_object_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Dopesheet

    km = kc.keymaps.new(name="Dopesheet", space_type="DOPESHEET_EDITOR", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'DOPESHEET_MT_context_menu'
    addon_keymaps.append((km, kmi))

    # Add Call Menu In Animation Channels

    km = kc.keymaps.new(name="Animation Channels", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'DOPESHEET_MT_channel_context_menu'
    addon_keymaps.append((km, kmi))

    # Add Call Menu In Graph Editor
    
    km = kc.keymaps.new(name="Graph Editor", space_type="GRAPH_EDITOR", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'GRAPH_MT_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Pose

    km = kc.keymaps.new(name="Pose", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'VIEW3D_MT_pose_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu Shade Editor

    km = kc.keymaps.new(name="Node Editor", space_type="NODE_EDITOR", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'NODE_MT_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu Clip Editor

    km = kc.keymaps.new(name="Clip Editor", space_type="CLIP_EDITOR", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'CLIP_MT_tracking_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Curve

    km = kc.keymaps.new(name="Curve", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'VIEW3D_MT_edit_curve_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Armature

    km = kc.keymaps.new(name="Armature", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_menu", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'VIEW3D_MT_armature_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Weight Paint

    km = kc.keymaps.new(name="Weight Paint", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_panel", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'VIEW3D_PT_paint_weight_context_menu'
    addon_keymaps.append((km, kmi))

    #Add Call Menu In Weight Paint

    km = kc.keymaps.new(name="Vertex Paint", space_type="EMPTY", region_type='WINDOW')
    kmi = km.keymap_items.new("wm.call_panel", 'RIGHTMOUSE', 'CLICK')
    kmi.properties.name = 'VIEW3D_PT_paint_vertex_context_menu'
    addon_keymaps.append((km, kmi))

    
    # ********************************************************************************************************************************************* 


def unregister_keymap():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()



def register():
    from bpy.utils import register_class
    addon_keymaps.clear()
    start_thread()
    register_keymap()


def unregister():
    from bpy.utils import register_class

    keymaps_default_manipulator(True)
    unregister_keymap()


if __name__ == "__main__":
    register()
