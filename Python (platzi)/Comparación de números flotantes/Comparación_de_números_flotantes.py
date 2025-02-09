x=3.3
print(x)
y=1.1+2.2
print(y)
print( x==y )           #Precisión diferente
print("")



#          Transformación y eliminacion de 0.0000


#Manera 1    (Programación) 
print("Manera 1: Programación")
y_str= format(y,".2g")
print(y_str)
print(y_str==str(x))
print("")



# Manera 2   (Matemática)
print("Manera 2: Matemática")
print("")
print(y,x)
tolerance=0.00001
print(abs(x-y)<tolerance)
print(False==True)