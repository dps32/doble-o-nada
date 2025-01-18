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


# insertPlayer
# devuelve la id de la inserción
def insertPlayer(dni, name, risk_level, is_ai):
    return query("INSERT INTO players (dni, name, risk_level, is_ai) VALUES (%s, %s, %s, %s)", (dni, name, risk_level, is_ai))


# newGame
# 1 - española
# 2 - poker
# devuelve la id de la inserción
# debe crearse al iniciar una partida
def newGame(deck = 1):
    return query("INSERT INTO games (deck_id) VALUES (%s)", (deck,))

#insertPlayerIntoGame
# insertar un jugador en una partida
# devuelve la id de la inserción
def insertPlayerIntoGame(playerId, gameId):
    return query("INSERT INTO game_players (player_id, game_id) VALUES (%s, %s)", (playerId, gameId))

#newRound
# crear una nueva ronda
# gameId: id de la partida
# roundNumber: número de ronda en esa partida
def newRound(gameId, roundNumber):
    return query("INSERT INTO rounds (game_id, round_number) VALUES (%s, %s)", (gameId, roundNumber))


#insertPlayerRound
# insertar un jugador en una ronda
# se debe insertar al final de cada ronda por cada jugador que siga jugando
def insertPlayerRound(round_id, is_bank, player_id, start_points, end_points, player_bet, first_card_in_hand):
    return query("INSERT INTO player_rounds (round_id, is_bank, player_id, start_points, end_points, player_bet, first_card_in_hand) VALUES (%s, %s, %s, %s, %s, %s, %s)", (round_id, is_bank, player_id, start_points, end_points, player_bet, first_card_in_hand))