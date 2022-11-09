def palindromo(cadena):
    izquierda = 0
    derecha = len(cadena)-1
 
    while  derecha >= izquierda:
        if not cadena[izquierda] == cadena[derecha]:
            return False

        izquierda += 1
        derecha -= 1 

    return True

print(palindromo('ana'))
print(palindromo('oso'))
print(palindromo('oro'))
print(palindromo('somos'))
print(palindromo('seres'))
print(palindromo('salas'))
print(palindromo('bola'))

