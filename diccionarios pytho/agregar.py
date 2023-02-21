#agragar elementos de una tabla a otra
animales={"felinos":"leon", "acuaticos":"defin","omnivoro":"gallina", "reptiles":"iguana"}
objetos = {"tecnologicos":"televisor", "escolares":"lapiz", "hogar":"nevera"}
animales.update(objetos)
print(animales)