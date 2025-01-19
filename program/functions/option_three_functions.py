import datetime
import random
import functions.titles as titles
import functions.database as database
#REVISAR QUÉ VARIABLES PUEDO PONER COMO GLOBALES (ej. players, cards...)

def playGame(players,game,deck,deckID,cards,max_rounds):
    if deckID == 0 or deckID == 1:
        gameID = database.newGame(deck = 1)
    else:
        gameID = database.newGame(deck = 2)
    game_variables = {"gameID":gameID}

    print("*"*136 + "\n" + titles.title_seven_and_half_centred + "\n" + "*"*136)

    round = 0
    exit = False

    resetPointsInitialCard(players,game) #Le damos a todos los jugadores 20 puntos para empezar, y sitio para guardar la carta inicial

    while len(game) > 1 and round <= max_rounds and not exit:
        if players[game[0]]["initialCard"] == "":
            setGamePriority(players,game,deck,cards)
        round = playRound(players,game,deck,cards,round)
        exit = exitGame()

    winner(players,game,round,max_rounds)
    input("Enter to continue")

def resetPointsInitialCard(players,game):
    for player in game:
        players[player]["points"] = 20
        players[player]["initialCard"] = ""
    print("\nEvery player has now 20 points to start playing!\n")


def setGamePriority(players,game,deck,cards):
    used_cards = []

    #Damos la carta inicial a todos los jugadores
    for player in game:
        index_deck = random.randint(0,len(deck)-1) #Se elige aleatoriamente un indice de la lista
        players[player]["initialCard"] = deck[index_deck] #Se añade como carta inicial del jugador la carta que este en el índice elegido de la lista

        used_cards.append(deck[index_deck]) #Metemos la carta que haya salido en used_cards
        deck.remove(deck[index_deck]) #Lo eliminamos de la lista de deck, para que dos jugadores no puedan tener la misma carta inicial

    deck = deck + used_cards #Volvemos a meter en la baraja todas las cartas usadas

    #Ordenamos la lista de jugadores según su prioridad (el primer elemento de la lista ordenada será el de mayor prioridad)
    for sweep in range(len(game) - 1):
        cambio = False
        for i in range(len(game) - (sweep + 1)):
            if cards[players[game[i + 1]]["initialCard"]]["value"] < cards[players[game[i]]["initialCard"]]["value"]: #Si el número de la carta inicial del jugador 2 es menor que el del jugador 1, los intercambiamos de sitio
                cambio = True
                aux = game[i + 1]
                game[i + 1] = game[i]
                game[i] = aux
            elif cards[players[game[i + 1]]["initialCard"]]["value"] == cards[players[game[i]]["initialCard"]]["value"]: #Si el número de la carta para dos jugadores es igual, compararemos el palo y su prioridad para desempatar
                if cards[players[game[i + 1]]["initialCard"]]["priority"] < cards[players[game[i]]["initialCard"]]["priority"]:
                    cambio = True
                    aux = game[i + 1]
                    game[i + 1] = game[i]
                    game[i] = aux
        if not cambio:
            break

    summary = "*" * 60 + "\n" + "Name".center(20) + "Initial Card".center(20) + "Priority".center(
        20) + "\n" + "*" * 60 + "\n"
    for i in range(len(game)):
        if i == len(game)-1:
            players[game[i]]["bank"] = True  # Al jugador de mayor prioridad, se le establece como banca
        else:
            players[game[i]]["bank"] = False
        players[game[i]]["priority"] = i+1 #Le ponemos a cada jugador su numero de prioridad

        summary += "{}".format(players[game[i]]["name"]).center(20) + "{}".format(players[game[i]]["initialCard"]).center(
            20) + "{}".format(players[game[i]]["priority"]).center(20) + "\n"
    print(summary)
    print("{}, the player with the most priority, is now the Bank!\n".format(players[game[-1]]["name"]))


    input("Enter to continue")


