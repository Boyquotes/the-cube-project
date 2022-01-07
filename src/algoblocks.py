import bpy
import json
from random import randint
from random import uniform
       

def create():
    """
    Create NFT
    :return: None
    """
      
    bpy.ops.scene.new()
    
    for nft_number in range(0, 51):
        generate_cubes()
        create_light()
        create_camera()
        create_background()
        
        # Render
        render(nft_number)
        
        # Remove assets
        clean()
        
    return
        
        

def generate_cubes():
    """
    Generate n cubes
    :return: None
    """
    
    # Create cube collection
    cube_collection = bpy.context.blend_data.collections.new(name='Cubes')
    bpy.context.collection.children.link(cube_collection)
    
    # Set options for material
    materials = bpy.data.materials
    r = uniform(0, 1)
    g = uniform(0, 1)
    
    for _ in range(0, 50):
        x = uniform(-uniform(0, 5), uniform(0, 5))
        y = uniform(-uniform(0, 5), uniform(0, 5))
        z = uniform(-uniform(0, 5), uniform(0, 5))
        bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
        
        # Get current cube object
        cube_object = bpy.context.object
        cube_object.scale = (uniform(0.2, 1), uniform(0.2, 1), uniform(0.2, 1))
        
        # Add cube to collection
        bpy.data.collections['Cubes'].objects.link(cube_object)
        
        # Assign material
        b = uniform(0, 1) 
        material = materials.new(name='CubeColor')
        material.diffuse_color = (r, g, b, 1)
        cube_object.data.materials.append(material)
        
        # Animate cube
        cube_object.keyframe_insert(data_path='rotation_euler', frame=1)
        cube_object.rotation_euler[2] = 6
        cube_object.keyframe_insert(data_path='rotation_euler', frame=24)
        
        
    return



def create_camera():
    """
    Create camera
    :return: None
    """
    
    camera = bpy.data.cameras.new('Camera')
    camera.lens = 50
    camera_object = bpy.data.objects.new('Camera', camera)
    camera_object.location = (19.348, -18.227, 13.144)
    camera_object.rotation_euler = (1.109, 0, 0.8149)
    bpy.context.collection.objects.link(camera_object)
    bpy.context.scene.camera = camera_object
    
    return
        
        
        
def create_light():
    """
    Create light
    :return: None
    """
    
    light = bpy.data.lights.new(name='Light', type='POINT')
    light.energy = 10000
    light.use_shadow = False
    light_object = bpy.data.objects.new(name='Light', object_data=light)
    bpy.context.collection.objects.link(light_object)
    light_object.location = (20.6245, -23.59, 14.4891 )
    light_object.rotation_euler = (0.9887, -0.7407, 0.7169)
    
    return
    
    
    
def create_background():
    """
    Create background plane
    :return: None
    """
    
    # Create background collection
    background_collection = bpy.context.blend_data.collections.new(name='Background')
    bpy.context.collection.children.link(background_collection)
    
    bpy.ops.mesh.primitive_plane_add(
        size=60, 
        location=(-10.603, 9.8974, -10), 
        rotation=(0, 1.57, -0.7853)
    )
    
    plane_object = bpy.context.object
    
    # Set color
    materials = bpy.data.materials
    material = materials.new(name='BackgroundColor')
    material.diffuse_color = (0, 0, 0, 1)
    plane_object.data.materials.append(material)
    
    bpy.data.collections['Background'].objects.link(plane_object)
    
    return
    
    
    
def render(nft_number):
    """
    Set export settings and export image
    :return: None
    """
    
    path = '/Users/dennis/Developer/the-cube-project/src/output/nft-{}/'.format(nft_number)
    bpy.data.scenes['Scene.001'].frame_end = 30
    bpy.data.scenes['Scene.001'].render.resolution_x = 500
    bpy.data.scenes['Scene.001'].render.resolution_y = 500
    bpy.data.scenes['Scene.001'].render.filepath = path
    bpy.data.scenes['Scene.001'].render.image_settings.file_format = 'PNG'
    bpy.data.scenes['Scene.001'].render.image_settings.compression = 20
    bpy.ops.render.render(animation=True, write_still=True, scene='Scene.001')
    
    return
        
    
                    
def clean():
    """
    Clean scene
    :return: None
    """
    
    # Delete assets in scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Remove materials if exists
    materials = bpy.data.materials
    for material in materials:
        materials.remove(material)
    
    return
        
        
    
if __name__ == '__main__':
    create()
    
