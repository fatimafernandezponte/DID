import random

jugadaGana=0
yoGano=0
cont=0
while(True):
    print("PIEDRA PAPEL TIJERA :)")
    print("")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("")
    jugada = input("Escoge una jugada (1/2/3): ")
    jugada = int(jugada)
    
    while(jugada<1 or jugada>3):
        jugada=input("Jugada no válida, vuelve a probar:")
        jugada= int(jugada)

    print("")
    yo = random.randint(1,3)

    if jugada==yo:
        print("Empate, no se cuenta la jugada")
    else:
        if jugada==1 and yo==2:
            print("Has sacado piedra y yo he sacado papel")
            print("Has perdido, piedra pierde contra papel")
            yoGano=yoGano+1
            cont=cont+1
        else:
            if jugada==1 and yo==3:
                print("Has sacado piedra y yo he sacado tijera")
                print("Has ganado, piedra gana a tijera")
                jugadaGana=jugadaGana+1
                cont=cont+1
            else:
                if jugada==2 and yo==1:
                    print("Has sacado papel y yo he sacado piedra")
                    print("Has ganado, papel gana a piedra")
                    jugadaGana=jugadaGana+1
                    cont=cont+1
                else:
                    if jugada==2 and yo==3:
                        print("Has sacado papel y yo he sacado tijera")
                        print("Has perdido, papel pierde contra tijera")
                        yoGano=yoGano+1
                        cont=cont+1
                    else:
                        if jugada==3 and yo==1:
                            print("Has sacado tijera y yo he sacado piedra")
                            print("Has perdido, tijera pierde contra piedra")
                            yoGano=yoGano+1
                            cont=cont+1
                        else:
                            if jugada==3 and yo==2:
                                print("Has sacado tijera y yo he sacado papel")
                                print("Has ganado, tijera gana a papel")
                                jugadaGana=jugadaGana+1
                                cont=cont+1
    print(cont)
    print("")

    if cont==5:
        if jugadaGana>yoGano:
            print("¡Has ganado!")
            print("Resultado: ")
            print("Tú: ",jugadaGana)
            print("Yo: ",yoGano)
        else:
            print("Has perdido :(")
            print("Resultado: ")
            print("Tú: ",jugadaGana)
            print("Yo: ",yoGano)
    
    if cont==5:
        break
        
