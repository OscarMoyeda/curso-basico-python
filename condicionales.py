# Declaramos una variable
calificacion = input("Mete tu perra calificacion de la az 900: ")
calificacion = int(calificacion)
#Preguntamos la calificacion del examen
if calificacion < 700:
    print("Ves, por no estudiar che wey")
elif calificacion > 1000:
    print("No trollear")

else:
    print("A huevo, recoge tu certificado")

# Preguntamos edad
edad = input("A ver pinche morro meco, cual es tu edad? ")
edad = int(edad) # Pasamos la edad a dato entero

#Si se cumple:
if edad >= 18 and edad <= 100 :
    print("Pasele pues jovenazo, bienvenido al Mamitas Puebla")

elif edad > 100: #Si no
    print("Alv mejor ahorre para su retiro, pasele pues")

elif edad < 0:
    print("Todavia ni naces culero, vuelve a tu linea de tiempo")
else: # Si todo lo anterior no cumple, entonces esto
    print("Ja te mamaste pinche morrito, orale a su casa")