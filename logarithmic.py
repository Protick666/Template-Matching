import numpy
import math
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time


ans_val=-1

def ck(x,y):
    i = x
    j = y
    sum = 0.0
    global ans_val


    for a in range (0,gm.size[0]):
        for b in range (0,gm.size[1]):

            p=rr[a][b]
            q=tt[i][j]
            sum = sum + (p-q)*(p-q)
            j = j+1

        i=i+1
        j=y
    if ans_val == -1:

        ans_val = sum
        ans_pixel[0] = x;
        ans_pixel[1] = y;
    elif ans_val > sum:
        ans_val = sum
        ans_pixel[0] = x;
        ans_pixel[1] = y;
    return sum








im = Image.open('test.jpg') # Can be many different formats.
test = im.load()

gm = Image.open('ref.jpg') # Can be many different formats.
ref = gm.load()

ans_pixel=numpy.zeros(3, dtype=int)

tt=numpy.ones((im.size[0],im.size[1]))
rr=numpy.ones((gm.size[0],gm.size[1]))

for i in range(0,im.size[0]):
    for j in range(0, im.size[1]):
        tt[i][j]=.2989*test[i,j][0]+.5870*test[i,j][1]+.1140*test[i,j][2]

for i in range(0,gm.size[0]):
    for j in range(0, gm.size[1]):
        rr[i][j]=.2989*ref[i, j][0]+.5870*ref[i,j][1]+.1140*ref[i,j][2]

x1 = int(im.size[0]/2)
y1 = int(im.size[1]/2)
p1 = im.size[0] - x1
p2 = im.size[1] - y1
dis = min(p1, p2)
div=2

t_pixel = numpy.zeros(3, dtype=int)
t_ans=-1

while True:
    p = (dis+div-1)//div
    temp = ck(x1, y1)
    t_ans = -1
    #print("now")
    print(x1,y1)
    for i in range(-1 , 2):
        for j in range(-1 , 2):
            if i == 0 and j == 0:
                continue


            if x1 + i * p >= im.size[0] - (gm.size[0] - 1):
                continue
            if y1+j*p >= im.size[1]-(gm.size[1]-1):
                continue

            print(x1 + i * p, y1+j*p)
            tmp=ck(x1+i*p, y1+j*p)
            print(tmp)
            if t_ans == -1:
                t_ans = tmp
                t_pixel[0] = x1+i*p
                t_pixel[1] = y1+j*p
            elif tmp < t_ans:
                t_ans = tmp
                t_pixel[0] = x1 + i*p
                t_pixel[1] = y1 + j*p

    x1 =  t_pixel[0]
    y1 = t_pixel[1]
    div=div * 2
    if p == 1:
        break


im = numpy.array(Image.open('test.jpg'), dtype=numpy.uint8)
fig,ax = plt.subplots(1)
ax.imshow(im)
rect = patches.Rectangle((ans_pixel[0],ans_pixel[1]),gm.size[0],gm.size[1],linewidth=1,edgecolor='r',facecolor='none')

ax.add_patch(rect)

plt.show()
print(ans_pixel)


