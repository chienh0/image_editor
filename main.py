import json
from image_helpers import get_image_pixels, render_pixels

# Read the configuration file
with open('config.json') as f:
    config = json.load(f)

# Prompt the user for a new URL
url = input('Enter the URL of the JPG image to process: ')

# Update the URL value in the configuration file
config['image']['url'] = url

# Write the updated configuration file back to disk
with open('config.json', 'w') as f:
    json.dump(config, f)

# Use the functions above to fetch pixel data and render the original data
pixel_data = get_image_pixels(url)
render_pixels(pixel_data)