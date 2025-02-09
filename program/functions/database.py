"""
En este archivo se presentan las funciones utilizadas para la conexión a la BBDD alojada en Azure,
así como también para su modificación, para obtener datos alojados, entre otros.
Las únicas funciones que permiten obtiener datos de la BBDD y no se encuentran en este archivo son
las necesarias para los reportes (opción 5 del menú principal) y que se encuentran incluidas en el archivo
de las funciones de la opción 5.

Grupo: Doble o Nada
"""

import mysql.connector
from mysql.connector import Error

def getConnection():
    try:
        # datos de conexión
        connection = mysql.connector.connect(
            host='68.221.249.24',
            user='adminsql',
            password='Dani_cris_monica',
            database='sieteymedio'
        )

        if connection.is_connected():
            # print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar la base de datos: {e}")
        return None


def query(query, params=None):
    connection = getConnection()
    if connection is None:
        print("Algo ha fallado al conectarse a la base de datos.")
        return None

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)  # params para consultas con parámetros
            if query.lower().startswith("select"):
                columns = [column[0] for column in cursor.description]
                # convertir filas en diccionarios
                results = cursor.fetchall()
                return [dict(zip(columns, row)) for row in results]
            else:
                connection.commit()  # confirmar cambios
                return cursor.lastrowid  # devolver el id de la última fila insertada
                # print("Consulta ejecutada correctamente")
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        connection.close()  # Asegurarse de cerrar la conexión


# 1 - Española 48
# 2 - Española 40
# 3 - Poker
def getCards(id):
    if id == 1:
        cards = query("SELECT * FROM cards WHERE deck_id = 1")
    elif id == 2:
        cards = query("SELECT * FROM cards WHERE deck_id = 1 AND (value < 8 OR value > 9)")
    elif id == 3:
        cards = query("SELECT * FROM cards WHERE deck_id = 2")
    
    result = {}
    for card in cards:
        lastSpace = card['name'].rfind(' ') # pillar la posición del último espacio
        letter = card['name'][lastSpace + 1] # pillar la primera letra de la última palabra

        if int(card['value']) < 10: # añadimmos un 0 para las cartas de un dígito
            value = "0"+ str(card['value'])
        else:
            value = str(card['value'])
        key = letter + value # clave de la carta

        # print(card)
        result[key] = {"card_id": card['card_id'], "literal": card['name'], "value": card['value'], "priority": card['priority'], "realValue": card['real_value']}
    
    return result

# devuelve un diccionario con los jugadores que hay en la BBDD
def getPlayers():
    players = query("SELECT * FROM players WHERE deleted = 0")

    result = {}

    for player in players:
        human = player['is_ai'] == 0 # cambiamos los valores de human a bools
        result[player['dni']] = {"player_id": player['player_id'], "name": player['name'], "human": human, "type": player['risk_level']}
    return result


# devuelve la id de la inserción
def insertPlayer(dni, name, risk_level, is_ai):
    return query("INSERT INTO players (dni, name, risk_level, is_ai) VALUES (%s, %s, %s, %s)", (dni, name, risk_level, is_ai))


# 1 - española
# 2 - poker
# devuelve la id de la inserción
# debe crearse al iniciar una partida
def newGame(deck = 1):
    return query("INSERT INTO games (deck_id) VALUES (%s)", (deck,))

# insertar un jugador en una partida
# devuelve la id de la inserción
def insertPlayerIntoGame(playerId, gameId):
    return query("INSERT INTO game_players (player_id, game_id) VALUES (%s, %s)", (playerId, gameId))

# crear una nueva ronda
# gameId: id de la partida
# roundNumber: número de ronda en esa partida
def newRound(gameId, roundNumber):
    return query("INSERT INTO rounds (game_id, round_number) VALUES (%s, %s)", (gameId, roundNumber))


# insertar un jugador en una ronda
# se debe insertar al final de cada ronda por cada jugador que ha jugado en esa ronda
def insertPlayerRound(round_id, is_bank, player_id, start_points, end_points, player_bet, first_card_in_hand):
    return query("INSERT INTO player_rounds (round_id, is_bank, player_id, start_points, end_points, player_bet, first_card_in_hand) VALUES (%s, %s, %s, %s, %s, %s, %s)", (round_id, is_bank, player_id, start_points, end_points, player_bet, first_card_in_hand))


# actualizar el tiempo de juego de un jugador
# playerId: id del jugador
# minutes: minutos a añadir
def updatePlayerGameTime(playerId, minutes):
    return query("UPDATE players SET time = time + %s WHERE player_id = %s", (minutes, playerId))


# actualizar la fecha en la que la partida ha terminado
def updateGameEndTime(gameId, endTime):
    return query("UPDATE games SET end_time = %s WHERE game_id = %s", (endTime, gameId))


# actualizar la cantidad de puntos del ranking
# hay que pasar la cantidad a sumar a su puntuación total
def updatePlayerPoints(playerId, points):
    return query("UPDATE players SET points = points + %s WHERE player_id = %s", (points, playerId))


# borra a un jugador de la base de datos
def deletePlayer(dni):
    return query("UPDATE players SET deleted = 1 WHERE dni = %s", (dni,))

# saca el ranking de la base de datos
def getRanking():
    ranking = query("SELECT * FROM players_ranking")
    result = {}

    for entry in ranking:
        nif = query("SELECT dni FROM players WHERE player_id = %s",(entry['player_id'],)) # consigue el DNI de los jugadores que hay en el ranking (a partir de sus IDs)
        nif = nif[0]['dni']
        result[nif] = {"name":entry['player_name'],"total_gains":entry['total_gains'],"total_games":entry['total_games'],"total_minutes":entry['total_minutes_played']}

    return result
