mensajeOpciones="""
=========================
selecciona una opcion
 1)Suma
 2)Resta
 3)Divicion
 4)Multiplicacion
 ========================
"""
while True:
    print(mensajeOpciones)
    opcion=input("ingresa una opcion valida entre(1-5):")
    numeroUno=int(input("ingresa el primer numero: "))
    numeroDos=int(input("ingresa el segundo numero: "))
    match opcion:
        case "1":
         print (f"la suma de {numeroUno} + {numeroDos} = {numeroUno+numeroDos}")
        case "2":
         print (f"la resta de {numeroUno} - {numeroDos} = {numeroUno-numeroDos}")
        case "3":
         print (f"la divicion de {numeroUno} / {numeroDos} = {numeroUno/numeroDos}")
        case "4":
         print (f"la multiplicacion de {numeroUno} * {numeroDos} = {numeroUno*numeroDos}")
        case "5":
            break
        case __:
            print("esta opcion no existe")


