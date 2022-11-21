## estructura de datos
##listas
##metodos para estructura de dato tipo lista en python

# list=["deyanira"]#lista vacia
# list.append("diego")
# list.insert(0,"jose")
# list.insert(3,"macaco")
# list.insert(len(list),"simio")
# print(list)


# ##en lista vacia agrega del cero al 10 

# list=[]
# for i in range(21):
#      if i%2==0:
#         # list.append(i)
# print(list)

# ##metodos para estructura de dato tipo un python
# vocalesUno=["a","e"]
# vocalesDos=["i","o","u"]
# vocalesUno.extend(vocalesDos)

# vocalesUno[3]="oo"
# vocalesUno.remove("u")
# print(vocalesUno)

##escriba una funcion en python que acepte una lista y genera otra lista eliminando los duplicados numeros
def delDuplicate(array):
    newArray=[]
    for el in array:
     if el not in newArray:
        newArray.append(el)
    return newArray
arrayD=[1,1,2,5,3,3,6,5,8,6,6]
print(delDuplicate(arrayD))
##escriba una funcion que acpete una lista y genere otra con los numeros pares
def numeroPar(array):
    newArray=[]
    for r in array:
      if r%2==0:
        newArray.append(r)
    return newArray
arrayD=[2,4,7,8,9,3,6,10,12]
print(numeroPar(arrayD))


##ESCRIBA UNA FUNCION QUE ACEPTA UNA LISTA Y GENERE OTRA ELINANDO LOS DUPLICADOS DEL TEXTO
def delDuplicate(array):
    newArray=[]
    for el in array:
     if el not in newArray:
        newArray.append(el)
    return newArray
arrayD=["a","a","b","b","b","c","c","a"]
print(delDuplicate(arrayD))