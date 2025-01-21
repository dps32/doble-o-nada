"""
En este archivo se presentan las funciones utilizadas para la opción 3 (el juego en sí) del menú principal del programa.

Grupo: Doble o Nada
"""

from datetime import datetime
import random
import functions.titles as titles
import functions.database as database


def playGame(game_variables):
    # Se crea una nueva partida indicando la baraja que se utiliza (española (ya sea de 40 o 48) o de poker)
    if game_variables["deck_id"] == 0 or game_variables["deck_id"] == 1:
        gameID = database.newGame(deck = 1)
    else:
        gameID = database.newGame(deck = 2)

    game_variables["game_id"] = gameID
    game_variables["start_time"] = datetime.now().replace(microsecond=0)

    # Añadimos los jugadores a la partida creada
    for player in game_variables["game"]:
        playerID = game_variables["players"][player]["player_id"]
        database.insertPlayerIntoGame(playerID, game_variables["game_id"])

    print("*"*136 + "\n" + titles.title_seven_and_half_centred + "\n" + "*"*136)

    exit = False

    resetPointsInitialCard(game_variables["players"],game_variables["game"])

    # Se jugará mientras haya más de un jugador en la lista de participantes, no se llegue al número máximo de rondas y no se decida salir
    while len(game_variables["game"]) > 1 and game_variables["round"] <= game_variables["max_rounds"] and not exit:
        if game_variables["players"][game_variables["game"][0]]["initialCard"] == "":
            setGamePriority(game_variables)
            game_variables["round"] += 1
        playRound(game_variables)
        exit = exitGame()

    winner(game_variables)
    database.updateGameEndTime(game_variables["game_id"], datetime.now().replace(microsecond=0))

    # Se actualizarán los puntos de los jugadores que tengan más de 20 puntos al final de la partida (se sumarán los puntos finales menos los 20 iniciales)
    for player in game_variables["game"]:
        if game_variables["players"][player]["points"] > 20:
            database.updatePlayerPoints(game_variables["players"][player]["player_id"], game_variables["players"][player]["points"]-20)

    input("Enter to continue\n")

# Le damos a todos los jugadores 20 puntos para empezar, y sitio para guardar la carta inicial
def resetPointsInitialCard(players,game):
    for player in game:
        players[player]["points"] = 20
        players[player]["initialCard"] = ""
    print("\nEvery player has now 20 points to start playing!\n")

# Se establecen las prioridades de los jugadores repartiendo la carta inicial
def setGamePriority(game_variables):
    # Se crea la ronda 0
    roundID = database.newRound(game_variables["game_id"], game_variables["round"])
    game_variables["round_id"] = roundID

    # Se crea un diccionario que almacenará la información de los jugadores de cada ronda
    game_variables["round_players"] = {}
    for player in game_variables["game"]:
        game_variables["round_players"][player] = {}

    game_variables["used_cards"] = [] # En esta lista se guardarán las cartas usadas para que no se repitan en una misma ronda o al repartir la carta inicial

    # Damos la carta inicial a todos los jugadores
    for player in game_variables["game"]:
        index_deck = random.randint(0,len(game_variables["deck"])-1) # Se elige aleatoriamente un indice de la lista
        game_variables["players"][player]["initialCard"] = game_variables["deck"][index_deck] # Se añade como carta inicial del jugador la carta que este en el índice elegido de la lista

        game_variables["used_cards"].append(game_variables["deck"][index_deck]) # Metemos la carta que haya salido en used_cards
        game_variables["deck"].remove(game_variables["deck"][index_deck]) # Lo eliminamos de la lista de deck, para que dos jugadores no puedan tener la misma carta inicial

    game_variables["deck"] += game_variables["used_cards"] # Volvemos a meter en la baraja todas las cartas usadas

    # Ordenamos la lista de jugadores según su prioridad (el primer elemento de la lista ordenada será el de mayor prioridad)
    for sweep in range(len(game_variables["game"]) - 1):
        cambio = False
        for i in range(len(game_variables["game"]) - (sweep + 1)):
            if game_variables["cards"][game_variables["players"][game_variables["game"][i + 1]]["initialCard"]]["value"] < game_variables["cards"][game_variables["players"][game_variables["game"][i]]["initialCard"]]["value"]: #Si el número de la carta inicial del jugador 2 es menor que el del jugador 1, los intercambiamos de sitio
                cambio = True
                aux = game_variables["game"][i + 1]
                game_variables["game"][i + 1] = game_variables["game"][i]
                game_variables["game"][i] = aux
            elif game_variables["cards"][game_variables["players"][game_variables["game"][i + 1]]["initialCard"]]["value"] == game_variables["cards"][game_variables["players"][game_variables["game"][i]]["initialCard"]]["value"]: #Si el número de la carta para dos jugadores es igual, compararemos el palo y su prioridad para desempatar
                if game_variables["cards"][game_variables["players"][game_variables["game"][i + 1]]["initialCard"]]["priority"] < game_variables["cards"][game_variables["players"][game_variables["game"][i]]["initialCard"]]["priority"]:
                    cambio = True
                    aux = game_variables["game"][i + 1]
                    game_variables["game"][i + 1] = game_variables["game"][i]
                    game_variables["game"][i] = aux
        if not cambio:
            break

    # Se imprime una tabla con la información de la carta inicial y la prioridad de cada jugador
    summary = "*" * 60 + "\n" + "Name".center(20) + "Initial Card".center(25) + "Priority".center(20) + "\n" + "*" * 60 + "\n"
    for i in range(len(game_variables["game"])):
        if i == len(game_variables["game"])-1:
            game_variables["players"][game_variables["game"][i]]["bank"] = True  # Al jugador de mayor prioridad, se le establece como banca
        else:
            game_variables["players"][game_variables["game"][i]]["bank"] = False
        game_variables["players"][game_variables["game"][i]]["priority"] = i+1 #Le ponemos a cada jugador su numero de prioridad

        summary += "{}".format(game_variables["players"][game_variables["game"][i]]["name"]).center(20) + "{}".format(game_variables["cards"][game_variables["players"][game_variables["game"][i]]["initialCard"]]["literal"]).center(
            25) + "{}".format(game_variables["players"][game_variables["game"][i]]["priority"]).center(20) + "\n"
    print(summary)
    print("{}, the player with the most priority, is now the Bank!\n".format(game_variables["players"][game_variables["game"][-1]]["name"]))

    # Se introduce la información de los jugadores que han jugado la ronda 0
    for player in game_variables["round_players"]:
        database.insertPlayerRound(game_variables["round_id"],game_variables["players"][player]["bank"],game_variables["players"][player]["player_id"],20,20,0,game_variables["cards"][game_variables["players"][player]["initialCard"]]["card_id"])

    input("Enter to continue\n")

