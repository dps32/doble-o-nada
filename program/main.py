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

players = database.getPlayers()


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
menu05 = "*"*136 + titles.title_reports_centred + "*"*136 + "\n" + "1) Initial card more repeated by each user, only users who have played a minimum of 3 games.\n2) Player who makes the highest bet per game.\n"\
    + "3) Player who makes the lowest bet per game.\n4) Number of users that have been the bank in each game.\n5) Average bet per game.\n6) Average bet of the first round of each game.\n"\
    + "7) Average bet of the last round of each game.\n8) Go back"

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
            print("\nInvalid option")
            input("Enter to continue\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 6:
                print("\nInvalid option")
                input("Enter to continue\n")
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
            print("\nInvalid option")
            input("Enter to continue\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 4:
                print("\nInvalid option")
                input("Enter to continue\n")
            elif opt == 1:
                print("*"*136 + titles.title_new_human_centred + "*"*136 + "\n")
                newHuman = option_one_functions.newHuman(players)

            elif opt == 2:
                print("*"*136 + titles.title_new_bot_centred + "*" * 136 + "\n")
                newBot = option_one_functions.newBot(players)

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
            print("\nInvalid option")
            input("Enter to continue\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 4:
                print("\nInvalid option")
                input("Enter to continue\n")
            elif opt == 1:
                flg_02 = False
                flg_021 = True

            elif opt == 2:
                deck_number = option_two_functions.setDeck(possible_decks)
                if deck_number == 0:
                    print("The deck has not been changed. It is still {}.".format(deck_name))
                    input("Enter to continue\n")
                else:
                    deck_number = deck_number - 1
                    deck_name = possible_decks[deck_number]
                    print("Established deck: {}.".format(deck_name))
                    input("Enter to continue\n")

            elif opt == 3:
                max_rounds = option_two_functions.setMaxRounds()
                print("Established maximum of rounds to {}.".format(max_rounds))
                input("Enter to continue\n")

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
        cards = database.getCards(possible_decks.index(deck_name)+1)
        deck = list(cards.keys())

        if len(game) >= 2:
            game_variables = {"players":players,"game":game,"cards":cards,"deck":deck,"deck_id":possible_decks.index(deck_name),"round":0,"max_rounds":max_rounds}
            option_three_functions.playGame(game_variables)
            game_variables.clear()
        else:
            print("\nYou cannot play. Please, choose at least 2 players for the game.")
            input("Enter to continue\n")

        flg_03 = False
        flg_00 = True

    while flg_04:
        print(menu04)
        opt = input("Option: ")
        if not opt.isdigit():
            print("\nInvalid option")
            input("Enter to continue\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 4:
                print("\nInvalid option")
                input("Enter to continue\n")
            elif opt == 1:
                option_four_functions.rankingMoreEarnings()
            elif opt == 2:
                option_four_functions.rankingMoreGames()
            elif opt == 3:
                option_four_functions.rankingMoreMinutes()
            else:
                flg_04 = False
                flg_00 = True

    while flg_05:
        print(menu05)
        opt = input("Option: ")
        if not opt.isdigit():
            print("\nInvalid option")
            input("Enter to continue\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 8:
                print("\nInvalid option")
                input("Enter to continue\n")
            elif opt == 1:
                option_five_functions.report1()
            elif opt == 2:
                option_five_functions.report2()
            elif opt == 3:
                option_five_functions.report3()
            elif opt == 4:
                option_five_functions.report7()
            elif opt == 5:
                option_five_functions.report8()
            elif opt == 6:
                option_five_functions.report9()
            elif opt == 7:
                option_five_functions.report10()
            else:
                flg_05 = False
                flg_00 = True

