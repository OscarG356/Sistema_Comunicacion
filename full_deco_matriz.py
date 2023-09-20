from PIL import Image

import cv2
import numpy as np
import datetime
import sys

msj = 0
hexa = ""
while (msj == 0):
    codigo = input("Ingrese el hexa: ")
    
    
    if (len(codigo) == 4):
        if (codigo == "pppp"):
            hexa += "0"
        elif(codigo == "pppr"):
            hexa += "1"
        elif(codigo == "pprp"):
            hexa += "2"
        elif(codigo == "pprr"):
            hexa += "3"
        elif(codigo == "prpp"):
            hexa += "4"
        elif(codigo == "prpr"):
            hexa += "5"
        elif(codigo == "prrp"):
            hexa += "6"
        elif(codigo == "prrr"):
            hexa += "7"
        elif(codigo == "rppp"):
            hexa += "8"
        elif(codigo == "rppr"):
            hexa += "9"
        elif(codigo == "rprp"):
            hexa += "A"
        elif(codigo == "rprr"):
            hexa += "B"
        elif(codigo == "rrpp"):
            hexa += "C"
        elif(codigo == "rrpr"):
            hexa += "D"
        elif(codigo == "rrrp"):
            hexa += "E"
        elif(codigo == "rrrr"):
            hexa += "F"
        else:
            print("Caracter invalido")
        
    elif (len(codigo) == 3):
        if(codigo == "ppp"):
            msj = 1
            print("FIN")
        elif (codigo == "prp"):
            hexa = hexa.rstrip(hexa[-1])
        else:
            print("Caracter invalido")
            
    else:
        print ("Valor invalido")

mensaje = "s"
while (msj == 1):
    codigo = input("Ingrese la matriz: ")
    
    
    if (len(codigo) == 3):
        if (codigo == "ppp"):
            mensaje += "0"
        elif(codigo == "ppr"):
            mensaje += "1"
        elif(codigo == "prp"):
            mensaje += "2"
        elif(codigo == "prr"):
            mensaje += "3"
        elif(codigo == "rpp"):
            mensaje += "4"
        elif(codigo == "rpr"):
            mensaje += "5"
        elif(codigo == "rrp"):
            mensaje += "6"
        elif(codigo == "rrr"):
            mensaje += "7"
        else:
            print("Caracter invalido")
        
    elif (len(codigo) == 2):
        if(codigo == "rr"):
            mensaje += "n"
        elif (codigo == "xx"):
            mensaje += "e"
            msj = 3
            print("El mensaje es :", mensaje)
            print("FIN")
        else:
            print("Caracter invalido")
            
    else:
        print ("Valor invalido")

#mensaje="s0000n0731n0742e"

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



def draw_sequence(width, height, data, mensaje):
    collage = []
    for j in range(0, height):
        collage_line = []

        for i in range(j*width,(j+1)* width):
            collage_line.append(images[data[i]])

        collage.append(np.hstack(collage_line))

    out_data = np.vstack(collage)
    show_sequence(out_data,mensaje)

def show_sequence(out_data,mensaje):
    cv2.imshow("Final Collage", out_data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(f"./tests/collage_{mensaje}_{datetime.datetime.now().time()}.png",out_data)

print("El hexa es: ", hexa)
decode_string(mensaje)