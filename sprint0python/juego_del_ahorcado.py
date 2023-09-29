import random

errores=0
palabra=""
palabra2=""
siLetra=False
letrasUsadas=[]
modo=0
longitud=0
cont=0
ganar=False


palabras_facil = ['ala','avion','sol','cara','perro','gato','calvo','pota','abeto','bizco','cabra']


palabras_normal = ['alerta','brillo','butaca','bufones','caballo','cabeza','guarida','castillo','chorizo','escudero']

palabras_dificil = ['coagulacion','paracaidas','esternocleidomastoideo','abdominales','radiactiva','refugiados','escalofrio','estallidos','festivales','estaciones']

while(modo!='1' and modo!='2' and modo!='3'):
    print("")
    print("AHORCADO")
    print("========")
    print("")
    print("")
    print("1. Modo Fácil")
    print("2. Modo Normal")
    print("3. Modo Difícil")
    print("")
    modo = input("Elige el modo de juego(1/2/3): ")



print("")
print("¡Empieza el juego!")
print("Si adivinas la palabra ganas, tienes un margen de 6 errores")
print("")


if modo=='1':
    palabra=random.sample(palabras_facil,k=1)
    modoO='Fácil'
else:
    if modo=='2':
        palabra = random.sample(palabras_normal,k=1)
        modoO='Normal'
    else:
        if modo=='3':
            palabra=random.sample(palabras_dificil,k=1)
            modoO='Difícil'


longitud=len(palabra[0])


palabra2=palabra[0]

i=0
almacen=[]

for i in range(len(palabra2)):
    almacen.append('_')


while(errores<6):
    cont=0
    siLetra=False
    print("")
    print("Modo: ",modoO)
    print("Errores: ",errores)
    print("Letras usadas: ",letrasUsadas)
    print("")
    print("")

    for i in range(len(palabra2)):
        print(almacen[i], end=" ")

    print("")
    print("")
    letra=input("Introduce una letra: ")
    letrasUsadas.append(letra)
    print("")

    for i in range(len(palabra2)):
        if almacen[i]=='_' and letra==palabra2[i:i+1:1]:
            almacen[i]=letra
            siLetra=True
        
               

    if siLetra==False:
        errores=errores+1
    
    for i in range(len(palabra2)):
        if almacen[i]=='_':
            cont=cont+1
    
    if cont==0:
        break
    
    


print("")
print("")
if errores==6:
    print("Has perdido :(")
    print("La palabra era: "+palabra2)
else:
    print("¡Has ganado! :)")


    