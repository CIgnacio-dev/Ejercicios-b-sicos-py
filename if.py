import random



aleatorios = [random.randint(1,6) for _ in range(2)]
print(aleatorios)
s=sum(aleatorios)
print ('La suma de los números es', s)

ask=int(input('¿Desea lanzar el dado otra vez? Ingresa 1 para Sí o cualquier otro número para No '))
if ask==1:
        aleatorios = [random.randint(1,6) for _ in range(2)]
        print(aleatorios)
        s=sum(aleatorios)
        print ('La suma de los números es', s)
else:
    print('adiós')
        
        
   
