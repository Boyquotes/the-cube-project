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
        
        # Add assets
        generate_cubes(randint(30, 70))
        create_light()
        create_camera()
        create_background()
        
        # Create animation
        animate_cubes()
        
        # Add materials
        assign_material_to_cubes()
        assign_material_to_background()
        
        # Render
        render(nft_number)
        
        # Remove assets
        clean()
        
    return
        
        

def generate_cubes(n):
    """
    Generate n cubes
    :param n: string, required
    :return: None
    """
    
    # Create cube collection
    cube_collection = bpy.context.blend_data.collections.new(name='Cubes')
    bpy.context.collection.children.link(cube_collection)
    
    x_bound = uniform(0, 5)
    y_bound = uniform(0, 5)
    z_bound = uniform(0, 5)
    
    for _ in range(0, n):
        x = uniform(-x_bound, x_bound)
        y = uniform(-y_bound, y_bound)
        z = uniform(-z_bound, z_bound)
        bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
        
        # Get current cube object
        cube_object = bpy.context.object
        
        # Add cube to collection
        bpy.data.collections['Cubes'].objects.link(cube_object)
        
    return
        
        
        
def animate_cubes():
    """
    Create rotation animation
    :return: None
    """
    
    cubes = bpy.data.collections['Cubes'].all_objects
    
    # Select all cubes
    for cube in cubes:
        cube.keyframe_insert(data_path='rotation_euler', frame=1)
        cube.rotation_euler[2] = 6
        cube.keyframe_insert(data_path='rotation_euler', frame=24)
        
    return
        
        
        
def create_light():
    """
    Create light
    :return: None
    """
    
    light = bpy.data.lights.new(name='Light', type='POINT')
    light.energy = 10000
    light_object = bpy.data.objects.new(name='Light', object_data=light)
    bpy.context.collection.objects.link(light_object)
    light_object.location = (20.6245, -23.59, 8.8291)
    light_object.rotation_euler = (0.9887, -0.7407, 0.7169)
    
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
    
    
    
def create_background():
    """
    Create room
    :return: None
    """
    
    # Create background collection
    background_collection = bpy.context.blend_data.collections.new(name='Background')
    bpy.context.collection.children.link(background_collection)
    
    bpy.ops.mesh.primitive_plane_add(size=60, location=(-8, 0, -17))
    plane_object = bpy.context.object
    bpy.data.collections['Background'].objects.link(plane_object)
    
    bpy.ops.mesh.primitive_plane_add(size=60, location=(-8, 28.196, -17), rotation=(1.57, 0, 0))
    plane_object = bpy.context.object
    bpy.data.collections['Background'].objects.link(plane_object)
    
    bpy.ops.mesh.primitive_plane_add(size=60, location=(-38.013, 0, -17), rotation=(0, 1.57, 0))
    plane_object = bpy.context.object
    bpy.data.collections['Background'].objects.link(plane_object)
    
    return
    
    
    
def assign_material_to_cubes():
    """
    Create material if is None and assign it to cubes
    :return: None
    """
    
    materials = bpy.data.materials
    
    r = uniform(0, 1)
    g = uniform(0, 1)
    
    cubes = bpy.data.collections['Cubes'].all_objects
    for index, cube in enumerate(cubes):
        material = materials.new(name='CubeColor.{}'.format(index))
        b = uniform(0, 1) 
        material.diffuse_color = (r, g, b, 1)
        cube.data.materials.append(material)
        
    return 
        
        
        
def assign_material_to_background():
    """
    Create material if is None and assign it to background
    :return: None
    """
    
    material = bpy.data.materials.get('BackgroundMaterial')
    if material is None:
        material = bpy.data.materials.new(name='BackgroundMaterial')
        
    material.diffuse_color = (0, 0, 0, 1)
    planes = bpy.data.collections['Background'].all_objects
    for plane in planes:
        plane.data.materials.append(material)
        
    return
    
    
    
    
def render(nft_number):
    """
    Export animation as image sequence
    :return: None
    """
    
    path = '/Users/dennis/Developer/open-source-cubes/output/nft-{}/'.format(nft_number)
    bpy.data.scenes['Scene.001'].render.resolution_x = 600
    bpy.data.scenes['Scene.001'].render.resolution_y = 600
    bpy.data.scenes['Scene.001'].render.filepath = path
    bpy.data.scenes['Scene.001'].render.image_settings.file_format = 'PNG'
    bpy.data.scenes['Scene.001'].render.image_settings.compression = 20
    bpy.data.scenes['Scene.001'].frame_end = 48
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
    
