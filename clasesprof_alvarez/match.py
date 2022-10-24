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