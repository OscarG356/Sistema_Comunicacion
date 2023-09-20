msj = 0
mensaje = ""
while (msj == 0):
    codigo = input("Ingrese el mensaje: ")
    
    
    if (len(codigo) == 4):
        if (codigo == "pppp"):
            mensaje += "0"
        elif(codigo == "pppr"):
            mensaje += "1"
        elif(codigo == "pprp"):
            mensaje += "2"
        elif(codigo == "pprr"):
            mensaje += "3"
        elif(codigo == "prpp"):
            mensaje += "4"
        elif(codigo == "prpr"):
            mensaje += "5"
        elif(codigo == "prrp"):
            mensaje += "6"
        elif(codigo == "prrr"):
            mensaje += "7"
        elif(codigo == "rppp"):
            mensaje += "8"
        elif(codigo == "rppr"):
            mensaje += "9"
        elif(codigo == "rprp"):
            mensaje += "A"
        elif(codigo == "rprr"):
            mensaje += "B"
        elif(codigo == "rrpp"):
            mensaje += "C"
        elif(codigo == "rrpr"):
            mensaje += "D"
        elif(codigo == "rrrp"):
            mensaje += "E"
        elif(codigo == "rrrr"):
            mensaje += "F"
        else:
            print("Caracter invalido")
        
    elif (len(codigo) == 3):
        if(codigo == "ppp"):
            msj = 1
            print("El mensaje es: ", mensaje)
            print("FIN")
        elif (codigo == "prp"):
            mensaje += "X"
        else:
            print("Caracter invalido")
    
    elif (len(codigo) == 2):
        if(codigo == "rr"):
            mensaje += "n"
        else:
            print("Sa mondá no existe")
            
    else:
        print ("Valor invalido")