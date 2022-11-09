numero=int(input('numero: '))
factorial=1
if numero !=0:
    for i in range(1,numero+1):
        factorial*=i
        
print("factorial:",factorial)