"""
En este archivo se presentan las funciones utilizadas para la opción 2 del menú principal del programa.

Grupo: Doble o Nada
"""

import functions.titles as titles
import functions.table_headers as table_headers

# Se muestran los participantes (los jugadores ya seleccionados para jugar)
def showParticipants(game,players):
    print(table_headers.participants_header)

    data = ""
    if len(game) == 0:
        data += "There are no participants for now.".center(60)
    else:
        for id in game:
            data += id.ljust(15) + players[id]["name"].ljust(15) + str(players[id]["human"]).ljust(15)

            if players[id]["type"] == 30:
                profile = "Cautious"
            elif players[id]["type"] == 40:
                profile = "Moderated"
            else:
                profile = "Bold"
            data += profile.ljust(15) + "\n"

    print(data)

# Se muestran los jugadores entre los que puedes elegir los participantes
def showPlayersToChoose(game,players):
    data = ""
    human_list = []
    bot_list = []
    for id in players:
        if id not in game:
            if players[id]["human"]:
                human_list.append(id)
            else:
                bot_list.append(id)

    while len(human_list) != 0 or len(bot_list) != 0:
        if len(human_list) == 0:
            data += " " * 66 + "||" + " " + bot_list[0].ljust(19) + players[bot_list[0]]["name"].ljust(27) + str(
                players[bot_list[0]]["type"]).ljust(20) + "\n"
            bot_list.remove(bot_list[0])
        elif len(bot_list) == 0:
            data += human_list[0].ljust(19) + players[human_list[0]]["name"].ljust(
                27) + str(players[human_list[0]]["type"]).ljust(20) + "||" + " " * 67 + "\n"
            human_list.remove(human_list[0])
        else:
            data += human_list[0].ljust(19) + players[human_list[0]]["name"].ljust(
                27) + str(players[human_list[0]]["type"]).ljust(20) + "||" + " " + bot_list[0].ljust(19) + \
                    players[bot_list[0]]["name"].ljust(27) + str(players[bot_list[0]]["type"]).ljust(20) + "\n"
            bot_list.remove(bot_list[0])
            human_list.remove(human_list[0])
    data += "*" * 136
    print(data)

# Opción que te permite elegir los participantes o quitarlos
def pickParticipants(game,players):
    opt = input("\n->Option (id to add to game, -id to remove from game, -1 to exit): ")

    if len(game) > 6:
        print("\nMaximum number of participants reached!")
        input("Enter to continue\n")
        return False
    else:
        if opt[0] == "-":
            opt = opt[1:]
            if opt == "1":
                return False
            else:
                exists = False
                for key in players:
                    if opt == key:
                        exists = True
                        break
                if exists and opt in game:
                    game.remove(opt)
                    print("{} is no longer a participant.".format(opt))
                    input("Enter to continue\n")
                elif exists and opt not in game:
                    print("{} is not in the list of participants.".format(opt))
                    input("Enter to continue\n")
                else:
                    print("There is no player with ID: ",opt)
                    input("Enter to continue\n")
                return True
        else:
            exists = False
            for key in players:
                if opt == key:
                    exists = True
                    break
            if exists and opt in game:
                print("{} is already a participant.".format(opt))
                input("Enter to continue\n")
            elif exists and opt not in game:
                game.append(opt)
                print("{} is now a participant.".format(opt))
                input("Enter to continue\n")
            else:
                print("There is no player with ID: ", opt)
                input("Enter to continue\n")
            return True

# Permite determinar la baraja con la que se va a jugar
def setDeck(possible_decks):
    while True:
        text_options = ""
        print("*" * 136 + "\n" + titles.title_card_deck_centred + "\n" + "*" * 136)
        for i in range(len(possible_decks)):
            text_options += str(i+1) + ") " + possible_decks[i] + "\n"
        print(text_options)

        deck = input("Choose a deck (0 to go back): ")
        if not deck.isdigit():
            print("\nPlease, enter only numbers.")
            input("Enter to continue\n")
        else:
            deck = int(deck)
            if deck == 0:
                return deck
            elif deck > len(possible_decks):
                print("\nInvalid option.")
                input("Enter to continue\n")
            else:
                return deck

# Permite establecer el número máximo de rondas
def setMaxRounds():
    while True:
        print("*"*136 + "\n" + titles.title_set_max_rounds_centred + "\n" + "*"*136)
        rounds = input("Max Rounds: ")
        if not rounds.isdigit():
            print("\nPlease, enter only numbers.")
            input("Enter to continue\n")
        else:
            rounds = int(rounds)
            if rounds < 1 or rounds > 30:
                print("\nThe maximum number of rounds must be between 1 and 30, those included.")
                input("Enter to continue\n")
            else:
                return rounds