# Función que ejecuta una ronda del juego
def playRound(game_variables):
    # Se crea la ronda en la BBDD
    roundID = database.newRound(game_variables["game_id"], game_variables["round"])
    game_variables["round_id"] = roundID

    # Se crea el diccionario donde se guardará la información de los jugadores que juegan la ronda (información que no cambiará pase lo que pase en la ronda)
    game_variables["round_players"] = {}
    for player in game_variables["game"]:
        game_variables["round_players"][player] = {}


    print("*" * 136 + "\n" + titles.title_seven_and_half_centred + "\n")
    print("Round: {}".format(game_variables["round"]).center(136,"*"))

    for player in game_variables["game"]:
        game_variables["players"][player]["bet"] = 0 # Ponemos a 0 las apuestas de todos los jugadores, así evitamos que la banca de error al no tener bet

    setBet(game_variables,game_variables["players"],game_variables["game"]) # Se establecen las apuestas
    game_variables["used_cards"] = [] # Se reinicia la lista de used_cards

    resettingPlayerRoundValues(game_variables["players"], game_variables["game"]) # Se vacían las listas de cartas de los jugadores y se ponen los roundPoints a 0

    print("\nThe first card of each player is about to be given!\n")
    summary = "*" * 60 + "\n" + "Name".center(20) + "Card".center(25) + "Round Points".center(20) + "\n" + "*" * 60 + "\n"
    for player in game_variables["game"]:
        hitCard(game_variables,player) #Se le da a todos los jugadores la primera carta de la ronda
        summary += "{}".format(game_variables["players"][player]["name"]).center(20) + "{}".format(game_variables["cards"][game_variables["players"][player]["cards"][0]]["literal"]).center(25) + "{}".format(game_variables["players"][player]["roundPoints"]).center(20) + "\n"
    print(summary)
    input("Enter to continue\n")

    for player in game_variables["game"]:
        game_variables["round_players"][player] = {"player_id":game_variables["players"][player]["player_id"],"is_bank":game_variables["players"][player]["bank"],"start_points":game_variables["players"][player]["points"],"end_points":0,"player_bet":game_variables["players"][player]["bet"],"first_card":game_variables["players"][player]["cards"][0]} # Ponemos end_points=0 por si algun jugador es eliminado en la ronda y si no lo es, al recorrer la lista de participantes al final de la ronda se corregirán los puntos finales de la ronda

    # Dependiendo de si el jugador es humano, bot y/o banca se ejecutarán las funciones que definen sus respectivas rondas (ya sea dándoles opciones o imprimiendo mensajes que expliquen las decisiones de los jugadores automatizados)
    for i in range(len(game_variables["game"])):
        if game_variables["players"][game_variables["game"][i]]["bank"]:
            print("*" * 136 + "\n" + titles.title_seven_and_half_centred + "\n" + "*" * 136)
            print("{}'s (BANK) turn (round {})".format(game_variables["players"][game_variables["game"][i]]["name"],game_variables["round"]).center(136,"*") + "\n")
            if game_variables["players"][game_variables["game"][i]]["human"]:
                humanRound(game_variables,game_variables["game"][i])
            else:
                bankRound(game_variables,game_variables["game"][i])
            input("Enter to continue\n")
        else:
            if game_variables["players"][game_variables["game"][i]]["human"]:
                print("*" * 136 + "\n" + titles.title_seven_and_half_centred + "\n" + "*" * 136)
                print("{}'s turn (round {})".format(game_variables["players"][game_variables["game"][i]]["name"],game_variables["round"]).center(136,"*") + "\n")
                humanRound(game_variables,game_variables["game"][i])
                input("Enter to continue\n")
            else:
                print("*" * 136 + "\n" + titles.title_seven_and_half_centred + "\n" + "*" * 136)
                print("{}'s turn (round {})".format(game_variables["players"][game_variables["game"][i]]["name"],game_variables["round"]).center(136,"*") + "\n")
                botRound(game_variables,game_variables["game"][i])
                input("Enter to continue\n")
    # Después de las rondas se hace una primera eliminación de todos aquellos jugadores que ya no tienen puntos
    eliminatingPlayersWith0Points(game_variables)
    # Si queda todavía más de un jugador se reparten los puntos correspondientes, se cambia de banca si es necesario y se vuelven a eliminar jugadores sin puntos
    if len(game_variables["game"]) > 1:
        givePoints_bankCandidates(game_variables)
        input("Enter to continue\n")
        eliminatingPlayersWith0Points(game_variables)

    # Se imprime un resumen de las stats de los jugadores
    showSummaryStats(game_variables["players"],game_variables["game"])

    # Se introducen los jugadores que han jugado la ronda en la BBDD
    for player in game_variables["round_players"]:
        database.insertPlayerRound(game_variables["round_id"],game_variables["round_players"][player]["is_bank"],game_variables["players"][player]["player_id"],game_variables["round_players"][player]["start_points"],game_variables["round_players"][player]["end_points"],game_variables["round_players"][player]["player_bet"],game_variables["cards"][game_variables["round_players"][player]["first_card"]]["card_id"])
    game_variables["deck"] += game_variables["used_cards"] # Resetting the deck

    game_variables["round"] += 1

