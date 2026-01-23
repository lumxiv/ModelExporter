bl_info = {
	"name" : "GLTF-ModelFrameExporter",
	"author" : "lumxiv",
	"description" : "Export models frame by frame to gltf for use in VFXEditor",
	"version": (1, 0, 0),
	"blender" : (4, 5, 4),
	"location" : "3D View > Tools (Right Side) > ModelFrameExporter",
	"warning" : "",
	"category" : "Animation",
	"wiki_url": 'https://github.com/lumxiv/GTLF-ModelFrameExporter',
    "tracker_url": 'https://github.com/lumxiv/GTLF-ModelFrameExporter/issues',
}

from . import addon

def register():
	addon.register()

def unregister():
    addon.unregister()