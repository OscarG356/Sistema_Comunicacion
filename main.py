from PIL import Image

import cv2
import numpy as np
import datetime
import sys

raw_data="s0000n0731n0742e"

size = 80
images = [
    cv2.resize(cv2.imread("images/R_img3.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img1.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img2.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img5.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img6.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img7.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img8.png"), (size, size)),
    cv2.resize(cv2.imread("images/R_img4.png"), (size, size))]

def decode_string(data):
    start='s'
    end='e'
    new_line='n'
    i=0
    dimx=0 #number of columns
    dimy=0 #number of rows = new lines + 1
    sequence=[]
    drawings=0
    while(1):#drawings<2):
        c=data[i]

        if(c==start):
            i=0
            dimx=0
            dimy=0
        elif(c>='0' and c<='7'):
            sequence.append(int(c))
        elif(c==new_line):
            if (dimy==0):
                dimx=len(sequence)
            dimy+=1
        elif(c==end):
            print(f"dimx{dimx} dimy{dimy+1} sequence{sequence} len(sequence){len(sequence)}")
            draw_sequence(dimx,dimy+1,sequence,data)
            drawings+=1
            break
        i+=1



def draw_sequence(width, height, data, raw_data):
    collage = []
    for j in range(0, height):
        collage_line = []

        for i in range(j*width,(j+1)* width):
            collage_line.append(images[data[i]])

        collage.append(np.hstack(collage_line))

    out_data = np.vstack(collage)
    show_sequence(out_data,raw_data)

def show_sequence(out_data,raw_data):
    cv2.imshow("Final Collage", out_data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(f"./tests/collage_{raw_data}_{datetime.datetime.now().time()}.png",out_data)

"""
draw_sequence(8,8,[2,2,2,2,2,4,2,2,
                   2,4,5,2,2,7,4,2,
                   2,3,3,2,2,2,3,2,
                   2,7,6,2,2,2,3,2,
                   2,5,3,3,3,3,3,2,
                   2,3,1,3,0,2,3,2,
                   2,7,3,3,3,3,6,2,
                   2,2,1,2,2,1,2,2])
"""

decode_string(raw_data)


