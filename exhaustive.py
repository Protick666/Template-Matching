import numpy
import math
from PIL import Image

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def ck(x,y):
    i=x;
    j=y;
    sum=0.0

    for a in range (0,gm.size[0]):
        for b in range (0,gm.size[1]):
            #0.2989, 0.5870, 0.1140.
            p=rr[a][b]
            q=tt[i][j]
            sum=sum+(p-q)*(p-q)
            j=j+1

        i=i+1
        j=y
    return sum








im = Image.open('test.jpg') # Can be many different formats.
test = im.load()

gm = Image.open('ref.jpg') # Can be many different formats.
ref = gm.load()
#print (im.size[0] )
#print pix[x,y]
ans_pixel=numpy.zeros(3, dtype=int)
ans_val=-1
tt=numpy.ones((im.size[0],im.size[1]))
rr=numpy.ones((gm.size[0],gm.size[1]))

for i in range(0,im.size[0]):
    for j in range(0, im.size[1]):
        tt[i][j]=.2989*test[i,j][0]+.5870*test[i,j][1]+.1140*test[i,j][2]

for i in range(0,gm.size[0]):
    for j in range(0, gm.size[1]):
        rr[i][j]=.2989*ref[i, j][0]+.5870*ref[i,j][1]+.1140*ref[i,j][2]

for i in range (0,im.size[0]-(gm.size[0]-1)):
    for j in range (0,im.size[1]-(gm.size[1]-1)):
        temp=ck(i , j)
        #print(i,j)
        if ans_val==-1:
            ans_val=temp
            ans_pixel[0]=i;
            ans_pixel[1]=j;
        elif ans_val>temp:
            ans_val = temp
            ans_pixel[0] = i;
            ans_pixel[1] = j;


im = numpy.array(Image.open('test.png'), dtype=numpy.uint8)
fig,ax = plt.subplots(1)
ax.imshow(im)
rect = patches.Rectangle((ans_pixel[0],ans_pixel[1]),gm.size[0],gm.size[1],linewidth=1,edgecolor='r',facecolor='none')

ax.add_patch(rect)

plt.show()

print(ans_pixel)







