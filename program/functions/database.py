import mysql.connector
from mysql.connector import Error

def getConnection():
    try:
        # datos de conexión
        connection = mysql.connector.connect(
            host='dobleonada.mysql.database.azure.com',
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

        if card['value'] < 10: # añadimmos un 0 para las cartas de un dígito
            value = "0"+ str(card['value'])
        key = letter + value # clave de la carta
        print(card)
        result[key] = {"card_id": card['card_id'], "literal": card['name'], "value": card['value'], "priority": card['priority'], "realValue": card['real_value']}
    
    return result


def getPlayers():
    players = query("SELECT * FROM players")

    result = {}

    for player in players:
        human = player['is_ai'] == 0 # cambiamos los valores de human a bools
        result[player['dni']] = {"name": player['name'], "human": human, "type": player['risk_level']}
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
# se debe insertar al final de cada ronda por cada jugador que siga jugando
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
    return query("DELETE FROM players WHERE dni = %s", (dni,))