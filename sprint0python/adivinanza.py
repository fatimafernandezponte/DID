cont = 0
print ("Cada respuesta correcta suma 10 y cada respuesta inccorecta resta 5, suerte!")
print("")
print("Primera adivinanza:")
print ("Para ser más elegante no usa guante ni chaqué solo cambia en un instante por una 'efe' la 'ge': ")
print ("a. Gato.")
print ("b. Elefante.")
print ("c. León.")
print("")

respuesta = input("Introduce tu respuesta (a/b/c): ")

if respuesta == "b": 
    print("¡Has acertado!")
    cont = cont + 10
else: 
    print ("No has acertado :(")
    cont = cont -5

print("")
print("Segunda adivinanza:")
print("No muerde ni ladra, pero tiene dientes y la casa guarda. ¿Qué es?")
print("a. Una llave")
print("b. Un perro")
print("c. Una puerta")
print("")
respuesta = input("Introduce tu respuesta (a/b/c): ")

if respuesta == "a": 
    print("¡Has acertado!")
    cont = cont + 10
else:
    print("No has acertado :(")
    cont = cont -5

print("")
print("Tercera adivinanza:")
print("¿Qué cosa es que entra en el río y o se moja?")
print("a. Los peces")
print("b. Los rayos del sol")
print("c. Las piedras")
print("")
respuesta = input("Introduce tu respuesta (a/b/c): ")

if respuesta == "b": 
    print("¡Has acertado!")
    cont = cont + 10
else: 
    print ("No has acertado :(")
    cont = cont -5

print("")
print("¡Se acabó!")
print("Tu puntuación es de: ",cont)