def playRound(players,game,deck,cards,round):
    """round_variables = {}"""

    round +=1
    print("*" * 136 + "\n" + titles.title_seven_and_half_centred + "\n")
    print("Round: {}".format(round).center(136,"*"))

    for player in game:
        players[player]["bet"] = 0 # Ponemos a 0 las apuestas de todos los jugadores, así evitamos que la banca de error al no tener bet

    losingPot = setBet(players,game)
    used_cards = []

    resettingPlayerRoundValues(players, game)

    print("\nThe first card of each player is about to be given!\n")
    summary = "*" * 60 + "\n" + "Name".center(20) + "Card".center(20) + "Round Points".center(20) + "\n" + "*" * 60 + "\n"
    for player in game:
        hitCard(players, player, game, deck, cards, used_cards,losingPot) #Se le da a todos los jugadores la primera carta de la ronda
        summary += "{}".format(players[player]["name"]).center(20) + "{}".format(players[player]["cards"][0]).center(20) + "{}".format(players[player]["roundPoints"]).center(20) + "\n"
    print(summary)

    for player in game:
        if players[player]["bank"]:
            print("*" * 136 + "\n" + titles.title_seven_and_half_centred + "\n" + "*" * 136)
            print("{}'s (BANK) turn (round {})".format(players[player]["name"],round).center(136,"*") + "\n")
            if players[player]["human"]:
                humanRound(players,player,game,deck,cards,used_cards,losingPot)
            else:
                bankRound(players,player,game,deck,cards,used_cards,losingPot)
            input("Enter to continue")
        else:
            if players[player]["human"]:
                print("*" * 136 + "\n" + titles.title_seven_and_half_centred + "\n" + "*" * 136)
                print("{}'s turn (round {})".format(players[player]["name"],round).center(136,"*") + "\n")
                humanRound(players,player,game,deck,cards,used_cards,losingPot)
                input("Enter to continue")
            else:
                print("*" * 136 + "\n" + titles.title_seven_and_half_centred + "\n" + "*" * 136)
                print("{}'s turn (round {})".format(players[player]["name"],round).center(136,"*") + "\n")
                botRound(players, player, game, deck, cards, used_cards,losingPot)
                input("Enter to continue")

    showSummaryStats(players, game)
    givePoints_bankCandidates(players,game,losingPot)
    input("Enter to continue")
    showSummaryStats(players,game)
    eliminatingPlayersWith0Points(players,game)
    showSummaryStats(players,game)

    deck = deck + used_cards # Resetting the deck
    return round

def setBet(players,game):
   losingPot = 0
   for player in game:
       if players[player]["bank"]:
           continue

       else:
           print("{}'s turn".format(players[player]["name"]).center(136, "*") + "\n")
           if players[player]["human"]:
               while True:
                   bet = input("Set your bet (or put 0 if you want it done automatically): ")
                   if not bet.isdigit():
                       print("\nInvalid value.")
                       input("Enter to continue\n")
                   else:
                       bet = int(bet)
                       if bet == 0:
                           players[player]["bet"] = int(players[player]["points"]*(players[player]["type"]/100))
                           print("Your bet as {} has been established as {} points.\n".format(players[player]["name"],players[player]["bet"]))
                           losingPot += players[player]["bet"]
                           break
                       elif bet > players[player]["points"]:
                           print("\nInvalid value.")
                           input("Enter to continue\n")
                       else:
                           players[player]["bet"] = bet
                           print("Your bet as {} has been established as {} points.\n".format(players[player]["name"],players[player]["bet"]))
                           losingPot += bet
                           break
           else:
               players[player]["bet"] = players[player]["points"]*(players[player]["type"]/100)
               print("{}'s bet is of {} points.\n".format(players[player]["name"],players[player]["bet"]))
               losingPot += players[player]["bet"]

   input("Enter to continue")
   return losingPot

def bankRound(players,player,game,deck,cards,used_cards,losingPot):
    while mustBankHit(players,player,deck,cards,game,losingPot):
        hitCard(players,player,game,deck,cards,used_cards,losingPot)


