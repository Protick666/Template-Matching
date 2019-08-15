
import numpy
import math
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time


def make_array(im, gm, tt, rr):
    for i in range(0, im.size[0]):
        for j in range(0, im.size[1]):
            tt[i][j] = .2989 * test[i, j][0] + .5870 * test[i, j][1] + .1140 * test[i, j][2]

    for i in range(0, gm.size[0]):
        for j in range(0, gm.size[1]):
            rr[i][j] = .2989 * ref[i, j][0] + .5870 * ref[i, j][1] + .1140 * ref[i, j][2]

    return


def ck(x, y, tst, rf):
    i=x
    j=y
    sum=0.0

    for a in range (0,rf.shape[0]):
        for b in range (0,rf.shape[1]):
            #0.2989, 0.5870, 0.1140.
            p = rf[a][b]
            q = tst[i][j]
            sum = sum+(p-q)*(p-q)
            j=j+1

        i = i+1
        j = y
    return sum


def exh(tst,rf):
    # print(sub_sample.shape[0])
    # print(sub_sample[300,0])
    global pos
    ans_val....................................................=-1


    for i in range(0, tst.shape[0] - (rf.shape[0] - 1)):
        for j in range(0, tst.shape[1] - (rf.shape[1] - 1)):
            temp = ck(i,j,tst,rf)
            # print(i,j)
            if ans_val == -1:
                ans_val = temp
                pos=(i,j)
            elif ans_val > temp:
                ans_val = temp
                pos = (i, j)









im = Image.open('test.jpg') # Can be many different formats.
test = im.load()

gm = Image.open('ref.jpg') # Can be many different formats.
ref = gm.load()

ans_pixel=numpy.zeros(3, dtype=int)

tt=numpy.ones((im.size[0],im.size[1]))
rr=numpy.ones((gm.size[0],gm.size[1]))

make_array(im,gm,tt,rr)
depth=3
div=1
pic=[]
pic_ref=[]

for i in range(1,depth+1):
    lpf = cv2.GaussianBlur(tt, (5, 5), 0)
    sub_sample = cv2.resize(lpf, (0, 0), fx=1/div, fy=1/div)
    pic.append(sub_sample)
    lpf = cv2.GaussianBlur(rr, (5, 5), 0)
    sub_sample = cv2.resize(lpf, (0, 0), fx=1 / div, fy=1 / div)
    pic_ref.append(sub_sample)
    div=div*2


pos = (0 , 0)

for i in range(depth,0,-1):
    tst_pic=pic[i-1]
    rf_pic = pic_ref[i - 1]
    if i == depth:
        exh(tst_pic,rf_pic)
    else:
        x1 = pos[0]
        y1 = pos[1]
        x1 = x1*2
        y1 = y1*2
        rel_val = -1
        temp_pos = (0, 0)
        dir = [(-1, -1), (-1, 1), (-1, 0), (1, -1), (1, 1), (1, 0), (0, -1), (0, 1), (0, 0)]

        for t in range(0, 9):
            dx = dir[t][0]
            dy = dir[t][1]
            x = x1+dx
            y = y1+dy

            #for i in range(0, tst.shape[0] - (rf.shape[0] - 1)):
            #for j in range(0, tst.shape[1] - (rf.shape[1] - 1)):

            if x >= (tst_pic.shape[0] - (rf_pic.shape[0] - 1)):
                continue
            if y >= (tst_pic.shape[1] - (rf_pic.shape[1] - 1)):
                continue

            temp_sum=ck(x, y, tst_pic, rf_pic)

            if rel_val == -1:
                rel_val = temp_sum
                pos = (x, y)
            elif temp_sum < rel_val:
                rel_val = temp_sum
                pos = (x, y)














im = numpy.array(Image.open('test.jpg'), dtype=numpy.uint8)
fig,ax = plt.subplots(1)
ax.imshow(im)
rect = patches.Rectangle((pos[0],pos[1]),gm.size[0],gm.size[1],linewidth=1,edgecolor='r',facecolor='none')

ax.add_patch(rect)

plt.show()
print(ans_pixel)


