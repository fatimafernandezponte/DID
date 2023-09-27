
from operaciones import suma, resta, multiplicacion, division
while(True):
    print("")
    print("CALCULADORA")
    print("")

    num1 = input ("Introduce el primer número: ")
    num1=int(num1)
    num2 = input ("Introduce el segundo número: ")
    num2=int(num2)

    print("")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("")

    opcion = input("Elige la operación a realizar (1/2/3/4): ")
    while(opcion!='1' and opcion!='2' and opcion!='3' and opcion!='4'):
        opcion = input("Opción no válida, vuelve a probar(1/2/3/4): ")

    if opcion == "1":
        print("Resultado: ", suma(num1,num2))
    else:
        if opcion == "2":
         print("Resultado: ",resta(num1,num2))
        else:
            if opcion == "3":
                print("Resultado: ",multiplicacion(num1,num2))
            else:
                if opcion == "4":
                    print("Resultado: ",division(num1,num2))
                

    
    otro = input("¿Desea realizar otra operación (s/n): ")
    while(otro!='s' and otro!='n'):
        otro = input("Tu respuesta debe ser 'n' o 's': ")

    if otro=='n':
        break






            



