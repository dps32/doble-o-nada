import random
import functions.titles as titles
#REVISAR QUÉ VARIABLES PUEDO PONER COMO GLOBALES (ej. players, cards...)
"""
def setGamePriority(deck):

def fill_player_game(player_game,gameID,*fields):

def fill_player_game_round(player_game_round,round,*fields):

def checkMinimum2PlayerWithPoints():

def orderAllPlayers():

def standardRound(id,deck):

def humanRound(id,deck):

def distributionPointAndNewBankCandidates():

"""
def playGame(players,game,deck,cards,max_rounds):
    round = 0
    exit = False

    resetPoints(players,game) #Le damos a todos los jugadores 20 puntos para empezar

    while len(game) > 1 and round <= max_rounds and not exit:
        if players[game[0]]["initialCard"] == "":
            setGamePriority(players,game,deck,cards)
        round = playRound(players,game,deck,cards,round)
        exit = exitGame()

    winner(players,game,round,max_rounds)

def resetPoints(players,game):
    for player in game:
        players[player]["points"] = 20
        print("\nEvery player has now 20 points to start playing!\n")


def setGamePriority(players,game,deck,cards):
    used_cards = []

    #Damos la carta inicial a todos los jugadores
    for player in game:
        index_deck = random.randint(0,len(deck)-1) #Se elige aleatoriamente un indice de la lista
        players[player]["initialCard"] = deck[index_deck] #Se añade como carta inicial del jugador la carta que este en el índice elegido de la lista
        print("The initial card of {} is {}.".format(players[player]["name"],players[player]["initialCard"]))
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

    for i in range(len(game)):
        players[game[i]]["priority"] = i+1 #Le ponemos a cada jugador su numero de prioridad
        print("{} has priority {}.".format(players[game[i]]["name"],i+1))

    for i in range(len(game)):
        if i == len(game)-1:
            players[game[i]]["bank"] = True #Al jugador de mayor prioridad, se le establece como banca
            print("{}, the player with the most priority, is now the Bank!".format(players[game[i]]["name"]))
        else:
            players[game[i]]["bank"] = False


def playRound(players,game,deck,cards,round):
    round +=1
    print("Round: ",round)
    losingPot = setBet(players,game)
    used_cards = []

    resettingPlayerRoundValues(players, game)

    for player in game:
        print("The first card of each player is about to be given!")
        hitCard(players, player, game, deck, cards, used_cards,losingPot) #Se le da a todos los jugadores la primera carta de la ronda

    for player in game:
        if players[player]["bank"] == True:
            print("Bank's turn!")
            bankRound(players,player,game,deck,cards,used_cards,losingPot)
        else:
            if players[player]["human"] == True:
                print("{}'s turn".format(players[player]["name"]))
                humanRound(players,player,game,deck,cards,used_cards,losingPot)
            else:
                print("{}'s turn".format(players[player]["name"]))
                botRound(players, player, game, deck, cards, used_cards,losingPot)

    givePoints_bankCandidates(players,game,losingPot)
    eliminatingPlayersWith0Points(players,game)

    deck = deck + used_cards # Resetting the deck
    return round

def setBet(players,game):
   losingPot = 0
   for player in game:
       if players[player]["bank"]:
           continue
       else:
           if players[player]["human"]:
               while True:
                   bet = input("Set your bet (or put 0 if you want it done automatically): ")
                   if not bet.isdigit():
                       print("\nInvalid value.\n")
                   else:
                       bet = int(bet)
                       if bet == 0:
                           players[player]["bet"] = players[player]["points"]*(players[player]["type"]/100)
                           print("Your bet as {} has been established as {} points.".format(players[player]["name"],players[player]["bet"]))
                           losingPot += players[player]["bet"]
                           break
                       elif bet > players[player]["points"]:
                           print("\nInvalid value.\n")
                       else:
                           players[player]["bet"] = bet
                           print("Your bet as {} has been established as {} points.".format(players[player]["name"],players[player]["bet"]))
                           losingPot += bet
                           break
           else:
               players[player]["bet"] = players[player]["points"]*(players[player]["type"]/100)
               print("{}'s bet is of {} points.".format(players[player]["name"],players[player]["bet"]))
               losingPot += players[player]["bet"]

   return losingPot

