# pip install pillow

from PIL import Image
def image_info():
    im = Image.open('images/tree.jpg')
    print(im.filename)
    print(im.format)
    print(im.mode)
    print(im.size)      # a tuple.
##image_info()

''' The loaded image is saved to a temporary BMP file,
and uses a BMP display program to show it (on Window is Paint).
'''
##Image.open('images/tree.jpg').show()

# save() saves the loaded image into a file and may convert into other format.
##Image.open('images/tree.jpg').save('tree.png')   # Try: .gif, tif

def resize():
    im = Image.open('images/rose.jpg')
    im.show()
    im = im.resize((50, 50))
    im.show()
    # im.save('rose_thumb.png')
##resize()

def crop():
    box = (5, 27, 38, 92)  # (x, y., width, height)
    im = Image.open('images/bird3.png').crop(box)
    im.show()
##crop()

def paste():  # pastes an image on another image.
    b = Image.open('images/bird3.png') # Blackground should be transparent.
    se = Image.open('images/sea.png')
    se.paste(b, (100, 100))
    se.show()
##paste()

# rotate(<degree>) rotates the image by <degree>.
##Image.open('images/bird3.png').rotate(20).show()

''' transpose(<operator>) processes the image by <operator>.
Image defines a lot of operators.
'''
def flip():
    Image.open('images/bird3.png').transpose(Image.FLIP_LEFT_RIGHT).show()
    Image.open('images/bird3.png').transpose(Image.FLIP_TOP_BOTTOM).show()
##flip()

''' filter(<filter>) processes the image by <filter>.
ImageFilter defines a lot of filters.
'''
from PIL import ImageFilter
def filters():
    im = Image.open('images/road.jpg')
    w, h = im.size
    ims = Image.new('RGBA', (2*w, 2*h))
    ims.paste(im.filter(ImageFilter.EDGE_ENHANCE), (0,0))
    ims.paste(im.filter(ImageFilter.EMBOSS), (w,0))
    ims.paste(im.filter(ImageFilter.FIND_EDGES), (0,h))
    ims.paste(im.filter(ImageFilter.CONTOUR), (w,h))
    ims.show()
##filters()

from PIL import ImageEnhance
def enhance():
    def position(i, w, h):
        return (0,0) if i == 1 else (w,0) if i == 2 else (0,h) if i == 3 else (w,h)

    im = Image.open('images/tree.jpg')
    # im = Image.open('images/sea.png')
    w, h = im.size
    ims = Image.new('RGBA', (2*w, 2*h))
    for i in range(1, 5):
        e = ImageEnhance.Contrast(im).enhance(i)
##        e = ImageEnhance.Sharpness(im).enhance(i*10)
##        e = ImageEnhance.Brightness(im).enhance(i/2)
##        e = ImageEnhance.Color(im).enhance(i)
        ims.paste(e, position(i, w, h))
    ims.show()
##enhance()

# putpixel((x,y), color) draws a pixel at the coordinate (x,y).
def draw_square(w):
   hw = w // 2 
   # im = Image.new("L", (w, w), 255) # Create an empty B/W image
   im = Image.new("RGB", (w, w), 255) # Create an empty RGB image
   for x in range(-hw, hw):
      for y in range(-hw, hw):
         # im.putpixel((x,y), 0)
         im.putpixel((x,y), (125, 0, 0))
   im.show()
##draw_square(300)

# Image Processing:
# getpixel((x,y)) returns the color of the pixel at x,y.
def image_process():
    im =  Image.open('images/rose.jpg')
    # im = Image.open('images/flower.jpg')
    w, h = im.size
    for x in range(w):
        for y in range(h):
            r, g, b = im.getpixel((x, y))
            im.putpixel((x,y), (g, r, b))   # Swap red and green
                        # Try: (b, g, r)
    im.show()
##image_process()

##----------------------------------------------------------

## Graphic Drawing:
## The PIL graphic is simple but not as power as the Pygame graphic.
## We need an ImageDraw object attach to an existing image.
## Then we can draw on the ImageDraw object.
from PIL import ImageDraw
def draw():
    im = Image.new('L', (400, 300), 255)
    imd = ImageDraw.Draw(im)
    imd.line((100, 100, 200, 200))
    imd.ellipse((20, 20, 80, 50), fill=0)
    imd.rectangle((200, 20, 280, 70))
    imd.polygon([210, 220, 250, 230, 300, 210])
    im.show()
draw()

## Text:
from matplotlib import font_manager
from PIL import ImageFont
def text():
    im = Image.new('L', (250, 100), 255)
    imd = ImageDraw.Draw(im)
    ttf = ImageFont.truetype(font_manager.findfont('Lucida Handwriting'), 24)
    imd.text((75, 30), 'Hello!', font=ttf)
    im.show()  
# text()




