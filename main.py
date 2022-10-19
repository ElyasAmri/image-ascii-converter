# the image library (to be downloaded using instructions in README.md)
from PIL import Image
# useful utility for handling command-line arguments
from argparse import ArgumentParser

# the filling characters in descending order
ascii_chars = '@#$%?*+;:,.'


def main(args):
	# the file to be opened
	path = args.file
	# the desired output width
	width = int(args.width)
	# the output file path
	out_path = args.output

	# open and constructs image using PIL image opener
	with Image.open(path) as image:
		# resize image to the desired width
		resized = resize_image(image, width)

		# convert image to grayscale
		grayified = resized.convert('L')

		# get pixels as a single-dimension list
		pixels = grayified.getdata()

		# perform operation on each pixel
		ascii_image = [get_pixel_value(pixel) for pixel in pixels]

	# converts single-dimension list of characters to a 2D list of width and height
	ascii_image = [ascii_image[i * width:(i + 1) * width] for i in range(grayified.height)]

	# converts 2D-list of characters to a string
	# each row separated by a newline
	seq = '\n'.join([''.join(i) for i in ascii_image])

	# write the result string to output file
	with open(out_path, 'w') as out:
		out.write(seq)

	print(f'the result has been written to {out_path}')


def resize_image(image, new_width):
	"""resizes an image while preserving aspect ratio

	:param image: the image to be resized
	:param new_width: the new width to resize the image with
	:return: letter representing pixel brightness
	"""
	width, height = image.size
	ratio = height / width
	new_height = int(ratio * new_width)
	resized_image = image.resize((new_width, new_height))
	return resized_image


def get_pixel_value(v):
	"""Converts a gray pixel into an ascii character

	:param v: the pixel to be converted
	:return: letter representing pixel brightness
	"""
	return ascii_chars[v // 25]


if __name__ == '__main__':
	# creates the argument parser to handle command-line input and runs main with it
	ap = ArgumentParser()
	ap.add_argument('file')
	ap.add_argument('--width', default='400')
	ap.add_argument('--output', default='result.txt')

	args = ap.parse_args()
	main(args)
