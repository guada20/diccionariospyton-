#devuelve el valor de un diccionario indicando su clave
animales={"felinos":"leon", "acuaticos":"defin","omnivoro":"gallina", "reptiles":"iguana"}
objetos = {"tecnologicos":"televisor", "escolares":"lapiz", "hogar":"nevera"}
valor = animales.get("acuaticos")
print(valor)