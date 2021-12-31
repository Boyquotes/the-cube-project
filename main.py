import bpy
from random import randint


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
        cube.keyframe_insert(data_path="rotation_euler", frame=1)
        cube.rotation_euler[2] = 6
        cube.keyframe_insert(data_path="rotation_euler", frame=60)
        
        
        
def create_light():
    """
    Create light
    :return: None
    """
    
    light = bpy.data.lights.new(name="Light.001", type='POINT')
    light.energy = 10000
    light_object = bpy.data.objects.new(name="Light.001", object_data=light)
    bpy.context.collection.objects.link(light_object)
    light_object.location = (20.6245, -23.59, 8.8291)
    light_object.rotation_euler = (0.9887, -0.7407, 0.7169)
    
    
    
def create_camera():
    """
    Create camera
    :return: None
    """
    
    camera = bpy.data.cameras.new("Camera")
    camera.lens = 50
    camera_object = bpy.data.objects.new("Camera", camera)
    camera_object.location = (36.4522, -34.3497, 24.8413)
    camera_object.rotation_euler = (1.109, 0, 0.8149)
    camera_object.keyframe_insert(data_path="location", frame=1)
    bpy.context.collection.objects.link(camera_object)
    
    
    
def create_background():
    """
    Create room
    :return: None
    """
    
    bpy.ops.mesh.primitive_plane_add(size=60, location=(-8, 0, -17))
    bpy.ops.mesh.primitive_plane_add(size=60, location=(-8, 28.196, -17), rotation=(1.57, 0, 0))
    bpy.ops.mesh.primitive_plane_add(size=60, location=(-38.013, 0, -17), rotation=(0, 1.57, 0))
    
    
    
def remove_all():
    """
    Remove all objects
    :return: None
    """
    
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
        
        
    
if __name__ == "__main__":
    remove_all()
    generate_cubes(80)
    create_camera()
    create_light()
    create_background()
    animate_cubes()
    
    