def humanRound(players,player,game,deck,cards,used_cards,losingPot):
    while players[player]["roundPoints"] < 7.5:
        menuHumanRound = "\n1) View Stats\n2) View Game Stats\n3) Hit\n4) Stand\n5) Automatic Play\n"
        print(menuHumanRound)
        opt = input("Option: ")
        if not opt.isdigit():
            print("\nInvalid option\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 5:
                print("\nInvalid option\n")
            elif opt == 1:
                viewStats(players,player)
            elif opt == 2:
                viewGameStats(players,game)
            elif opt == 3:
                percentage_risk = calculateRisk(players,player,deck,cards)
                while True:
                    answer = input("You have {:.1f}% chance of exceeding 7,5. Are you sure that you want another card? Y/N ".format(percentage_risk))
                    if not answer.isalpha():
                        print("\nInvalid answer\n")
                    elif answer.upper() == "Y":
                        losingPot = hitCard(players, player, game, deck, cards, used_cards, losingPot)
                        break
                    elif answer.upper() == "N":
                        break
                    else:
                        print("\nInvalid answer\n")

            elif opt == 4:
                print("\nI stand with {} points!\n".format(players[player]["roundPoints"]))
                return
            else:
                if players[player]["bank"]:
                    bankRound(players,player,game,deck,cards,used_cards,losingPot)
                else:
                    botRound(players,player,game,deck,cards,used_cards,losingPot)
                return


def botRound(players,player,game,deck,cards,used_cards,losingPot):
    while players[player]["roundPoints"] < 7.5:
        if shouldTakeRisk(players,player,deck,cards):
            print("\n{} wants another card.\n".format(players[player]["name"]))
            losingPot = hitCard(players,player,game,deck,cards,used_cards,losingPot)
        else:
            print("\n{} stands with {} points!\n".format(players[player]["name"],players[player]["roundPoints"]))
            return

# Evaluación de riesgo para todos los jugadores, devuelve True si el jugador debe pedir carta
# currentPoints: puntos actuales del jugador
# remainingCards: cartas que quedan por salir
# riskProfile: perfil de riesgo del jugador
def shouldTakeRisk(players,player,deck,cards):
    count = 0
    for card in deck:
        if cards[card]["realValue"] + players[player]["roundPoints"] > 7.5:
            count += 1    # Contamos las cartas que nos harían perder
    risk = count / len(deck) * 100    # Calculamos las probabilidades de que salga una carta que nos haga pasarnos
    if players[player]["type"] > risk:
        return True
    return False

def calculateRisk(players,player,deck,cards):
    count = 0
    for card in deck:
        if cards[card]["realValue"] + players[player]["roundPoints"] > 7.5:
            count += 1  # Contamos las cartas que nos harían perder
    risk = count / len(deck) * 100  # Calculamos las probabilidades de que salga una carta que nos haga pasarnos
    return risk

def viewStats(players,player):
    card_str = ""
    for i in range(len(players[player]["cards"])):
        if i == len(players[player]["cards"])-1:
            card_str += players[player]["cards"][i]
        else:
            card_str += players[player]["cards"][i] + ","

    stats = "{} Stats".format(players[player]["name"]).center(136,"*") + "\n"\
    + "Name:".ljust(68) + "{}".format(players[player]["name"]).upper() + "\n" \
    + "Bank:".ljust(68) + "{}".format(players[player]["bank"]) + "\n" \
    + "Type:".ljust(68) + "{}".format(players[player]["type"]) + "\n"\
    + "Human:".ljust(68) + "{}".format(players[player]["human"]) + "\n"\
    + "Initial Card:".ljust(68) + "{}".format(players[player]["initialCard"]) + "\n"\
    + "Priority:".ljust(68) + "{}".format(players[player]["priority"]) + "\n"\
    + "Bet:".ljust(68) + "{}".format(players[player]["bet"]) + "\n"\
    + "Points:".ljust(68) + "{}".format(players[player]["points"]) + "\n"\
    + "Cards:".ljust(68) + "{}".format(card_str) + "\n"\
    + "Round Points:".ljust(68) + "{}".format(players[player]["roundPoints"]) + "\n"

    print("*" * 136 + "\n" + titles.title_stats_centred + "\n" + "*" * 136)
    print("\n" + stats + "\n")
    input("Enter to continue")

def viewGameStats(players,game):
    char_player = 136//(len(game)+1)

    name_str = ""
    bank_str = ""
    type_str = ""
    human_str = ""
    initialCard_str = ""
    priority_str = ""
    bet_str = ""
    points_str = ""
    cards_str = ""
    roundPoints_str = ""

    for player in game:
        name_str += players[player]["name"].ljust(char_player).upper()
        bank_str += str(players[player]["bank"]).ljust(char_player)
        type_str += str(players[player]["type"]).ljust(char_player)
        human_str += str(players[player]["human"]).ljust(char_player)
        initialCard_str += players[player]["initialCard"].ljust(char_player)
        priority_str += str(players[player]["priority"]).ljust(char_player)
        bet_str += str(players[player]["bet"]).ljust(char_player)
        points_str += str(players[player]["points"]).ljust(char_player)
        roundPoints_str += str(players[player]["roundPoints"]).ljust(char_player)

        card_str = ""
        for i in range(len(players[player]["cards"])):
            if i == len(players[player]["cards"]) - 1:
                card_str += players[player]["cards"][i]
            else:
                card_str += players[player]["cards"][i] + ","
        cards_str += card_str.ljust(char_player)

    stats = "Name:".ljust(char_player) + "{}".format(name_str).ljust(char_player) + "\n" \
    + "Bank:".ljust(char_player) + "{}".format(bank_str).ljust(char_player) + "\n"\
    + "Type:".ljust(char_player) + "{}".format(type_str).ljust(char_player) + "\n"\
    + "Human:".ljust(char_player) + "{}".format(human_str).ljust(char_player) + "\n"\
    + "Initial Card:".ljust(char_player) + "{}".format(initialCard_str).ljust(char_player) + "\n"\
    + "Priority:".ljust(char_player) + "{}".format(priority_str).ljust(char_player) + "\n"\
    + "Bet:".ljust(char_player) + "{}".format(bet_str).ljust(char_player) + "\n"\
    + "Points:".ljust(char_player) + "{}".format(points_str).ljust(char_player) + "\n"\
    + "Cards:".ljust(char_player) + "{}".format(cards_str).ljust(char_player) + "\n"\
    + "Round Points:".ljust(char_player) + "{}".format(roundPoints_str).ljust(char_player) + "\n"

    print("*" * 136 + "\n" + titles.title_stats_centred + "\n" + "*" * 136)
    print("\n" + stats + "\n")
    input("Enter to continue")

def showSummaryStats(players,game):
    char_player = 136 // (len(game) + 1)

    name_str = ""
    bank_str = ""
    type_str = ""
    human_str = ""
    priority_str = ""
    points_str = ""

    for player in game:
        name_str += players[player]["name"].ljust(char_player).upper()
        bank_str += str(players[player]["bank"]).ljust(char_player)
        type_str += str(players[player]["type"]).ljust(char_player)
        human_str += str(players[player]["human"]).ljust(char_player)
        priority_str += str(players[player]["priority"]).ljust(char_player)
        points_str += str(players[player]["points"]).ljust(char_player)

    stats = "Name:".ljust(char_player) + "{}".format(name_str).ljust(char_player) + "\n" \
            + "Bank:".ljust(char_player) + "{}".format(bank_str).ljust(char_player) + "\n" \
            + "Type:".ljust(char_player) + "{}".format(type_str).ljust(char_player) + "\n" \
            + "Human:".ljust(char_player) + "{}".format(human_str).ljust(char_player) + "\n" \
            + "Priority:".ljust(char_player) + "{}".format(priority_str).ljust(char_player) + "\n" \
            + "Points:".ljust(char_player) + "{}".format(points_str).ljust(char_player) + "\n"

    print("\n" + stats + "\n")
    input("Enter to continue")


def hitCard(players, player, game, deck, cards, used_cards, losingPot):
    index_deck = random.randint(0, len(deck) - 1)  # Se elige aleatoriamente un indice de la lista

    players[player]["cards"].append(deck[index_deck])
    players[player]["roundPoints"] += cards[deck[index_deck]]["realValue"]

    if len(players[player]["cards"]) != 1:
        print("{} is {}'s card, which means {} has now {} points!".format(players[player]["cards"][-1],players[player]["name"],players[player]["name"],players[player]["roundPoints"]))

    used_cards.append(deck[index_deck])  # Metemos la carta que haya salido en used_cards
    deck.remove(deck[index_deck])  # Lo eliminamos de la lista de deck, para que dos jugadores no puedan sacar en una misma ronda la misma carta

    losingPot = tooManyPoints(players, player, game, losingPot)
    return losingPot

# La banca debe pedir carta o plantarse
# bankPoints: puntos de la banca
# cardsValue: valor de las cartas de la banca
# losingPot: el bote que perdería la banca actualmente si se planta
# winningPlayers: cantidad de jugadores que ganan a la banca
# losingPlayers: cantidad de jugadores que pierden a la banca
def mustBankHit(players,player,deck,cards,game,losingPot):
    winningPlayers = 0
    for id in game:
        if players[id]["roundPoints"] > players[player]["roundPoints"]:
            winningPlayers += 1


    if players[player]["roundPoints"] >= 7.5:    # Si la banca ya tiene 7.5 o más
        return False

    if winningPlayers == 0:   # Si no hay jugadores que ganen a la banca
        return False

    if players[player]["points"] <= losingPot:   # Si la banca tiene menos puntos que el bote que perdería
        return True

    #La banca no tiene 7,5 ni más, hay jugadores que ganan a la banca y tiene puntos como para pagar las apuestas sin perder
    return shouldTakeRisk(players,player,deck,cards)

def givePoints_bankCandidates(players,game,losingPot):
    bankCandidates = []

    for player in game:
        if players[game[-1]]["roundPoints"] != 7.5: # Si la banca no ha sacado un 7,5
            if players[player]["roundPoints"] == 7.5: # Y otro jugador sí, ganará el doble de puntos y será candidato a la banca
                losingPot += players[player]["bet"]
                players[player]["bet"] += players[player]["bet"]
                bankCandidates.append(player) # Esta lista ya estará ordenada de menor a mayor prioridad porque la lista game está ordenada así
                print("{} is a Bank Candidate and will earn the double of his bet!!".format(players[player]["name"]))

    if players[game[-1]]["roundPoints"] == 7.5: # Si la banca tiene 7,5, habrá ganado a todos los jugadores (porque en caso de empate, gana la banca)
        players[game[-1]]["points"] += losingPot # Le sumamos todos los puntos apostados de los jugadores que no se habían pasado de 7,5

        for player in game:
            if players[player]["bet"] != 0:
                players[player]["points"] -= players[player]["bet"] # Le restamos los puntos apostados a todos los jugadores a los que no se les haya restado ya
        print("The Bank, {}, has defeated everyone in this round and now has {} points.".format(players[game[-1]]["name"],players[game[-1]]["points"]))
    elif players[game[-1]]["roundPoints"] > 7.5:
        if players[game[-1]]["points"] >= losingPot:
            players[game[-1]]["points"] -= losingPot
            print("The Bank, {}, has lost {} points and now has {} points.".format(players[game[-1]]["name"],losingPot,players[game[-1]]["points"]))
            for i in range(len(game)-2,-1,-1):
                if players[game[i]]["roundPoints"] <= 7.5:
                    players[game[i]]["points"] += players[game[i]]["bet"]
                    print("{} has won {} points, and now has {} points!".format(players[game[i]]["name"],players[game[i]]["bet"],players[game[i]]["points"]))
        else:
            while players[game[-1]]["points"] > 0:
                for i in range(len(game) - 2, -1, -1):
                    if players[game[i]]["roundPoints"] <= 7.5:
                        if players[game[i]]["bet"] < players[game[-1]]["points"]:
                            players[game[-1]]["points"] -= players[game[i]]["bet"]
                            players[game[i]]["points"] += players[game[i]]["bet"]
                            print("{} has won {} points, and now has {} points!".format(players[game[i]]["name"],
                                                                                    players[game[i]]["bet"],
                                                                                    players[game[i]]["points"]))
                        elif players[game[i]]["bet"] == players[game[-1]]["points"]:
                            players[game[-1]]["points"] -= players[game[i]]["bet"]
                            players[game[i]]["points"] += players[game[i]]["bet"]
                            print("{} has won {} points, and now has {} points!\nThe Bank has ran out of points, if any other character had to receive points, they won't.".format(
                                players[game[i]]["name"],
                                players[game[i]]["bet"],
                                players[game[i]]["points"]))
                            break
                        else:
                            players[game[i]]["points"] += players[game[-1]]["points"]

                            print("The bank didn't have enough points.\n{} has won {} points, and now has {} points!\nIf any other player had to receive points, they won't.".format(
                                    players[game[i]]["name"],
                                    players[game[-1]]["points"],
                                    players[game[i]]["points"]))

                            players[game[-1]]["points"] = 0

                            break
    else:
        for i in range(len(game) - 2, -1, -1):
            if players[game[-1]]["roundPoints"] < players[game[i]]["roundPoints"] and players[game[i]]["roundPoints"] <= 7.5:
                if players[game[-1]]["points"] > players[game[i]]["bet"]:
                    players[game[i]]["points"] += players[game[i]]["bet"]
                    players[game[-1]]["points"] -= players[game[i]]["bet"]
                    print("{} has won {} points, and now has {} points!".format(players[game[i]]["name"],
                                                                                players[game[i]]["bet"],
                                                                                players[game[i]]["points"]))
                elif players[game[-1]]["points"] == players[game[i]]["bet"]:
                    players[game[i]]["points"] += players[game[i]]["bet"]
                    players[game[-1]]["points"] = 0
                    print("{} has won {} points, and now has {} points!\nThe Bank has ran out of points, if any other character had to receive points, they won't.".format(
                            players[game[i]]["name"],
                            players[game[i]]["bet"],
                            players[game[i]]["points"]))
                    break
                else:
                    players[game[i]]["points"] += players[game[-1]]["points"]

                    print("The Bank didn't have enough points.\n{} has won {} points, and now has {} points!\nThe rest of the players won't receive any points.".format(
                            players[game[i]]["name"],
                            players[game[-1]]["points"],
                            players[game[i]]["points"]))

                    players[game[-1]]["points"] = 0
                    break


    if len(bankCandidates) != 0: # Si hay candidatos a la banca
        if players[game[-1]]["points"] == 0: # Y la banca actual debe ser eliminada
            print("{}, who was the Bank, has been eliminated!".format(players[game[-1]]["name"]))
            game.remove(game[-1]) # Eliminamos a la banca de la lista de jugadores

            players[bankCandidates[-1]]["bank"] = True  #Ponemos al jugador más prioritario de la lista de candidatos como banca
            print("{} is now the Bank!".format(players[bankCandidates[-1]]["name"]))
            game.remove(bankCandidates[-1]) # Y lo quitamos de la lista de jugadores para añadirlo al final
            game.append(bankCandidates[-1])

        else: # Si la banca actual puede seguir jugando aunque sin ser banca
            players[game[-1]]["bank"] = False # Cambiamos el status del jugador que era banca y del jugador más prioritario de la lista de candidatos
            players[bankCandidates[-1]]["bank"] = True
            print("{} is no longer the Bank. Now it is {}!".format(players[game[-1]]["name"],players[bankCandidates[-1]]["name"]))

            game.remove(bankCandidates[-1]) # Quitamos a la nueva banca de la lista de jugadores

            for sweep in range(len(game) - 1): # Ordenamos la lista según las prioridades de los jugadores
                cambio = False
                for i in range(len(game) - (sweep + 1)):
                    if players[game[i + 1]]["priority"] < players[game[i]]["priority"]:  # Si el número de prioridad del jugador 2 es menor que el del jugador 1, los intercambiamos de sitio
                        cambio = True
                        aux = game[i + 1]
                        game[i + 1] = game[i]
                        game[i] = aux
                if not cambio:
                    break

            game.append(bankCandidates[-1]) # Añadimos a la nueva banca al final

    else: # Si no hay candidatos a la banca
        if players[game[-1]]["points"] == 0: # Y la banca actual debe ser eliminada
            print("{}, who was the Bank, has been eliminated!".format(players[game[-1]]["name"]))
            game.remove(game[-1]) # Quitamos a la banca de la lista

            players[game[-1]]["bank"] = True # Y el nuevo último jugador de la lista (el más prioritario) pasará a ser banca
            print("{} is now the Bank!".format(players[game[-1]]["name"]))

def tooManyPoints(players, player, game, losingPot):
    if players[player]["bank"] and players[player]["roundPoints"]>7.5:
        print("The bank, {}, has too many round points and has lost the round!".format(players[player]["name"]))
    else:
        if players[player]["roundPoints"] > 7.5:
            players[player]["points"] -= players[player]["bet"] # Le quitamos los puntos apostados al jugador que ha perdido
            players[game[-1]]["points"] += players[player]["bet"] # Le sumamos los puntos apostados del jugador que ha perdido a la banca

            losingPot -= players[player]["bet"] # Restamos la apuesta de este jugador a lo que tendría que pagar la banca si perdiera contra todos

            print("{} has too many round points and has lost the round!\nWhich means that {} has lost {} points, and now has {} points!\nTherefore, {}, the Bank, now has {} points!".format(players[player]["name"],players[player]["name"],players[player]["bet"],players[player]["points"],players[game[-1]]["name"],players[game[-1]]["points"]))
            players[player]["bet"] = 0
            eliminatingPlayersWith0Points(players,game)
            return losingPot

def eliminatingPlayersWith0Points(players,game):
    for player in game:
        if players[player]["points"] == 0:
            print("{} has been eliminated from the game!".format(players[player]["name"]))
            game.remove(player)
            input("Enter to continue")

def resettingPlayerRoundValues(players,game):
    for player in game:
        players[player]["cards"] = []
        players[player]["roundPoints"] = 0

def exitGame():
    while True:
        answer = input("Press enter to continue or write exit to exit the game: ")
        if answer == "":
            return False
        else:
            if not answer.isalpha():
                print("\nInvalid answer\n")
            elif answer.lower() != "exit":
                print("\nInvalid answer\n")
            else:
                return True

def winner(players,game,round,max_rounds):
    if len(game) == 1:
        print("{} has won with {} points after {} rounds!!! CONGRATULATIONS!".format(players[game[0]]["name"],players[game[0]]["points"],round))
    else:
        #Si se ha llegado al máximo de rondas o hemos elegido abandonar el juego, se ordenará la lista para dejar en primera posición al jugador con más puntos
        for sweep in range(len(game) - 1):
            cambio = False
            for i in range(len(game) - (sweep + 1)):
                if players[game[i + 1]]["points"] > players[game[i]]["points"]:  # Si el jugador 2 tiene más puntos que el jugador 1, los intercambiamos de sitio
                    cambio = True
                    aux = game[i + 1]
                    game[i + 1] = game[i]
                    game[i] = aux
            if not cambio:
                break
        if round == max_rounds:
            print("The maximum number of round has been reached!\nThe winner, with {} points, is {}!!! CONGRATULATIONS!".format(players[game[0]]["points"],players[game[0]]["name"]))
        else:
            print("You have chosen to exit the game.\nThe winner, with {} points, is {}!!! CONGRATULATIONS!".format(players[game[0]]["points"],players[game[0]]["name"]))