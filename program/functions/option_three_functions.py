"""
def setGamePriority(deck):

def resetPoints():

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

def playGame(game,deck,cards):
    print("juego")



# La banca debe pedir carta o plantarse
# bankPoints: puntos de la banca
# cardsValue: valor de las cartas de la banca
# losingPot: el bote que perdería la banca actualmente si se planta
# winningPlayers: cantidad de jugadores que ganan a la banca
# losingPlayers: cantidad de jugadores que pierden a la banca
def mustBankHit(bankPoints, cardsValue, losingPot, winningPlayers, losingPlayers, riskProfile):
    if cardsValue >= 7.5:    # Si la banca ya tiene 7.5 o más
        return False

    if winningPlayers == 0:   # Si no hay jugadores que ganen a la banca
        return False

    if bankPoints <= losingPot:   # Si la banca tiene menos puntos que el bote que perdería
        return True

    if losingPlayers == 0:    # Si no hay jugadores que pierdan a la banca
        return False
    else:    # Si hay jugadores que pierden a la banca probamos el riesgo
        return shouldTakeRisk(bankPoints, cardsValue, riskProfile)


# La banca debe pedir carta o plantarse
# bankPoints: puntos de la banca
# cardsValue: valor de las cartas de la banca
# losingPot: el bote que perdería la banca actualmente si se planta
# winningPlayers: cantidad de jugadores que ganan a la banca
# losingPlayers: cantidad de jugadores que pierden a la banca
def mustBankHit(bankPoints, cardsValue, losingPot, winningPlayers, losingPlayers, riskProfile):
    if cardsValue >= 7.5:    # Si la banca ya tiene 7.5 o más
        return False

    if winningPlayers == 0:   # Si no hay jugadores que ganen a la banca
        return False

    if bankPoints <= losingPot:   # Si la banca tiene menos puntos que el bote que perdería
        return True

    if losingPlayers == 0:    # Si no hay jugadores que pierdan a la banca
        return False
    else:    # Si hay jugadores que pierden a la banca probamos el riesgo
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



def hitCard(player):
    card = random.choice(list(cards.keys()))
    players[player]["cards"].append(card)
    cards.pop(card)
    return True