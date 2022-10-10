from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import random as rand
import PIL.ImageOps

img = Image.open("st2.png")

contrast = ImageEnhance.Contrast(img)
contrast = contrast.enhance(1) # set FACTOR > 1 to enhance contrast, < 1 to decrease
a,b = img.size
imge = Image.new("RGBA",(a,b),(0,0,0,0))
cont = ImageEnhance.Contrast(img)
cont.enhance(2).save("fan.png")

image = Image.new("RGBA",(a,b),(0,0,0,0))
draw = ImageDraw.Draw(image)
draw. rectangle((0,0,a,b), fill="black")
drawor = ImageDraw.Draw(img)
blr = img.filter(ImageFilter.BLUR)
blr.save("blur.png")
def bw(img,
    image):
   color_image = Image.open(img)
   bw = color_image.convert('L')
   bw.save(image)
def avclr(filename):
    i = Image.open(filename)
    h = i.histogram()
    # split into red, green, blue
    r = h[0:256]
    g = h[256:256*2]
    b = h[256*2: 256*3]
    # perform the weighted average of each channel:
    # the *index* is the channel value, and the *value* is its weight
    return (
        sum( i*w for i, w in enumerate(r) ) / sum(r),
        sum( i*w for i, w in enumerate(g) ) / sum(g),
        sum( i*w for i, w in enumerate(b) ) / sum(b)
    )
ac = avclr("st2.png")
obj = img.load()
pix =0
cl =[]
cr = []
"""for p in range(a):
    for pp in range(b):
        cl.append(list(obj[p,pp]))
        cr.append([p,pp])
for i in range(len(cl)):
        rr = abs((cl[i][0]-100)//2)
        gg = abs((cl[i][1]-100)//2)
        bb = abs((cl[i][2]-100)//2)
        drawor.point((cr[i]), fill= (rr,gg,bb))
"""
ac = avclr("st2.png")
image.save("fin.png") 
bw("st2.png","andf.png")
andf  =  Image.open("andf.png")
cont = ImageEnhance.Contrast(andf)
cont.enhance(3).save("fan.png")
fan = Image.open("fan.png")
inv = PIL.ImageOps.invert(fan)
#inv.save("rbd.png")
im1 = inv.filter(ImageFilter.GaussianBlur(radius=1.5))
im1.save("im1.png")
obj = img.load()
pix =0
cl =[]
cr = []