# Se establecen las apuestas de los jugadores que no son banca; los humanos pueden elegirla o decidir que se determine automáticamente según su perfil de riesgo como en el caso de los bots
# Se guardará una nueva variable en el diccionario de game_variables que acumulará los puntos que la banca debe pagar si todos los jugadores que pueden ganar, ganan
def setBet(game_variables,players,game):
   game_variables["losingPot"] = 0
   for player in game:
       if players[player]["bank"]:
           print("As Bank, {} doesn't have to set a bet.".format(game_variables["players"][player]["name"]))

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
                           bet = int(players[player]["points"]*(players[player]["type"]/100))
                           if bet < 1:
                               bet = 1
                           players[player]["bet"] = bet
                           print("Your bet as {} has been established as {} points.\n".format(players[player]["name"],players[player]["bet"]))
                           game_variables["losingPot"] += players[player]["bet"]
                           input("Enter to continue\n")
                           break
                       elif bet > players[player]["points"]:
                           print("\nInvalid value.")
                           input("Enter to continue\n")
                       else:
                           players[player]["bet"] = bet
                           print("Your bet as {} has been established as {} points.\n".format(players[player]["name"],players[player]["bet"]))
                           game_variables["losingPot"] += bet
                           break

           else:
               bet = int(players[player]["points"]*(players[player]["type"]/100))
               if bet < 1:
                   bet = 1
               players[player]["bet"] = bet
               print("{}'s bet is of {} points.\n".format(players[player]["name"],players[player]["bet"]))
               game_variables["losingPot"] += players[player]["bet"]

   input("Enter to continue\n")
   return

# Ronda de la banca
def bankRound(game_variables,player):
    while mustBankHit(game_variables,player):
        hitCard(game_variables,player)

