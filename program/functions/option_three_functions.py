import random
import functions.titles as titles
#REVISAR QUÉ VARIABLES PUEDO PONER COMO GLOBALES (ej. players, cards...)
"""
def setGamePriority(deck):

def fill_player_game(player_game,gameID,*fields):

def fill_player_game_round(player_game_round,round,*fields):

def checkMinimum2PlayerWithPoints():

def orderAllPlayers():

def setBets():

def standardRound(id,deck):

def humanRound(id,deck):

def distributionPointAndNewBankCandidates():

def printStats(idPlayer="",titulo="")
"""

def playGame(players,game,deck,cards,max_rounds):
    round = 0

    resetPoints(players,game) #Le damos a todos los jugadores 20 puntos para empezar

    while len(game) > 1 and round <= max_rounds:
        if players[game[0]]["initialCard"] == "":
            setGamePriority(players,game,deck,cards)
        playRound(players,game,deck,cards)

def resetPoints(players,game):
    for player in game:
        players[player]["points"] = 20


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

    for i in range(len(game)):
        players[game[i]]["priority"] = i+1 #Le ponemos a cada jugador su numero de prioridad

    players[game[-1]]["bank"] = True #Al jugador de mayor prioridad, se le establece como banca


def playRound(players,game,deck,cards):
    setBet(players,game)
    used_cards = []
    for player in game:
        if players[player]["human"] == True:
            humanRound(players,player,game,deck,cards,used_cards)
        else:
            botRound(players, player, game, deck, cards, used_cards)

def setBet(players,game):
   for player in game:
       if players[player]["bank"] == True:
           continue
       else:
           if players[player]["human"] == True:
               while True:
                   bet = input("Set your bet (or put 0 if you want it done automatically): ")
                   if not bet.isdigit():
                       print("\nInvalid value.\n")
                   else:
                       bet = int(bet)
                       if bet == 0:
                           players[player]["bet"] = players[player]["points"]*(players[player]["type"]/100)
                           print("Your bet as {} has been established as {} points.".format(players[player]["name"],players[player]["bet"]))
                           break
                       elif bet > players[player]["points"]:
                           print("\nInvalid value.\n")
                       else:
                           players[player]["bet"] = bet
                           print("Your bet as {} has been established as {} points.".format(players[player]["name"],players[player]["bet"]))
                           break
           else:
               players[player]["bet"] = players[player]["points"]*(players[player]["type"]/100)
               print("{}'s bet is of {} points.".format(players[player]["name"],players[player]["bet"]))

def humanRound(players,player,game,deck,cards,used_cards):
    while True:
        menuHumanRound = "\n1) View Stats\n2) View Game Stats\n3) Hit\n4) Stand\n5) Automatic Play\n"
        opt = input("Option: ")
        if not opt.isdigit():
            print("\nInvalid option\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 5:
                print("\nInvalid option\n")
            else:
                break
    if opt == 1:
        viewStats(players,player)
    elif opt == 2:
        viewGameStats(players,game)
    elif opt == 3:
        hitCard(players,player,deck,cards,used_cards)
    elif opt == 4:
        return
    else:
        botRound(players,player,game,deck,cards,used_cards)


def botRound(players,player,game,deck,cards,used_cards):
    print("bot")

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


def hitCard(players, player, deck, cards, used_cards):
    index_deck = random.randint(0, len(deck) - 1)  # Se elige aleatoriamente un indice de la lista

    players[player]["cards"].append(deck[index_deck])
    players[player]["roundPoints"] += cards[deck[index_deck]]["realValue"]

    used_cards.append(deck[index_deck])  # Metemos la carta que haya salido en used_cards
    deck.remove(deck[index_deck])  # Lo eliminamos de la lista de deck, para que dos jugadores no puedan sacar en una misma ronda la misma carta
    return

# La banca debe pedir carta o plantarse
# bankPoints: puntos de la banca
# cardsValue: valor de las cartas de la banca
# losingPot: el bote que perdería la banca actualmente si se planta
# winningPlayers: cantidad de jugadores que ganan a la banca
# losingPlayers: cantidad de jugadores que pierden a la banca
def mustBankHit(bankPoints, cardsValue, losingPot, winningPlayers, riskProfile):
    if cardsValue >= 7.5:    # Si la banca ya tiene 7.5 o más
        return False

    if winningPlayers == 0:   # Si no hay jugadores que ganen a la banca
        return False

    if bankPoints <= losingPot:   # Si la banca tiene menos puntos que el bote que perdería
        return True

    #La banca no tiene 7,5 ni más, hay jugadores que ganan a la banca y tiene puntos como para pagar las apuestas sin perder
    return shouldTakeRisk(bankPoints, cardsValue, riskProfile)



# Evaluación de riesgo para todos los jugadores, devuelve True si el jugador debe pedir carta
# currentPoints: puntos actuales del jugador
# remainingCards: cartas que quedan por salir
# riskProfile: perfil de riesgo del jugador
def shouldTakeRisk(currentPoints, remainingCards, riskProfile):
    count = 0
    for card in remainingCards:
        if remainingCards[card]["realValue"] + currentPoints > 7.5:
            count += 1    # Contamos las cartas que nos harían perder
    print("Count: ", count)
    risk = count / len(remainingCards) * 100    # Calculamos las probabilidades de que salga una carta que nos haga pasarnos
    print(risk)
    if riskProfile > risk:
        return True
    return False



