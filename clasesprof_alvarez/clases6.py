def mensaje(nombre,apellido,accion):
    if accion == "salido":
        mensaje="hola", nombre, apellido, "como estas"
    elif accion=="despedida":
            mensaje="adios", nombre,apellido
    return mensaje 
respuesta=mensaje("jose", "alvarez", "despedida")
print(respuesta)