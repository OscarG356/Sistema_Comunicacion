msj = 0
while (msj == 0):
    codigo = input("Ingrese el mensaje: ")
    
    
    if (len(codigo) == 1):
        if (codigo == "0"):
            print("pppp")
        elif(codigo == "1"):
            print("pppr")
        elif(codigo == "2"):
            print("pprp")
        elif(codigo == "3"):
            print("pprr")
        elif(codigo == "4"):
            print("prpp")
        elif(codigo == "5"):
            print("prpr")
        elif(codigo == "6"):
            print("prrp")
        elif(codigo == "7"):
            print("prrr")
        elif(codigo == "8"):
            print("rppp")
        elif(codigo == "9"):
            print("rppr")
        elif(codigo == "A"):
            print("rprp")
        elif(codigo == "B"):
            print("rprr")
        elif(codigo == "C"):
            print("rrpp")
        elif(codigo == "D"):
            print("rrpr")
        elif(codigo == "E"):
            print("rrrp")
        elif(codigo == "F"):
            print("rrrr")
        elif(codigo == "X"):
            msj = 1
            print("FIN")
        else:
            print("Caracter invalido")
            
    else:
        print ("Valor invalido")