#aqui en main ejecutara mis funciones

from funcions import operaciones,saludo

#import funciones as op
respuesta=operaciones(10,8,"suma")
respuesta2=operaciones(100,20,"resta")
respuesta3=operaciones(10,2,"por")
print(f"la suma es: {respuesta}")
print(f"la resta es: {respuesta2}")
print(f"la multiplicaciones es: {respuesta3}")

print(saludo())

