#mostrar solamente las claves de un diccionario 
animales={"felinos":"leon", "acuaticos":"defin","omnivoro":"gallina", "reptiles":"iguana"}
objetos = {"tecnologicos":"televisor", "escolares":"lapiz", "hogar":"nevera"}
for clave in animales.keys():
    print(clave)


#values se usa paar ver los elementos de un diccionario 
for clave in animales.values():
    print(clave)

#mostrar las claves y los valores
for clave,valor in animales.items():
    print(clave + " = "+ valor)