def bankRound(players,player,game,deck,cards,used_cards,losingPot):
    while mustBankHit(players,player,deck,cards,game,losingPot):
        hitCard(players,player,game,deck,cards,used_cards,losingPot)


def humanRound(players,player,game,deck,cards,used_cards,losingPot):
    while players[player]["roundPoints"] < 7.5:
        menuHumanRound = "\n1) View Stats\n2) View Game Stats\n3) Hit\n4) Stand\n5) Automatic Play\n"
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
                losingPot = hitCard(players,player,game,deck,cards,used_cards,losingPot)
            elif opt == 4:
                return
            else:
                botRound(players,player,game,deck,cards,used_cards,losingPot)


def botRound(players,player,game,deck,cards,used_cards,losingPot):
    while players[player]["roundPoints"] < 7.5:
        if shouldTakeRisk(players,player,deck,cards):
            losingPot = hitCard(players,player,game,deck,cards,used_cards,losingPot)
        else:
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

def viewStats(players,player):
    card_str = ""
    for i in range(len(players[player]["cards"])):
        if i == len(players[player]["cards"])-1:
            card_str += players[player]["cards"][i]
        else:
            card_str += players[player]["cards"][i] + ","

    stats = "{} Stats".format(players[player]["name"]).center(136,"*") + "\n"\
    + "Name:".ljust(68) + "{}".format(players[player]["name"]) + "\n"\
    + "Type:".ljust(68) + "{}".format(players[player]["type"]) + "\n"\
    + "Human:".ljust(68) + "{}".format(players[player]["human"]) + "\n"\
    + "Initial Card:".ljust(68) + "{}".format(players[player]["initialCard"]) + "\n"\
    + "Priority:".ljust(68) + "{}".format(players[player]["priority"]) + "\n"\
    + "Bet:".ljust(68) + "{}".format(players[player]["bet"]) + "\n"\
    + "Points:".ljust(68) + "{}".format(players[player]["points"]) + "\n"\
    + "Cards:".ljust(68) + "{}".format(card_str) + "\n"\
    + "Round Points:".ljust(68) + "{}".format(players[player]["roundPoints"]) + "\n"

    print(stats)

def viewGameStats(players,game):
    char_player = 136//(len(game)+1)

    name_str = ""
    type_str = ""
    human_str = ""
    initialCard_str = ""
    priority_str = ""
    bet_str = ""
    points_str = ""
    cards_str = ""
    roundPoints_str = ""

    for player in game:
        name_str += players[player]["name"].ljust(char_player)
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

    stats = "Name:".ljust(68) + "{}".format(name_str) + "\n"\
    + "Type:".ljust(68) + "{}".format(type_str) + "\n"\
    + "Human:".ljust(68) + "{}".format(human_str) + "\n"\
    + "Initial Card:".ljust(68) + "{}".format(initialCard_str) + "\n"\
    + "Priority:".ljust(68) + "{}".format(priority_str) + "\n"\
    + "Bet:".ljust(68) + "{}".format(bet_str) + "\n"\
    + "Points:".ljust(68) + "{}".format(points_str) + "\n"\
    + "Cards:".ljust(68) + "{}".format(cards_str) + "\n"\
    + "Round Points:".ljust(68) + "{}".format(roundPoints_str) + "\n"

    print(stats)


