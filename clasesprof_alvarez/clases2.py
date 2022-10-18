##tendremos una variable con el mensaje hola mundo
## pedir al usuario un texto
## si el texto ingresado es hola
## mostraras el mensaje completo
## si el texto ingresado es como estas
## estraeras del mensaje la palabra hola
## si el texto ingresado es saludos
## estraeras del mensaje la palabra mundo
## si se ingresa otro texto
## mostraras por defecto el mensaje de error 
mensaje=" hola mundo"
texto=input("ingresa un texto:")
match  texto:
    case "hola":
        print(mensaje[:])
    case "como estas":
        print(mensaje[:5])
    case "saludos":
        print(mensaje[5:1])
    case _:
        print("error")