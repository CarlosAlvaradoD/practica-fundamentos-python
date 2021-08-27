#Generar un número aleatorio
import random

#Instalar librerias:
# python -m pip install -U pip
# python -m pip install -U 
import matplotlib.pyplot as plt
print(random.randint(1,20))

#Reacomodar una lista al azar
Lista = [1,2,3,4,5,6,7,8,9,10]
print("Lista original: ", Lista)

#Mezcla los elementos de la lista al azar
random.shuffle(Lista)
print("Lista mixeada: ", Lista)

#Generar    una gráfica tipo gauss
Campana = [random.gauss(1,0,5) for i in range (1000)]
#Arma la gráfica
plt.hist(Campana, bins=15)
#Muestra la gráfica
plt.show()