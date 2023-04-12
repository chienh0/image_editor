## Photo Filter: Applying filters to photos, like inversion, flipping, and grayscale

### Project Goal 
To develop a photo filtering application that allows users to filter their images using nested loops and lists in Python to manipulate the the Red, Green, Blue (RGB) values of individual pixels.

### Tech Stack
<p float='left'>
  <img src='/logos/logo_python.png' width='130' />
</p>

### From Picture to Pixels

In this first step, the program finds a picture on the web, loads the picture file into Python, and converts that file into an array of pixels. That requires the use of several external libraries, so we've written all the pixel loading code for you.

### ✏︎ For you to do:
* Find a picture on the web. A smaller picture is actually better at first, since your program will run faster and you can iterate more quickly. Even a 200x300 pixture has 60,000 pixels!
* Replace the current value of the `url` variable with the address to your picture. That URL _must_ be to an image file (ending with an extension like .jpg/.png/.gif/.webp), not to a webpage displaying the image.

```python
# Import some standard libraries
import doctest
import copy

# Import external libraries
import numpy
import cv2
from skimage import io
from google.colab.patches import cv2_imshow


def get_image_pixels(image_url):
  """ Returns a nested list of the pixels for the image located at image_url"""
  # Fetch the image
  image = io.imread(image_url)
  # Convert the Blue-Green-Red representation to Red-Green-Blue representation
  image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  # Get an array of pixels representing the image
  pixel_data = numpy.asarray(image2).tolist()
  for row in pixel_data:
    for pixel in row:
      pixel[0], pixel[2] = pixel[2], pixel[0]
  return pixel_data

def render_pixels(pixel_data):
  """ Displays the image represented by pixel_data"""
  # Write the pixel_data to a local image file
  transformed_data = copy.deepcopy(pixel_data)
  for row in transformed_data:
    for pixel in row:
      pixel[0], pixel[2] = pixel[2], pixel[0]
  cv2.imwrite('rendered.jpg', numpy.array(transformed_data))
  # Display that image file in the notebook
  cv2_imshow(cv2.imread("rendered.jpg"))

# Use the functions above to fetch pixel data and render the original data
url = 'https://livestock.extension.wisc.edu/files/2021/08/brown-chicken.jpg'
pixel_data = get_image_pixels(url)
render_pixels(pixel_data)
```

### Exploring the Pixel Data

Before you start messing with the pixels list of your picture, let's explore how the pixels are actually stored.

We'll start with a simpler example: a picture that's just 2 pixels by 2 pixels.

![rgbsquare.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACAgMAAAAP2OW3AAAADFBMVEUAAAD/AAAA/wAAAP+bwBPcAAAADElEQVR4nGMQYNgAAADkAMEnqOhXAAAAAElFTkSuQmCC)

That's super small, so small it probably just looks like dirt on the screen. Here's a blown-up version so you can see each pixel:

![rgbsquare_blownup.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUAgMAAADw5/WeAAAADFBMVEUAAAD/AAAA/wAAAP+bwBPcAAAAGElEQVR4nGNgYGANDWUgj1y1av3//+SRAAVdLuEsKjYYAAAAAElFTkSuQmCC)

In the top row, the first pixel is black and the second is red. In the bottom row, the first pixel is green and the second is blue.

#### ✏︎ For you to do

Run the code below to see what the entire pixel list looks like. There should only be four pixels in the list, since it's a 2x2 picture.

The pixels list is not just a nested list, it's a 3-dimensional nested list: a list of lists of lists.

Here's another way of formatting the list which may make the structure clearer:

```
[
  [ [0, 0, 0],  [255, 0, 0]  ],
  [ [0, 255, 0], [0, 0, 255] ]
]
```

The outer list contains lists which represents each row in the picture. Then, each of the row lists contains lists which represent each color channel in the pixel. 

Each pixel is represented using the  Red-Green-Blue (RGB) scheme for pixels, with a minimum value of 0 and maximum value of 255. The first pixel is black, which is 0 in all channels (devoid of color!). The second pixel in the top row is pure red, so there's a 255 as the first item and the other values are 0. Check out the bottom two pixels and see if the color values align with what you expect.

_If you haven't used the RGB color scheme before, play around with [this RGB color picker](https://www.rapidtables.com/web/color/RGB_Color.html) to get a feel for how different amounts of R/G/B make up different colors._

The picture you loaded in above is represented the same way in the `pixel_data` list, but it's a much longer list, so it's harder to just look at it and immediately understand each value. 

### ✏︎ For you to do

Run the code snippets below to explore different parts of the `pixel_data` list. Do the values make sense? You're welcome to do some additional exploration beyond what we've suggested.

### Attribution

Inspiration for this project comes from the [PPM Image Editor project](http://nifty.stanford.edu/2012/guerin-image-editor/) by Joshua Guerin T and Debby Keen, as presented at SIGCSE Nifty Projects 2012.