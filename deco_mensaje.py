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
            print("El hexa es: ", hexa)
            print("FIN")
        elif (codigo == "prp"):
            hexa += "X"
        else:
            print("Caracter invalido")
    
    elif (len(codigo) == 2):
        if(codigo == "rr"):
            hexa += "n"
        else:
            print("Sa mondá no existe")
            
    else:
        print ("Valor invalido")