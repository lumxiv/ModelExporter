bl_info = {
    "name" : "ModelExporter",
    "author" : "lumxiv",
    "description" : "Export models frame by frame to gltf for use in VFXEditor",
    "version": (1, 0, 1),
    "blender" : (4, 5, 4),
    "location" : "3D View > Tools (Right Side) > ModelExporter",
    "warning" : "",
    "category" : "Animation",
    "wiki_url": 'https://github.com/lumxiv/ModelExporter',
    "tracker_url": 'https://github.com/lumxiv/ModelExporter/issues',
}

from . import addon

def register():
	addon.register()

def unregister():
    addon.unregister()