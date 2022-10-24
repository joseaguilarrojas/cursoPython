# oracion=input("ingrese su oracion:")
# vocales=["a","e","i","o","u"]
# contadorVocales=0
# for letras in oracion:
#     if letras in vocales:
#         contadorVocales+=1
#         print("la contidad de vocales es:",
#         contadorVocales)


sentence=input("ingrese un numero:")
counvocals=0
for words in sentence:
    match words:
        case "a":
            counvocals+=1
        case "e":
            counvocals+=1            
        case "i":
            counvocals+=1
        case "o":
            counvocals+=1
        case"u":
            counvocals+=1      
print("la cantidad de vocaleses:", counvocals)      


# sentence:input("ingrese una oracion:")
# def countVocals(texto):
#     vocales=["a","e","i","o","u"]
#     contadorVocales=0
#     for letras in texto:
#         if letras in vocales:
#             contadorVocales+=1
#             return contadorVocales
# print("la cantidad de vocales es:",countVocals("sentence"))