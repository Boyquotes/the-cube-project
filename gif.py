import os
from glob import glob
from PIL import Image


"""
Make GIF from frames
"""


dir_path = os.path.dirname(os.path.realpath(__file__))

for nft_path in glob('{}/output/*/'.format(dir_path)):
	print('---- Creating: {} ----'.format(nft_path))

	frames = []
	for frame in sorted(glob('{}*.png'.format(nft_path))):
		frames.append(Image.open(frame))

	first_frame = frames[0]
	first_frame.save(
		'{}/result.gif'.format(nft_path), 
		format="GIF", 
		append_images=frames,
		save_all=True, 
		duration=41, 
		loop=0
	)

