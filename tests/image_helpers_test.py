from image_helpers import get_image_pixels


def test_get_image_pixels():
    pixels = get_image_pixels(
        "https://livestock.extension.wisc.edu/files/2021/08/brown-chicken.jpg"
    )
    assert len(pixels) == 249
    assert len(pixels[0]) == 320
    assert (pixels[0][0]) == [73, 66, 11]