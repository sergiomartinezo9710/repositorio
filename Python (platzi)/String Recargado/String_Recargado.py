text = "Ella sabe programar en python"
"""

print("Javascript" in text)
print("python" in text)

if "python" in text:
    print("Elegiste bien !")

else:
    print("Tambien elegiste bien !")

"""
size = len(text) 
print(size)

print(text)
print(text.upper())                     #Todo en mayúsculas
print(text.lower())                     #Todo en minúsculas
print(text.count("a"))                  #Cuenta el número de letras (en éste caso las "a")
print(text.swapcase())                  #Intercambia las mayúsculas por minúsculas y visceversa
print(text.startswith("Ella"))          #
print(text.endswith("Rust"))            #
print(text.replace("python","mondá"))   #

text_2 ="este es un título"
print(text_2)
print(text_2.capitalize())
print(text_2.title())