def hitCard(players, player, game, deck, cards, used_cards, losingPot):
    index_deck = random.randint(0, len(deck) - 1)  # Se elige aleatoriamente un indice de la lista

    players[player]["cards"].append(deck[index_deck])
    players[player]["roundPoints"] += cards[deck[index_deck]]["realValue"]
    print("{} is {}'s card, which means {} has now {} points!".format(players[player]["cards"][-1],players[player]["name"],players[player]["name"],players[player]["points"]))

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

    if players[game[-1]]["roundPoints"] == 7.5: # Si la banca tiene 7,5, habrá ganado a todos los jugadores (porque en caso de empate, gana la banca)
        players[game[-1]]["points"] += losingPot # Le sumamos todos los puntos apostados de los jugadores que no se habían pasado de 7,5

        for player in game:
            if players[player]["bet"] != 0:
                players[player]["points"] -= players[player]["bet"] # Le restamos los puntos apostados a todos los jugadores a los que no se les haya restado ya
        print("The Bank, {}, has defeated everyone in this round and now has {} points.".format(players[game[-1]]["name"],players[game[-1]]["points"]))
    elif players[game[-1]]["roundPoints"] > 7.5:
        if players[game[-1]]["points"] <= losingPot:
            players[game[-1]]["points"] -= losingPot
            print("The Bank, {}, has lost {} points and now has {} points.".format(players[game[-1]]["name"],losingPot,players[game[-1]]["points"]))
            for i in range(len(game)-2,0,-1):
                if players[game[i]]["roundPoints"] <= 7.5:
                    if players[game[i]]["roundPoints"] == 7.5:
                        bankCandidates.append(game[i])
                        print("{} is a Bank Candidate!!".format(players[game[i]]["name"]))
                    players[game[i]]["points"] += players[game[i]]["bet"]
                    print("{} has won {} points, and now has {} points!".format(players[game[i]]["name"],players[game[i]]["bet"],players[game[i]]["points"]))
        else:
            while players[game[-1]]["points"] > 0:
                for i in range(len(game) - 2, 0, -1):
                    if players[game[i]]["roundPoints"] <= 7.5:
                        if players[game[i]]["roundPoints"] == 7.5:
                            bankCandidates.append(game[i])
                            print("{} is a Bank Candidate!!".format(players[game[i]]["name"]))
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
        for i in range(len(game) - 2, 0, -1):
            if players[game[-1]]["roundPoints"] < players[game[i]]["roundPoints"] and players[game[i]]["roundPoints"] <= 7.5:
                if players[game[i]]["roundPoints"] == 7.5:
                    bankCandidates.append(game[i])
                    print("{} is a Bank Candidate!!".format(players[game[i]]["name"]))
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

                    print("The bank didn't have enough points.\n{} has won {} points, and now has {} points!\nThe rest of the players won't receive any points.".format(
                            players[game[i]]["name"],
                            players[game[-1]]["points"],
                            players[game[i]]["points"]))

                    players[game[-1]]["points"] = 0
                    break

    if len(bankCandidates) != 0:
        players[game[-1]]["bank"] = False
        players[bankCandidates[-1]]["bank"] = True

        game.remove(bankCandidates[-1])
        game.append(bankCandidates[-1])

def tooManyPoints(players, player, game, losingPot):
    if players[player]["roundPoints"] > 7.5:
        players[player]["points"] -= players[player]["bet"] # Le quitamos los puntos apostados al jugador que ha perdido
        players[game[-1]]["points"] += players[player]["bet"] # Le sumamos los puntos apostados del jugador que ha perdido a la banca
        losingPot -= players[player]["bet"] # Restamos la apuesta de este jugador a lo que tendría que pagar la banca si perdiera contra todos
        players[player]["bet"] = 0

        print("{} has too many points and has lost the round!\n Which means that {} has lost {} points, and now has {} points!".format(players[player]["name"],players[player]["name"],players[player]["bet"],players[player]["points"]))
        eliminatingPlayersWith0Points(players,game)

def eliminatingPlayersWith0Points(players,game):
    for player in game:
        if players[player]["points"] == 0:
            print("{} has been eliminated from the game!".format(players[player]["name"]))
            game.remove(player)

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
    elif round == max_rounds:
        print("The maximum number of round has been reached!\nThe winner, with {} points, is {}!!! CONGRATULATIONS!".format(players[game[0]]["points"],players[game[0]]["name"]))
    else:
        print("You have chosen to exit the game.\nThe winner, with {} points, is {}!!! CONGRATULATIONS!".format(players[game[0]]["points"],players[game[0]]["name"]))