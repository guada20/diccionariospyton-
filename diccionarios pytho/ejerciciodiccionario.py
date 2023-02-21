#crear un programa donde vamos a declarar un diccioario para guardar lor precios de diferentes articulos.
#el programa pedira inicialmete la cantidad de frutas comprada, en un ciclo for pedirá
#el nombre de la fruta y el precio d ela fruta que se ha vendido. el programa debe mostrar el precio final
#del articulo a partir de los datos guardados en el diccionario.si la fruta no existe nos dara un erros.
#tras cada consulta el progrma nos preguntara si queremos hacer otra consulta 

productos ={}
cant = int(input("Ingresa la cantidad de frutas"))

for x in range (1,cant+1):
    nombre = input("ingrese el nombre de la fruta")
    precio =int(input("ingrese el precio de la fruta"))
    productos[nombre]=precio
print(productos)
for i in productos.keys():
    nombre =input("ingerse el nombre de la fruta")
    if nombre in productos:
        cantV = int(input("ingrese la cantidad" ))
        preciototal = cantV*productos[nombre]
        print(preciototal)
    else:
        print("su fruta no existe ERROR")





