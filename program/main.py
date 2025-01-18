from datetime import datetime
import random
import functions.database as database
import functions.option_one_functions as option_one_functions
import functions.option_two_functions as option_two_functions
import functions.option_three_functions as option_three_functions
import functions.option_four_functions as option_four_functions
import functions.option_five_functions as option_five_functions
import functions.titles as titles
import functions.table_headers as table_headers


#MODIFICAR
game = []
possible_decks = ["SPANISH (48 cards)","SPANISH (40 cards)","POKER"]
deck_name = "SPANISH (40 cards)"
context_game = {"game":[],"round":0}
max_rounds = 5


menu00 = "*"*136 + titles.title_main_centred + "*"*136 + "\n" + "1) Add/Remove/Show Players\n2) Settings\n3) Play Game\n4) Ranking\n5) Reports\n6) Exit\n"
menu01 = "*"*136 + titles.title_bbdd_players_centred + "*"*136 + "\n" + "1) New Human Player\n2) New Bot\n3) Show/Remove Players\n4) Go back\n"
menu02 = "*"*136 + titles.title_settings_centred + "*"*136 + "\n" + "1) Set Game Players\n2) Set Card's Deck\n3) Set Max Rounds (Default 5 Rounds)\n4) Go back\n"
menu022 = "*"*136 + titles.title_card_deck_centred+ "*"*136 + "\n" + "1) Spanish Deck (48 cards)\n2) Spanish Deck (40 cards)\n3) Poker Deck\n4) Go back\n"
menu04 = "*"*136 + titles.title_ranking_centred + "*"*136 + "\n" + "1) Players With More Earnings\n2) Players With More Games Played\n3) Players With More Minutes Played\n4) Go back\n"
menu05 = "*"*136 + titles.title_reports_centred + "*"*136 + "\n" + "1) Initial card more repeated by each user,\nonly users who have played a minimum of 3 games.\n2) Player who makes the highest bet per game,\nfind the round with the highest bet.\n"\
    + "3) Player who makes the lowest bet per game.\n4) Percentage of rounds won per player in each game (%),\nas well as their average bet for the game.\n5) List of games won by Bots.\n"\
    + "6) Rounds won by the bank in each game.\n7) Number of users that have been the bank in each game.\n8) Average bet per game.\n9) Average bet of the first round of each game.\n"\
    + "10) Average bet of the last round of each game.\n11) Go back"

exit = False
flg_00 = True
flg_01 = False
flg_013 = False
flg_02 = False
flg_021 = False
flg_03 = False
flg_04 = False
flg_05 = False

while not exit:
    while flg_00:
        print(menu00)
        opt = input("Option: ")
        if not opt.isdigit():
            print("\nInvalid option\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 6:
                print("\nInvalid option\n")
            elif opt == 1:
                flg_00 = False
                flg_01 = True
            elif opt == 2:
                flg_00 = False
                flg_02 = True
            elif opt == 3:
                flg_00 = False
                flg_03 = True
            elif opt == 4:
                flg_00 = False
                flg_04 = True
            elif opt == 5:
                flg_00 = False
                flg_05 = True
            else:
                flg_00 = False
                exit = True

    while flg_01:
        print(menu01)
        opt = input("Option: ")
        if not opt.isdigit():
            print("\nInvalid option\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 4:
                print("\nInvalid option\n")
            elif opt == 1:
                print("*"*136 + titles.title_new_human_centred + "*"*136 + "\n")
                newHuman = option_one_functions.newHuman()
                if not newHuman == False:
                    nif = newHuman[0]
                    name = newHuman[1]
                    profile = newHuman[2]

                    players[nif] = {"name": name, "human": True, "bank": False, "initialCard": "", "priority": 0, "type": profile, "bet": 4, "points": 0, "cards": [], "roundPoints":0}

            elif opt == 2:
                print("*"*136 + titles.title_new_bot_centred + "*" * 136 + "\n")
                newBot = option_one_functions.newBot()
                if not newBot == False:
                    nif = newBot[0]
                    name = newBot[1]
                    profile = newBot[2]

                    players[nif] = {"name": name, "human": False, "bank": False, "initialCard": "", "priority": 0,
                                    "type": profile, "bet": 4, "points": 0, "cards": [], "roundPoints": 0}

            elif opt == 3:
                flg_01 = False
                flg_013 = True

            else:
                flg_01 = False
                flg_00 = True

    while flg_013:
        print(table_headers.show_remove_header)

        option_one_functions.showPlayers(players)

        continue_flg_013 = option_one_functions.removePlayers(players)

        if not continue_flg_013:
            flg_013 = False
            flg_01 = True

    while flg_02:
        print(menu02)
        opt = input("Option: ")
        if not opt.isdigit():
            print("\nInvalid option\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 4:
                print("\nInvalid option\n")
            elif opt == 1:
                flg_02 = False
                flg_021 = True

            elif opt == 2:
                deck_number = option_two_functions.setDeck(possible_decks)
                if deck_number == 0:
                    print("The deck has not been changed. It is still {}.".format(deck_name))
                else:
                    deck_number = deck_number - 1
                    deck_name = possible_decks[deck_number]
                    print("Established deck: {}.".format(deck_name))

            elif opt == 3:
                max_rounds = option_two_functions.setMaxRounds()
                print("Established maximum of rounds to {}.".format(max_rounds))

            else:
                flg_02 = False
                flg_00 = True

    while flg_021:
        print("*" * 136 + "\n" + titles.title_set_game_players_centred + "\n" + "*" * 136)
        print(table_headers.show_players_header)
        option_two_functions.showPlayersToChoose(game,players)
        option_two_functions.showParticipants(game, players)
        continue_picking = option_two_functions.pickParticipants(game, players)

        if not continue_picking:
            flg_021 = False
            flg_02 = True

    while flg_03:
        #Cargar desde la BBDD las cartas del deck elegido en un diccionario
        deck = database.getcards(1)

        if len(game) >= 2:
            option_three_functions.playGame(players,game,deck,cards,max_rounds)
        else:
            print("You cannot play. Please, choose at least 2 players for the game.")

        flg_03 = False
        flg_00 = True

    while flg_04:
        print(menu04)
        opt = input("Option: ")
        if not opt.isdigit():
            print("\nInvalid option\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 4:
                print("\nInvalid option\n")
            elif opt == 1:
                print("1")
            elif opt == 2:
                print("2")
            elif opt == 3:
                print("3")
            else:
                flg_04 = False
                flg_00 = True

    while flg_05:
        print(menu05)
        opt = input("Option: ")
        if not opt.isdigit():
            print("\nInvalid option\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 11:
                print("\nInvalid option\n")
            elif opt == 1:
                print("1")
            elif opt == 2:
                print("2")
            elif opt == 3:
                print("3")
            elif opt == 4:
                print("4")
            elif opt == 5:
                print("5")
            elif opt == 6:
                print("6")
            elif opt == 7:
                print("7")
            elif opt == 8:
                print("8")
            elif opt == 9:
                print("9")
            elif opt == 10:
                print("10")
            else:
                flg_05 = False
                flg_00 = True

