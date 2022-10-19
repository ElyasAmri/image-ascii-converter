# image-ascii-converter
Convert an image to letters ([ASCII](https://en.wikipedia.org/wiki/ASCII)) representation.

# Usage:
```python main.py <path_to_image> [--width <width>] [--output <path_to_output>]```

For easy use, copy the desired image into the same directory as the source-code (but you can specify the absolute path if you want):

```python main.py my-image.jpg```

You can specify the output width (defaults to 400 pixels):

```python main.py my-image.jpg --width 100```

You can specify the output path (defaults to result.txt):

```python main.py my-image.jpg --output my-ascii-image.txt```

# Install:
1. Clone this repository:
```git clone https://github.com/ElyasAmri/image-ascii-converter```

2. Change directory to image-ascii-converter:
```cd image-ascii-converter```

3. Install the dependencies:
```python -m pip install -r requirements.txt```
