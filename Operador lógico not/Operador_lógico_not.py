print( not True)
print (not False)

print("True and True: ",  not (True and True))
print("True and False: ", not (True and False))
print("False and True: ", not (False and True))
print("False and False: ",not (False and True))

stock= input("Ingrese el numero de stock:  ")
stock= int(stock)

print (not (stock >= 100 and stock <= 1000))
