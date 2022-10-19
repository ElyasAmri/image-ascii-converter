# import some image library
from argparse import ArgumentParser, Namespace

ascii_chars = r'@#$%?*+;:,.'


def main(args: Namespace):
	path = args['file']
	with open(path, 'r'):
		# todo: get actual width
		width = 0
		# todo: get actual height
		height = 0
		# todo: replace i * j with get actual pixel from file
		ascii_image = [[get_pixel_value(i * j) for i in range(width)] for j in range(height)]

	s = '\n'.join([''.join(i) for i in ascii_image])
	print(s)


def get_pixel_value(v):
	return ascii_chars[v // 23]


if __name__ == '__main__':
	ap = ArgumentParser()
	ap.add_argument('file', required=True)
	ap.add_argument('width', default='400')
	ap.add_argument('height', default='400')

	args = ap.parse_args()
	main(args)