# Ronda humana; presenta opciones para ver stats, pedir cartas, plantarse o que se juegue la ronda automáticamente
def humanRound(game_variables,player):
    while game_variables["players"][player]["roundPoints"] < 7.5:
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
                viewStats(game_variables["players"],player)
            elif opt == 2:
                viewGameStats(game_variables["players"],game_variables["game"])
            elif opt == 3:
                percentage_risk = calculateRisk(game_variables,player)
                while True:
                    answer = input("You have {:.1f}% chance of exceeding 7,5. Are you sure that you want another card? Y/N ".format(percentage_risk))
                    if not answer.isalpha():
                        print("\nInvalid answer\n")
                    elif answer.upper() == "Y":
                        hitCard(game_variables, player)
                        break
                    elif answer.upper() == "N":
                        break
                    else:
                        print("\nInvalid answer\n")

            elif opt == 4:
                print("\nI stand with {} points!\n".format(game_variables["players"][player]["roundPoints"]))
                break
            else:
                if game_variables["players"][player]["bank"]:
                    bankRound(game_variables,player)
                else:
                    botRound(game_variables,player)
                return
    return

# Ronda de bot
def botRound(game_variables,player):
    while game_variables["players"][player]["roundPoints"] < 7.5:
        if shouldTakeRisk(game_variables,player):
            print("\n{} wants another card.\n".format(game_variables["players"][player]["name"]))
            hitCard(game_variables,player)
        else:
            print("\n{} stands with {} points!\n".format(game_variables["players"][player]["name"],game_variables["players"][player]["roundPoints"]))
            break
    return

# Evaluación de riesgo para todos los jugadores automatizados, devuelve True si el jugador debe pedir carta
def shouldTakeRisk(game_variables,player):
    count = 0
    for card in game_variables["deck"]:
        if game_variables["cards"][card]["realValue"] + game_variables["players"][player]["roundPoints"] > 7.5:
            count += 1    # Contamos las cartas que nos harían perder
    risk = count / len(game_variables["deck"]) * 100    # Calculamos las probabilidades de que salga una carta que nos haga pasarnos
    if game_variables["players"][player]["type"] > risk:
        return True
    print("{} won't take the risk and stands with {} points!".format(game_variables["players"][player]["name"],game_variables["players"][player]["roundPoints"]))
    return False

# Devuelve el porcentaje de riesgo para imprimirlo cuando un humano pide carta
def calculateRisk(game_variables,player):
    count = 0
    for card in game_variables["deck"]:
        if game_variables["cards"][card]["realValue"] + game_variables["players"][player]["roundPoints"] > 7.5:
            count += 1  # Contamos las cartas que nos harían perder
    risk = count / len(game_variables["deck"]) * 100  # Calculamos las probabilidades de que salga una carta que nos haga pasarnos
    return risk

# Se muestran las stats del jugador humano que ha elegido que se muestren
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
    input("Enter to continue\n")

# Se muestran las stats de todos los jugadores
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
    input("Enter to continue\n")

# Se muestran unas stats más resumidas (para cuando acaba una ronda)
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
    input("Enter to continue\n")

# Función que permite añadir una nueva carta aleatoria a la lista de cartas de un jugador cuando éste pide carta
def hitCard(game_variables, player):
    index_deck = random.randint(0, len(game_variables["deck"]) - 1)  # Se elige aleatoriamente un indice de la lista

    game_variables["players"][player]["cards"].append(game_variables["deck"][index_deck])
    game_variables["players"][player]["roundPoints"] += game_variables["cards"][game_variables["deck"][index_deck]]["realValue"]

    if len(game_variables["players"][player]["cards"]) != 1:
        print("{} is {}'s card, which means {} has now {} points!".format(game_variables["players"][player]["cards"][-1],game_variables["players"][player]["name"],game_variables["players"][player]["name"],game_variables["players"][player]["roundPoints"]) + "\n")

    game_variables["used_cards"].append(game_variables["deck"][index_deck])  # Metemos la carta que haya salido en used_cards
    game_variables["deck"].remove(game_variables["deck"][index_deck])  # Lo eliminamos de la lista de deck, para que dos jugadores no puedan sacar en una misma ronda la misma carta

    tooManyPoints(game_variables, player) # Si con esta nueva carta se superan los 7,5 puntos se le quitarán los puntos apostados y se sumarán a la banca
    return

# Devuelve True si la banca debe pedir carta o False si debe plantarse
def mustBankHit(game_variables,player):
    winningPlayers = 0 # Variable que acumulará los jugadores que en la situación actual ganarían a la banca
    for id in game_variables["game"]:
        if game_variables["players"][id]["roundPoints"] > game_variables["players"][player]["roundPoints"]:
            winningPlayers += 1


    if game_variables["players"][player]["roundPoints"] >= 7.5:    # Si la banca ya tiene 7.5 o más
        return False

    if winningPlayers == 0:   # Si no hay jugadores que ganen a la banca
        print("There are no players that can win this round, the Bank stands!")
        return False

    if game_variables["players"][player]["points"] <= game_variables["losingPot"]:   # Si la banca tiene menos puntos que el bote que perdería
        return True

    #La banca no tiene 7,5 ni más, hay jugadores que ganan a la banca y tiene puntos como para pagar las apuestas sin perder
    return shouldTakeRisk(game_variables,player)

