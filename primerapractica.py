#Estructura de control if
tuEdad = input("Introduce tu edad: ")
tuEdad = int (tuEdad)

if tuEdad >= 18 and tuEdad <=100:
    print("Eres mayor de edad")
elif tuEdad >= 100:
    print("Eres un anciano")
elif tuEdad <= 0:
    print("No existes")
else:
    print("Eres menor de edad")

#Estructura for
for i in range(0,10):
    print(i)

