import functions.titles as titles
import functions.table_headers as table_headers

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

def showPlayersToChoose(game,players):
    data = ""
    human_list = []
    bot_list = []
    for id in players:
        if id not in game:
            if players[id]["human"] == True:
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

def pickParticipants(game,players):
    opt = input("\n->Option (id to add to game, -id to remove from game, -1 to exit): ")

    if len(game) > 6:
        print("\nMaximum number of participants reached!\n")
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
                elif exists and opt not in game:
                    print("{} is not in the list of participants.".format(opt))
                else:
                    print("There is no player with ID: ",opt)
                return True
        else:
            exists = False
            for key in players:
                if opt == key:
                    exists = True
                    break
            if exists and opt in game:
                print("{} is already a participant.".format(opt))
            elif exists and opt not in game:
                game.append(opt)
                print("{} is now a participant.".format(opt))
            else:
                print("There is no player with ID: ", opt)
            return True

def setDeck(possible_decks):
    while True:
        text_options = ""
        print("*" * 136 + "\n" + titles.title_card_deck_centred + "\n" + "*" * 136)
        for i in range(len(possible_decks)):
            text_options += str(i+1) + ") " + possible_decks[i] + "\n"
        print(text_options)

        deck = input("Choose a deck (0 to go back): ")
        if not deck.isdigit():
            print("\nPlease, enter only numbers.\n")
        else:
            deck = int(deck)
            if deck == 0:
                return deck
            elif deck > len(possible_decks):
                print("\nInvalid option.\n")
            else:
                return deck

def setMaxRounds():
    while True:
        print("*"*136 + "\n" + titles.title_set_max_rounds_centred + "\n" + "*"*136)
        rounds = input("Max Rounds: ")
        if not rounds.isdigit():
            print("\nPlease, enter only numbers.\n")
        else:
            rounds = int(rounds)
            if rounds < 1 or rounds > 30:
                print("\nThe maximum number of rounds must be between 1 and 30, those included.\n")
            else:
                return rounds

