mi_lista = ["python", 53, False,43,"Hola mundo","python","python","python","python"]
print(type(mi_lista))
print(mi_lista)

mi_lista.append("55") #Solamente toma 1 solo valor
print(mi_lista)

mi_lista.insert(3,"subs")
print(mi_lista)

mi_lista.remove("Hola mundo")
print(mi_lista)

mi_lista.pop(2)
print(mi_lista)

print(mi_lista.count("python"))

mi_lista.reverse()
print(mi_lista)

mi_lista.clear()
print(mi_lista)