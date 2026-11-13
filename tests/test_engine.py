from PIL import Image
from image_cleaner.engine import convert_to_black, convert_to_grayscale, remove_corner_background

def test_black_white_exact():
    im = Image.new("RGB", (2, 1))
    im.putpixel((0, 0), (0, 0, 0)); im.putpixel((1, 0), (255, 255, 255))
    out = convert_to_black(im, 128)
    assert out.getpixel((0, 0))[:3] == (0, 0, 0)
    assert out.getpixel((1, 0))[:3] == (255, 255, 255)

def test_grayscale_keeps_alpha():
    im = Image.new("RGBA", (1, 1), (20, 80, 150, 40))
    p = convert_to_grayscale(im).getpixel((0, 0))
    assert p[0] == p[1] == p[2] and p[3] == 40

def test_corner_removal():
    im = Image.new("RGB", (3, 3), "white"); im.putpixel((1, 1), (0, 0, 0))
    out = remove_corner_background(im, 0)
    assert out.getpixel((0, 0))[3] == 0
    assert out.getpixel((1, 1))[3] == 255