# Se reparten los puntos (para los jugadores que no se hayan pasado de 7,5, a excepción de la banca) y el rol de banca si es necesario
def givePoints_bankCandidates(game_variables):
    bankCandidates = []

    for player in game_variables["game"]:
        if game_variables["players"][game_variables["game"][-1]]["roundPoints"] != 7.5: # Si la banca no ha sacado un 7,5
            if game_variables["players"][player]["roundPoints"] == 7.5: # Y otro jugador sí, ganará el doble de puntos y será candidato a la banca
                game_variables["losingPot"] += game_variables["players"][player]["bet"]
                game_variables["players"][player]["bet"] += game_variables["players"][player]["bet"]
                bankCandidates.append(player) # Esta lista ya estará ordenada de menor a mayor prioridad porque la lista game está ordenada así
                print("{} is a Bank Candidate and will earn the double of his bet!!".format(game_variables["players"][player]["name"]))

    if game_variables["players"][game_variables["game"][-1]]["roundPoints"] == 7.5: # Si la banca tiene 7,5, habrá ganado a todos los jugadores (porque en caso de empate, gana la banca)
        game_variables["players"][game_variables["game"][-1]]["points"] += game_variables["losingPot"] # Le sumamos todos los puntos apostados de los jugadores que no se habían pasado de 7,5

        for player in game_variables["game"]:
            if game_variables["players"][player]["bet"] != 0:
                game_variables["players"][player]["points"] -= game_variables["players"][player]["bet"] # Le restamos los puntos apostados a todos los jugadores a los que no se les haya restado ya
        print("The Bank, {}, has defeated everyone in this round and now has {} points.".format(game_variables["players"][game_variables["game"][-1]]["name"],game_variables["players"][game_variables["game"][-1]]["points"]))
    elif game_variables["players"][game_variables["game"][-1]]["roundPoints"] > 7.5: # Si la banca se ha pasado de 7,5 perderá contra todos los jugadores que no se hayan pasado
        if game_variables["players"][game_variables["game"][-1]]["points"] >= game_variables["losingPot"]: # Si tiene puntos para pagar las apuestas de todos los jugadores así se hará
            game_variables["players"][game_variables["game"][-1]]["points"] -= game_variables["losingPot"]
            print("The Bank, {}, has lost {} points and now has {} points.".format(game_variables["players"][game_variables["game"][-1]]["name"],game_variables["losingPot"],game_variables["players"][game_variables["game"][-1]]["points"]))
            for i in range(len(game_variables["game"])-2,-1,-1):
                if game_variables["players"][game_variables["game"][i]]["roundPoints"] <= 7.5:
                    game_variables["players"][game_variables["game"][i]]["points"] += game_variables["players"][game_variables["game"][i]]["bet"]
                    print("{} has won {} points, and now has {} points!".format(game_variables["players"][game_variables["game"][i]]["name"],game_variables["players"][game_variables["game"][i]]["bet"],game_variables["players"][game_variables["game"][i]]["points"]))
        else: # Si no tiene suficientes puntos, se darán puntos empezando por los jugadores de mayor prioridad (empezando por el final de la lista game sin contar la banca)
            while game_variables["players"][game_variables["game"][-1]]["points"] > 0:
                for i in range(len(game_variables["game"]) - 2, -1, -1):
                    if game_variables["players"][game_variables["game"][i]]["roundPoints"] <= 7.5:
                        if game_variables["players"][game_variables["game"][i]]["bet"] < game_variables["players"][game_variables["game"][-1]]["points"]: # Si tiene suficientes puntos para pagar la apuesta del jugador -i de la lista, se pagará al completo
                            game_variables["players"][game_variables["game"][-1]]["points"] -= game_variables["players"][game_variables["game"][i]]["bet"]
                            game_variables["players"][game_variables["game"][i]]["points"] += game_variables["players"][game_variables["game"][i]]["bet"]
                            print("{} has won {} points, and now has {} points!\nSo the Bank has lost {} points and now has {} points.".format(game_variables["players"][game_variables["game"][i]]["name"],
                                                                                    game_variables["players"][game_variables["game"][i]]["bet"],
                                                                                    game_variables["players"][game_variables["game"][i]]["points"],game_variables["players"][game_variables["game"][i]]["bet"],game_variables["players"][game_variables["game"][-1]]["points"]))
                        elif game_variables["players"][game_variables["game"][i]]["bet"] == game_variables["players"][game_variables["game"][-1]]["points"]: # Si tiene solo los puntos para pagar esa apuesta, se darán y se indicará que el banco no puede pagar más apuestas
                            game_variables["players"][game_variables["game"][-1]]["points"] -= game_variables["players"][game_variables["game"][i]]["bet"]
                            game_variables["players"][game_variables["game"][i]]["points"] += game_variables["players"][game_variables["game"][i]]["bet"]
                            print("{} has won {} points, and now has {} points!\nThe Bank has ran out of points, if any other character had to receive points, they won't.".format(
                                game_variables["players"][game_variables["game"][i]]["name"],
                                game_variables["players"][game_variables["game"][i]]["bet"],
                                game_variables["players"][game_variables["game"][i]]["points"]))
                            break
                        else: # Si tiene menos puntos de los necesarios, se darán los que le queden y se informará de que el banco no puede pagar más apuestas
                            game_variables["players"][game_variables["game"][i]]["points"] += game_variables["players"][game_variables["game"][-1]]["points"]

                            print("The bank didn't have enough points.\n{} has won {} points, and now has {} points!\nIf any other player had to receive points, they won't.".format(
                                    game_variables["players"][game_variables["game"][i]]["name"],
                                    game_variables["players"][game_variables["game"][-1]]["points"],
                                    game_variables["players"][game_variables["game"][i]]["points"]))

                            game_variables["players"][game_variables["game"][-1]]["points"] = 0
                            break
    else: # Si la banca tiene menos de 7,5 se evaluará jugador por jugador si ha ganado contra ése o no, pagando o recibiendo los puntos correspondientes
        for i in range(len(game_variables["game"]) - 2, -1, -1):
            if game_variables["players"][game_variables["game"][i]]["bet"] != 0: # Solo se evaluarán aquellos jugadores que tengan una apuesta diferente de 0 (aquellos que se pasaron de 7,5 y ya pagaron su deuda)
                if game_variables["players"][game_variables["game"][-1]]["roundPoints"] < game_variables["players"][game_variables["game"][i]]["roundPoints"]: # En el caso de que la banca tenga menos puntos que el otro jugador (gana el jugador)
                    if game_variables["players"][game_variables["game"][-1]]["points"] > game_variables["players"][game_variables["game"][i]]["bet"]: # Si la banca tiene más puntos de los que debe pagar
                        game_variables["players"][game_variables["game"][i]]["points"] += game_variables["players"][game_variables["game"][i]]["bet"]
                        game_variables["players"][game_variables["game"][-1]]["points"] -= game_variables["players"][game_variables["game"][i]]["bet"]
                        print("{} has won {} points, and now has {} points!\nSo the Bank has lost {} points and now has {} points.".format(
                                game_variables["players"][game_variables["game"][i]]["name"],
                                game_variables["players"][game_variables["game"][i]]["bet"],
                                game_variables["players"][game_variables["game"][i]]["points"],
                                game_variables["players"][game_variables["game"][i]]["bet"],
                                game_variables["players"][game_variables["game"][-1]]["points"]))
                    elif game_variables["players"][game_variables["game"][-1]]["points"] == game_variables["players"][game_variables["game"][i]]["bet"]: # Si la banca tiene los mismos puntos que tiene que pagar
                        game_variables["players"][game_variables["game"][i]]["points"] += game_variables["players"][game_variables["game"][i]]["bet"]
                        game_variables["players"][game_variables["game"][-1]]["points"] = 0
                        print("{} has won {} points, and now has {} points!\nThe Bank has ran out of points, if any other character had to receive points, they won't.".format(
                                game_variables["players"][game_variables["game"][i]]["name"],
                                game_variables["players"][game_variables["game"][i]]["bet"],
                                game_variables["players"][game_variables["game"][i]]["points"]))
                        break
                    else: # Si la banca tiene menos puntos de los que tiene que pagar
                        game_variables["players"][game_variables["game"][i]]["points"] += game_variables["players"][game_variables["game"][-1]]["points"]

                        print("The Bank didn't have enough points.\n{} has won {} points, and now has {} points!\nThe rest of the players won't receive any points.".format(
                                game_variables["players"][game_variables["game"][i]]["name"],
                                game_variables["players"][game_variables["game"][-1]]["points"],
                                game_variables["players"][game_variables["game"][i]]["points"]))

                        game_variables["players"][game_variables["game"][-1]]["points"] = 0
                        break
                elif game_variables["players"][game_variables["game"][-1]]["roundPoints"] > game_variables["players"][game_variables["game"][i]]["roundPoints"]: # En el caso de que la banca tenga más puntos que el otro jugador (gana la banca)
                    game_variables["players"][game_variables["game"][-1]]["points"] += game_variables["players"][game_variables["game"][i]]["bet"]
                    game_variables["players"][game_variables["game"][i]]["points"] -= game_variables["players"][game_variables["game"][i]]["bet"]

                    print("The Bank, {}, has won {} points and now has {} points and {} has lost {} points and now has {} points.".format(game_variables["players"][game_variables["game"][-1]]["name"],game_variables["players"][game_variables["game"][i]]["bet"],game_variables["players"][game_variables["game"][-1]]["points"],game_variables["players"][game_variables["game"][i]]["name"],game_variables["players"][game_variables["game"][i]]["bet"],game_variables["players"][game_variables["game"][i]]["points"]))
                else: # En el caso de que la banca y el otro jugador tengan los mismo puntos (gana la banca)
                    game_variables["players"][game_variables["game"][-1]]["points"] += game_variables["players"][game_variables["game"][i]]["bet"]
                    game_variables["players"][game_variables["game"][i]]["points"] -= game_variables["players"][game_variables["game"][i]]["bet"]

                    print("The Bank, {}, has won {} points and now has {} points and {} has lost {} points and now has {} points.".format(game_variables["players"][game_variables["game"][-1]]["name"],game_variables["players"][game_variables["game"][i]]["bet"],game_variables["players"][game_variables["game"][-1]]["points"],game_variables["players"][game_variables["game"][i]]["name"],game_variables["players"][game_variables["game"][i]]["bet"],game_variables["players"][game_variables["game"][i]]["points"]))


    if len(bankCandidates) != 0: # Si hay candidatos a la banca
        if game_variables["players"][game_variables["game"][-1]]["points"] == 0: # Y la banca actual debe ser eliminada
            print("{}, who was the Bank, has been eliminated!".format(game_variables["players"][game_variables["game"][-1]]["name"]))

            database.updatePlayerGameTime(game_variables["players"][game_variables["game"][-1]]["player_id"], ((datetime.now().replace(microsecond=0) - game_variables["start_time"]).total_seconds() // 60))
            game_variables["game"].remove(game_variables["game"][-1]) # Eliminamos a la banca de la lista de jugadores


            game_variables["players"][bankCandidates[-1]]["bank"] = True  #Ponemos al jugador más prioritario de la lista de candidatos como banca
            print("{} is now the Bank!".format(game_variables["players"][bankCandidates[-1]]["name"]))
            game_variables["game"].remove(bankCandidates[-1]) # Y lo quitamos de la lista de jugadores para añadirlo al final
            game_variables["game"].append(bankCandidates[-1])

        else: # Si la banca actual puede seguir jugando aunque sin ser banca
            game_variables["players"][game_variables["game"][-1]]["bank"] = False # Cambiamos el status del jugador que era banca y del jugador más prioritario de la lista de candidatos
            game_variables["players"][bankCandidates[-1]]["bank"] = True
            print("{} is no longer the Bank. Now it is {}!".format(game_variables["players"][game_variables["game"][-1]]["name"],game_variables["players"][bankCandidates[-1]]["name"]))

            game_variables["game"].remove(bankCandidates[-1]) # Quitamos a la nueva banca de la lista de jugadores para después de ordenar la lista, añadirlo al final

            for sweep in range(len(game_variables["game"]) - 1): # Ordenamos la lista según las prioridades de los jugadores
                cambio = False
                for i in range(len(game_variables["game"]) - (sweep + 1)):
                    if game_variables["players"][game_variables["game"][i + 1]]["priority"] < game_variables["players"][game_variables["game"][i]]["priority"]:  # Si el número de prioridad del jugador 2 es menor que el del jugador 1, los intercambiamos de sitio
                        cambio = True
                        aux = game_variables["game"][i + 1]
                        game_variables["game"][i + 1] = game_variables["game"][i]
                        game_variables["game"][i] = aux
                if not cambio:
                    break

            game_variables["game"].append(bankCandidates[-1]) # Añadimos a la nueva banca al final

    else: # Si no hay candidatos a la banca
        if game_variables["players"][game_variables["game"][-1]]["points"] == 0: # Y la banca actual debe ser eliminada
            print("{}, who was the Bank, has been eliminated!".format(game_variables["players"][game_variables["game"][-1]]["name"]))

            database.updatePlayerGameTime(game_variables["players"][game_variables["game"][-1]]["player_id"], ((datetime.now().replace(microsecond=0) - game_variables["start_time"]).total_seconds() // 60))
            game_variables["game"].remove(game_variables["game"][-1]) # Quitamos a la banca de la lista


            game_variables["players"][game_variables["game"][-1]]["bank"] = True # Y el nuevo último jugador de la lista (el más prioritario) pasará a ser banca
            print("{} is now the Bank!".format(game_variables["players"][game_variables["game"][-1]]["name"]))


    for player in game_variables["game"]: # Cambiamos los end_points = 0 por los end_points de los jugadores que siguen jugando (y que por lo tanto no tienen 0 puntos)
        game_variables["round_players"][player]["end_points"] = game_variables["players"][player]["points"]

# Al haber pedido y recibido una nueva carta, se mirará si eso hace que el jugador supere los 7,5 roundPoints
def tooManyPoints(game_variables, player):
    if game_variables["players"][player]["bank"] and game_variables["players"][player]["roundPoints"]>7.5:
        print("The bank, {}, has too many round points and has lost the round!".format(game_variables["players"][player]["name"]))
    else:
        if game_variables["players"][player]["roundPoints"] > 7.5:
            game_variables["players"][player]["points"] -= game_variables["players"][player]["bet"] # Le quitamos los puntos apostados al jugador que ha perdido
            game_variables["players"][game_variables["game"][-1]]["points"] += game_variables["players"][player]["bet"] # Le sumamos los puntos apostados del jugador que ha perdido a la banca

            game_variables["losingPot"] -= game_variables["players"][player]["bet"] # Restamos la apuesta de este jugador a lo que tendría que pagar la banca si perdiera contra todos

            print("{} has too many round points and has lost the round!\nWhich means that {} has lost {} points, and now has {} points!\nTherefore, {}, the Bank, now has {} points!".format(game_variables["players"][player]["name"],game_variables["players"][player]["name"],game_variables["players"][player]["bet"],game_variables["players"][player]["points"],game_variables["players"][game_variables["game"][-1]]["name"],game_variables["players"][game_variables["game"][-1]]["points"]))
            game_variables["players"][player]["bet"] = 0
    return

# Función que elimina los jugadores que tengan 0 puntos y que actualizan los minutos jugados de esos jugadores
def eliminatingPlayersWith0Points(game_variables):
    for player in game_variables["game"]:
        if game_variables["players"][player]["points"] == 0:
            print("{} has been eliminated from the game!".format(game_variables["players"][player]["name"]))

            database.updatePlayerGameTime(game_variables["players"][player]["player_id"], ((datetime.now().replace(microsecond=0) - game_variables["start_time"]).total_seconds() // 60))
            game_variables["game"].remove(player)


# Vacía la lista de cartas de los jugadores para una nueva ronda y restablece los puntos de ronda a 0
def resettingPlayerRoundValues(players,game):
    for player in game:
        players[player]["cards"] = []
        players[player]["roundPoints"] = 0

# Opción que se ejecuta al acabar cada ronda para ver si se quiere seguir jugando o se quiere abandonar el juego
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

# Imprime el ganador (ya sea porque no quedan más jugadores, se ha alcanzado el máximo de ronda o se ha decidido abandonar la partida)
def winner(game_variables):
    if len(game_variables["game"]) == 1:
        print("{} has won with {} points after {} rounds!!! CONGRATULATIONS!".format(game_variables["players"][game_variables["game"][0]]["name"],game_variables["players"][game_variables["game"][0]]["points"],game_variables["round"]-1))
    else:
        #Si se ha llegado al máximo de rondas o hemos elegido abandonar el juego, se ordenará la lista para dejar en primera posición al jugador con más puntos
        for sweep in range(len(game_variables["game"]) - 1):
            cambio = False
            for i in range(len(game_variables["game"]) - (sweep + 1)):
                if game_variables["players"][game_variables["game"][i + 1]]["points"] > game_variables["players"][game_variables["game"][i]]["points"]:  # Si el jugador 2 tiene más puntos que el jugador 1, los intercambiamos de sitio
                    cambio = True
                    aux = game_variables["game"][i + 1]
                    game_variables["game"][i + 1] = game_variables["game"][i]
                    game_variables["game"][i] = aux
                elif game_variables["players"][game_variables["game"][i + 1]]["points"] == game_variables["players"][game_variables["game"][i]]["points"]:
                    if game_variables["players"][game_variables["game"][i + 1]]["priority"] > game_variables["players"][game_variables["game"][i]]["priority"]:
                        cambio = True
                        aux = game_variables["game"][i + 1]
                        game_variables["game"][i + 1] = game_variables["game"][i]
                        game_variables["game"][i] = aux
            if not cambio:
                break
        if game_variables["round"] == game_variables["max_rounds"]:
            print("The maximum number of rounds has been reached!\nThe winner, with {} points, is {}!!! CONGRATULATIONS!".format(game_variables["players"][game_variables["game"][0]]["points"],game_variables["players"][game_variables["game"][0]]["name"]))
        else:
            print("You have chosen to exit the game.\nThe winner, with {} points, is {}!!! CONGRATULATIONS!".format(game_variables["players"][game_variables["game"][0]]["points"],game_variables["players"][game_variables["game"][0]]["name"]))