"""imgfin = Image.new("RGBA",(1920,540),(0,0,0,0))
image = Image.new("RGBA",(960,540),(0,0,0,0))
draw = ImageDraw.Draw(image)
draw.polygon(((200, 200), (300, 100), (250, 50)), fill=(255, 255, 0), outline=(0, 0, 0))
 fill=(255, 255, 255), 
"""
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import random as rand
import PIL.ImageOps
dim_w=600
dim_h=600
imgbig_final = Image.new("RGBA",(dim_w,dim_h),(0,0,0,0))
draw_1 = ImageDraw.Draw(imgbig_final)

draw_1.rectangle((0, 0, 600, 600), fill=(0, 0, 0), outline=(0, 0, 0))
draw_1.polygon(((299, 0), (599, 599), (0, 599)), outline=(255, 255, 255))
draw_1.polygon(((299, 600), (599, 0), (0, 0)), outline=(255, 255, 255))
draw_1.polygon(((0, 299), (599, 599), (599, 0)), outline=(255, 255, 255))
draw_1.polygon(((599, 299), (0, 599), (0, 0)), outline=(255, 255, 255))
draw_1.ellipse((199, 199, 399, 399), outline=(255, 255, 255))
imgbig_final.save("roundlogo.png")