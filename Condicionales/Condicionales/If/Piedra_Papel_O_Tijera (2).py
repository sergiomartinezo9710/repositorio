user_option = input("Piedra,papel o tijera:  ")
computer_option="papel"

if user_option == computer_option:
    print("Empate")

elif user_option == "piedra":
    if computer_option == "tijera":
        print("Piedra gana a tijera ")
        print("Tu ganas :D ! ")
    else:
        print("Papel gana a piedra")
        print("La computadora gana !")
        print("Tu pierdes :( ")

elif user_option == "papel":
    if computer_option == "piedra":
        print("papel gana a piedra")
        print("tu ganas :D !")

    else:
        print("tijera gana a papel ")
        print("Computadora gana !")
        print("tu pierdes :( ")

elif user_option == "tijera":
    if computer_option == "papel":
        print("Tijera gana a papel !!")
        print("tu ganas :D !")

    else:
        print("Piedra gana a tijera ")
        print("Computadora ganó ")
        print("tu pierdes :( ")
