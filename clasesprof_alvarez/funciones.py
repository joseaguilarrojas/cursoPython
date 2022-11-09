#04.- siempre la funcion tiene que retornar un tipode dato
def saludo (nombre):
    respuesta=f"hola como estas {nombre}"
    return respuesta
#como uso
arrayAmigos=["ronald", "claudio", "diego", "jose", "kevin", "liliam"]
for amigo in range(0,len(arrayAmigos)):
    print(saludo(arrayAmigos[amigo]))

##TAREA
##crear una funcion que me retorme los n numeros FIBONACCI
#1 1 2 3 5 8 
##crear una funcion que me retorme el FACTORIAL de un numero N
#5=5*4*3*2*1
#CREAR UNA FUNCION QUE ME DIGA SI UNA PALABRA ES PALINDROMO
#ALA
#ADA
