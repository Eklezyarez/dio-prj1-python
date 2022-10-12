from socketserver import ThreadingUnixDatagramServer
from skimage.transform import resize

def resize_image(image, proportion):
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1."
    height = round(image,sahpe[0] * proportion)
    width = round(image,sahpe[1] * proportion)
    iamge_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized