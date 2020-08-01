cuadernos=int(input("Ingrese la cantidad de libros que va a comprar: "))
if cuadernos < 12:
    print ("Ningun obsequio")
elif cuadernos >=12 and cuadernos <24:
    lucas= int(cuadernos / 4)
    print("Obsequio: ",lucas," lapiceros Lucas de regalo")
elif cuadernos >=24 and cuadernos <36:
    cross=int(cuadernos/4)*2
    print("Obsequio: ",cross," lapiceros Cross de regalo")
elif cuadernos >=36:
    novo=int(cuadernos/4)*3
    lucas=int(cuadernos/4)
    cross=int(cuadernos/4)
    print("Obsequio: ",novo," lapiceros Novo mas ",lucas,", Lucas mas ",cross," Cross")
