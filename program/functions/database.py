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

        result[key] = {"literal": card['name'], "value": card['value'], "priority": card['priority'], "realValue": card['real_value']}
    
    return result


def getPlayers():
    players = query("SELECT * FROM players")

    result = {}

    for player in players:
        human = player['is_ai'] == 0 # cambiamos los valores de human a bools
        result[player['dni']] = {"name": player['name'], "human": human, "type": player['risk_level']}
    return result