import json
from image_helpers import get_image_pixels, render_pixels
from image_filters import remove_red, remove_green, remove_blue, invert_red, invert_green, invert_blue, grayscale, flip_horizontal, flip_vertical

# Read the configuration file
with open('config.json') as f:
    config = json.load(f)

# Prompt the user for a new URL
url = input('Enter the URL of the image to process: ')

# Update the URL value in the configuration file
config['image']['url'] = url

# Write the updated configuration file back to disk
with open('config.json', 'w') as f:
    json.dump(config, f)

# Use the functions above to fetch pixel data and render the original data
pixel_data = get_image_pixels(url)
render_pixels(pixel_data, 'Original')

# Render the color removed images
render_pixels(remove_red(pixel_data), 'Red Removed')
render_pixels(remove_green(pixel_data), 'Green Removed')
render_pixels(remove_blue(pixel_data), 'Blue Removed')

# Render the inverted color images
render_pixels(invert_red(pixel_data), 'Red Inverted')
render_pixels(invert_green(pixel_data), 'Green Inverted')
render_pixels(invert_blue(pixel_data), 'Blue Inverted')

# Render the total inversion image
render_pixels(invert_blue(invert_green(invert_red(pixel_data))), 'Total Inversion')

# Render the grayscale image
render_pixels(grayscale(pixel_data), 'Grayscale')

# Render the horizontal flip image
render_pixels(flip_horizontal(pixel_data), 'Horizontal Flip')

# Render the vertical flip image
render_pixels(flip_vertical(pixel_data), 'Vertical Flip')

# Render the horizontal and vertical flip image
render_pixels(flip_vertical(flip_horizontal(pixel_data)), 'Horizontal and Vertical Flip')