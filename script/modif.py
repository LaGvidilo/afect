from PIL import Image 
from statistics import *
import random
#f=open("motif_out.csv","w")
im = Image.open("im.jpg") # open colour image
#f.write("x0,x1,y\n")
xs,ys = im.size
for qual in range(2,256):
	im = Image.open("im.jpg") # open colour image
	xs,ys = im.size
	for x in range(0,xs):
		for y in range(0,ys):
			a,b,c = im.getpixel((x,y))
			#a,b,c = sorted([a,b,c])
			#a,b,c = int(mean([a,b,c])),int(mean([a,b,c])),int(mean([a,b,c]))
			a = min((a+random.randint(1,qual)),255)
			b = min((b+random.randint(1,qual)),255)
			c = min((c+random.randint(1,qual)),255)
			im.putpixel((x,y),(a,b,c))
		print((x/xs*1.0)*100.0)

	im.save("truc_"+str(qual)+".png")