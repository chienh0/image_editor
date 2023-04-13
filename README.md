## Image Editor: Filters Web Images using the Terminal
### Project Goal 
To enable users to filter web images using only a URL.

### Tech Stack
<p float='left'>
  <img src='/examples/logo_python.png' width='110' />
</p>

### From Picture to Pixels
The program finds a picture on the web, loads the picture file into Python, and converts that file into an array of pixels. Each pixel contains Red, Green, Blue (RGB) values that can be manipulated.

### How to Use:
* Find a picture on the web. A smaller picture is actually better at first, since your program will run faster and you can iterate more quickly. Even a 200x300 picture has 60,000 pixels!
  * Right-click on the image and select "Copy Image Address".
  * The URL must be to an image file (ending with an extension like .jpg/.png/.gif/.webp), not to a webpage displaying the image.
* Using the terminal, 
  * Clone the repository:
  ```
  git clone https://github.com/chienqho/image_editor.git
  ```
  * Create conda environment to install and manage all the python packages:
  ```
  conda env create --file environment.yml   
  ```
  * Activate conda environment to access the recently installed python packages:
  ```
  conda activate image_env 
  ```
  * Execute the main Python script:
  ```
  python3 main.py 
  ```
  * Enter the URL of the desired image when prompted:
  ```
  Enter the URL of the image to process:
  ```

### Exploring the Pixel Data
Let's explore how the pixels are actually stored. We'll start with a simpler example: a picture that's just 2 pixels by 2 pixels.
<p float='left'>
  <img src='/examples/rgbsquare.png' width='50' />
</p>

In the top row, the first pixel is black and the second is red. In the bottom row, the first pixel is green and the second is blue.

The pixels list is not just a nested list, it's a 3-dimensional nested list: a list of lists of lists.

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

### Available Filters 
The program offers several filters that you can use to modify the image, including:
  * Remove Red/Green/Blue color
  * Invert Red/Green/Blue color
  * Grayscale conversion
  * Horizontal/vertical flip

<p float='left'>
  <img src='/examples/chicken_original.png' width='300' />&nbsp;&nbsp;&nbsp;&nbsp;
  <img src='/examples/chicken_grayscale.png' width='300' />&nbsp;&nbsp;&nbsp;&nbsp; 
  <img src='/examples/chicken_total_inversion.png' width='300' /> 
</p>

<p float='left'>
  <img src='/examples/chicken_red_removed.png' width='300' />&nbsp;&nbsp;&nbsp;&nbsp;
  <img src='/examples/chicken_green_removed.png' width='300' />&nbsp;&nbsp;&nbsp;&nbsp; 
  <img src='/examples/chicken_blue_removed.png' width='300' />
</p>

<p float='left'>
  <img src='/examples/chicken_red_inverted.png' width='300' />&nbsp;&nbsp;&nbsp;&nbsp;
  <img src='/examples/chicken_green_inverted.png' width='300' />&nbsp;&nbsp;&nbsp;&nbsp; 
  <img src='/examples/chicken_blue_inverted.png' width='300' />
</p>

<p float='left'>
  <img src='/examples/chicken_horizontal_flip.png' width='300' />&nbsp;&nbsp;&nbsp;&nbsp;
  <img src='/examples/chicken_vertical_flip.png' width='300' />&nbsp;&nbsp;&nbsp;&nbsp; 
  <img src='/examples/chicken_horizontal_and_vertical_flip.png' width='300' />
</p>

### Attribution
Inspiration for this project comes from the [PPM Image Editor project](http://nifty.stanford.edu/2012/guerin-image-editor/) by Joshua Guerin T and Debby Keen, as presented at SIGCSE Nifty Projects 2012.
