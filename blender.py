import bpy
from random import randint
from random import uniform
       

def generate_cubes(n):
    """
    Generate n cubes
    :param n: string, required
    :return: None
    """
    
    # Create cube collection
    cube_collection = bpy.context.blend_data.collections.new(name='Cubes')
    bpy.context.collection.children.link(cube_collection)
    
    for _ in range(0, n):
        x = randint(-5,5)
        y = randint(-5,5)
        z = randint(-5,5)
        bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
        
        # Get current cube object
        cube_object = bpy.context.object
        
        # Add cube to collection
        bpy.data.collections['Cubes'].objects.link(cube_object)
        
        
        
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
    
    
    
def create_camera():
    """
    Create camera
    :return: None
    """
    
    camera = bpy.data.cameras.new('Camera')
    camera.lens = 50
    camera_object = bpy.data.objects.new('Camera', camera)
    camera_object.location = (36.4522, -34.3497, 24.8413)
    camera_object.rotation_euler = (1.109, 0, 0.8149)
    bpy.context.collection.objects.link(camera_object)
    
    
    
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
    
    
    
def assign_material_to_cubes():
    """
    Create material if is None and assign it to cubes
    :return: None
    """
    
    material = bpy.data.materials.get('CubeMaterial')
    if material is None:
        material = bpy.data.materials.new(name='CubeMaterial')
        
    r = uniform(0, 1)
    g = uniform(0, 1)
    b = uniform(0, 1)
    
    material.diffuse_color = (r, g, b, 1)
            
        
    cubes = bpy.data.collections['Cubes'].all_objects
    for cube in cubes:
        cube.data.materials.append(material)
        
        
        
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
    
    
    
def remove_all():
    """
    Remove all objects
    :return: None
    """
    
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    
    
def export_image_sequence(folder_name):
    """
    Export animation as image sequence
    :return: None
    """
    
    path = '/Users/dennis/Developer/open-source-cubes/output/{}/'.format(folder_name)
    bpy.data.scenes['Scene'].render.filepath = path
    bpy.data.scenes['Scene'].render.image_settings.file_format = 'PNG'
    bpy.data.scenes['Scene'].frame_end = 48
    bpy.ops.render.render('INVOKE_DEFAULT', animation=True, write_still=True)
        
        
    
if __name__ == '__main__':
    remove_all()
    generate_cubes(80)
    create_camera()
    create_light()
    create_background()
    animate_cubes()
    assign_material_to_cubes()
    assign_material_to_background()
    
    # Change folder_name in every run
    export_image_sequence(folder_name='cube-12')
    
    