"""
En este archivo se presentan las funciones utilizadas para la opción 1 del menú principal del programa.

Grupo: Doble o Nada
"""

import random
import functions.database as database
import functions.titles as titles

lettersNIF = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']

# Función que permite añadir un nuevo jugador humano
def newHuman(players):
    # Se comprueba que el nombre tenga solo caracteres alfabéticos y que no sea más largo que 15 caracteres
    while True:
        name = input("Name: ")
        if not name.isalpha():
            print("\nInvalid name.")
            input("Enter to continue\n")
        elif len(name) > 15:
            print("\nThe name is too long.")
            input("Enter to continue\n")
        else:
            name = name.title()
            break
    # Se comprueba que el DNI escrito sea válido
    while True:
        nif = input("NIF: ")
        if not len(nif) == 9:
            print("\nIncorrect NIF length.")
            input("Enter to continue\n")
        elif not nif[:-1].isdigit():
            print("\nInvalid NIF")
            input("Enter to continue\n")
        else:
            if not nif[-1].upper() == lettersNIF[int(nif[:-1]) % 23]:
                print("\nIncorrect DNI letter.")
                input("Enter to continue\n")
            else:
                break
    # Se comprueba que se elija una de las tres posibles opciones
    while True:
        opt = input("Select your Profile:\n1) Cautious\n2) Moderated\n3) Bold\nOption: ")
        if not opt.isdigit():
            print("\nInvalid option.")
            input("Enter to continue\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 3:
                print("\nInvalid option.")
                input("Enter to continue\n")
            elif opt == 1:
                profile = 30
                break
            elif opt == 2:
                profile = 40
                break
            else:
                profile = 50
                break
    # Se imprime la información del nuevo jugador y se pregunta si se quiere o no guardar
    while True:
        print("*" * 136 + titles.title_new_human_centred + "*" * 136 + "\n")
        print("NIF: {}\nName: {}\nType: {}\n".format(nif,name,profile))

        save = input("Is it ok? (Y/N) ")
        if not save.isalpha():
            print("\nInvalid answer.")
            input("Enter to continue\n")
        else:
            save = save.upper()
            if save == "Y":
                playerID = database.insertPlayer(nif, name, profile, 0)
                players[nif] = {"player_id":playerID,"name": name, "human": True, "type": profile}

                print("You have inserted {}, a new human, into the database.".format(name))
                input("Enter to continue\n")
                return
            elif save == "N":
                return
            else:
                print("\nInvalid answer.")
                input("Enter to continue\n")

# Función que permite añadir un nuevo jugador bot
def newBot(players):
    # Se comprueba que el nombre tenga solo caracteres alfabéticos y que no sea más largo que 15 caracteres
    while True:
        name = input("Name: ")
        if not name.isalpha():
            print("\nInvalid name.")
            input("Enter to continue\n")
        elif len(name) > 15:
            print("\nThe name is too long.")
            input("Enter to continue\n")
        else:
            name = name.title()
            break
    # Se genera un DNI para ese bot
    nif = random.randint(10000000,99999999)
    nif = str(nif) + lettersNIF[nif%23]
    print("NIF: ",nif)
    # Se comprueba que se elija una de las tres posibles opciones
    while True:
        opt = input("Select your Profile:\n1) Cautious\n2) Moderated\n3) Bold\nOption: ")
        if not opt.isdigit():
            print("\nInvalid option.")
            input("Enter to continue\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 3:
                print("\nInvalid option.")
                input("Enter to continue\n")
            elif opt == 1:
                profile = 30
                break
            elif opt == 2:
                profile = 40
                break
            else:
                profile = 50
                break
    # Se imprime la información del nuevo jugador y se pregunta si se quiere o no guardar
    while True:
        print("*" * 136 + titles.title_new_bot_centred + "*" * 136 + "\n")
        print("NIF: {}\nName: {}\nType: {}\n".format(nif, name, profile))

        save = input("Is it ok? (Y/N) ")
        if not save.isalpha():
            print("\nInvalid answer.")
            input("Enter to continue\n")
        else:
            save = save.upper()
            if save == "Y":
                playerID = database.insertPlayer(nif, name, profile, 1)
                players[nif] = {"playerID":playerID,"name": name, "human": False, "type": profile}

                print("You have inserted {}, a new bot, into the database.".format(name))
                input("Enter to continue\n")
                return
            elif save == "N":
                return
            else:
                print("\nInvalid answer.")
                input("Enter to continue\n")

# Se imprimen todos los jugadores que hay en la BBDD en dos columnas (separando humanos y bots)
def showPlayers(players):
    data = ""
    human_list = []
    bot_list = []
    for id in players:
        if players[id]["human"]:
            human_list.append(id)
        else:
            bot_list.append(id)

    while len(human_list) != 0 or len(bot_list) != 0:
        if len(human_list) == 0:
            data += " " * 67 + "||" + " " + bot_list[0].ljust(19) + players[bot_list[0]]["name"].ljust(27) + str(
                players[bot_list[0]]["type"]).ljust(20) + "\n"
            bot_list.remove(bot_list[0])
        elif len(bot_list) == 0:
            data += human_list[0].ljust(20) + players[human_list[0]]["name"].ljust(
                27) + str(players[human_list[0]]["type"]).ljust(20) + "||" + " " * 67 + "\n"
            human_list.remove(human_list[0])
        else:
            data += human_list[0].ljust(20) + players[human_list[0]]["name"].ljust(
                27) + str(players[human_list[0]]["type"]).ljust(20) + "||" + " " + bot_list[0].ljust(19) + \
                     players[bot_list[0]]["name"].ljust(27) + str(players[bot_list[0]]["type"]).ljust(20) + "\n"
            bot_list.remove(bot_list[0])
            human_list.remove(human_list[0])
    data += "*" * 136
    print(data)

# Opción que te permite borrar jugadores
def removePlayers(players):
    opt = input("\n->Option ( -id to remove player, -1 to exit): ")
    if opt[0] != "-":
        print("\nInvalid option.")
        input("Enter to continue\n")
        return True
    else:
        opt = opt[1:]
        if opt == "1":
            return False
        else:
            exists = False
            for key in players:
                if opt == key:
                    exists = True
                    break
            if exists:
                del players[opt]

                database.deletePlayer(opt)
                return True
            else:
                print("\nInvalid option.")
                input("Enter to continue\n")
                return True
