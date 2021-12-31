import glob
import os
from PIL import Image


"""
Make GIF from frames
"""


dir_path = os.path.dirname(os.path.realpath(__file__))
output_path = '{}/output'.format(dir_path)
cube_folders = glob.glob('{}/cube-*/'.format(output_path))

for index, cube_folder in enumerate(cube_folders):
	print('---- Creating: {} ----'.format(cube_folder))
	frames = []
	for frame in sorted(glob.glob('{}/*.png'.format(cube_folder))):
		frames.append(Image.open(frame))

	first_frame = frames[0]
	first_frame.save(
		'{}/gifs/{}.gif'.format(output_path, index), 
		format="GIF", 
		append_images=frames,
		save_all=True, 
		duration=41, 
		loop=0
	)

