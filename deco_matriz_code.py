msj = 0
mensaje = "s"
while (msj == 0):
    codigo = input("Ingrese el mensaje: ")
    
    
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
        elif (codigo == "X"):
            mensaje += e
            msj = 1
            print("El mensaje es :", mensaje)
            print("FIN")
        else:
            print("Caracter invalido")
            
    else:
        print ("Valor invalido")