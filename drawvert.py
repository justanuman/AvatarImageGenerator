"""
from PIL import Image, ImageDraw
import random as rand
imgfin = Image.new("RGBA", (1280,512), (0,0,0,0))
imgfinale = Image.new("RGBA", (1280,1024), (0,0,0,0))
image = Image.new("RGBA", (400,400), (0,0,0,0))
draw = ImageDraw.Draw(image)
draw. rectangle((0,0,400,400), fill="black")
x1 = rand.randint(0,400)
y1 = rand.randint(0,400)
x2 = rand.randint(0,400)
y2 = rand.randint(0,400)
stx = x2
sty = y2
draw. line((x1,y1,x2,y2), fill="white")
for i in range(rand.randint(20,70)):
	enx = rand.randint(0,400)
	eny = rand.randint(0,400)
	if eny>300:
		eny=400
	if enx>300:
		enx=400
	draw.line((stx,sty,enx,eny),fill="white")
	stx = enx
	sty=eny
del draw
image.save("test.png", "PNG")
trans = image.transpose(Image.FLIP_LEFT_RIGHT)
trans.save("trans.png")
img2 = Image.open("trans.png")  
imgfin.paste(img2, (400,0))
imgfin.paste(image, (0,0))
image.save("fin.png") 
imgfin.rotate(180).save("rotated.png")
ban = Image.open('rotated.png')
imgfinale.paste(imgfin,(0,0))
imgfinale.paste(ban,(0,400))
imgfin.save("final.png")
imgfinale.save("finale.png")
"""
from PIL import Image, ImageDraw
import random as rand
wid=400
hie=400
wid_hf=int(wid*0.5)
hie_hf=int(hie*0.5)
imgfin = Image.new("RGBA",(wid,hie_hf),(0,0,0,0))
imgfinale = Image.new("RGBA",(wid,hie),(0,0,0,0))
image = Image.new("RGBA",(wid_hf,hie_hf),(0,0,0,0))
draw = ImageDraw.Draw(image)
draw. rectangle((0,0,wid,wid), fill="black")
x1 = rand.randint(0,wid_hf)
y1 = rand.randint(0,wid_hf)
x2 = rand.randint(0,hie_hf)
y2 = rand.randint(0,hie_hf)
stx = x2
sty = y2
draw. line((x1,y1,x2,y2), fill="white")
for i in range(rand.randint(10,40)):
	enx = rand.randint(0,wid_hf)
	eny = rand.randint(0,hie_hf)
	if eny>hie_hf*0.75:
		eny=hie_hf
	if enx>hie_hf*0.75:
		enx=wid_hf
	draw.line((stx,sty,enx,eny),fill="white",width=3)
	stx = enx
	sty=eny
del draw
image.save("test.png", "PNG")
trans = image.transpose(Image.FLIP_LEFT_RIGHT)
trans.save("trans.png")
img2 = Image.open("trans.png")  
imgfin.paste(img2, (wid_hf,0))
imgfin.paste(image, (0,0))
image.save("fin.png") 
imgfin.rotate(180).save("rotated.png")
ban = Image.open('rotated.png')
imgfinale.paste(imgfin,(0,0))
imgfinale.paste(ban,(0,hie_hf))
imgfin.save("final.png")
imgfinale.save("finale.png")
