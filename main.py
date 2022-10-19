from PIL import Image
from argparse import ArgumentParser

ascii_chars = r'@#$%?*+;:,.'


def main(args):
	path = args.file
	width = int(args.width)
	height = int(args.height)
	with Image.open(path) as image:
		resized = resize_image(image, width)
		grayified = resized.convert('L')
		pixels = grayified.getdata()
		ascii_image = [get_pixel_value(pixel) for pixel in pixels]
	ascii_image = [ascii_image[i*width:(i+1)*width] for i in range(height)]

	seq = '\n'.join([''.join(i) for i in ascii_image])

	with open('result.txt', 'w') as out:
		out.write(seq)



def resize_image(image, new_width):
	width, height = image.size
	ratio = height / width
	new_height = int(ratio * new_width)
	resized_image = image.resize((new_width, new_height))
	return resized_image


def get_pixel_value(v):
	return ascii_chars[v // 25]


if __name__ == '__main__':
	ap = ArgumentParser()
	ap.add_argument('file')
	ap.add_argument('--width', default='400')

	args = ap.parse_args()
	main(args)
