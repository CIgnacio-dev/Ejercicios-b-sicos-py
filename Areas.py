print("""
    1) Area de un circulo       2) Area de un rectangulo
    3) Area de un triangulo
    """)


eligio=input("Selecciona un numero de la figura a calcular el area : ")

if eligio=="1":
    radio=float(input("Ingrese el radio del circulo: "))
    a=(radio**2)*3.14
    print("El area del circulo es: ",a)
elif eligio=="2":
    altura=float(input("Ingrese la altura del rectangulo: "))
    base=float(input("Ingrese la base del rectangulo: "))
    a=altura*base
    print("El area del rectangulo es: ",a)
elif eligio=="3":
    altura=float(input("Ingrese la altura del triangulo: "))
    base=float(input("Ingrese la base del triangulo: "))
    a=(base*altura)/2
    print("El area del triangulo es: ",a)
else:
    print("Opción no válida")
    
