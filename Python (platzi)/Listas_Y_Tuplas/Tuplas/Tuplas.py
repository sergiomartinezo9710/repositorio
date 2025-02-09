mi_tupla= (53,53,"perro",7.4,True)
print(type(mi_tupla))
print(mi_tupla[1])  #Es posicion 2 
print(mi_tupla.count(53))
print(mi_tupla.index(7.4))


mi_tupla = list(mi_tupla)
print(type(mi_tupla))

mi_tupla.pop()
print(mi_tupla)

mi_tupla = tuple(mi_tupla)
print(type(mi_tupla))
print(mi_tupla)