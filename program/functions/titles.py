"""
En este archivo se presentan las variables que alojan los títulos para el programa una vez han sido
dados el formato adecuado (para ver como se centran estos títulos consultar la función que se encuentra
en el archivo formatting_functions).

Grupo: Doble o Nada
"""

import functions.formatting_functions as formatting

# Títulos en ASCII
main_ascii = """
██████╗░░█████╗░██████╗░██╗░░░░░███████╗  ░█████╗░  ███╗░░██╗░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔════╝  ██╔══██╗  ████╗░██║██╔══██╗██╔══██╗██╔══██╗
██║░░██║██║░░██║██████╦╝██║░░░░░█████╗░░  ██║░░██║  ██╔██╗██║███████║██║░░██║███████║
██║░░██║██║░░██║██╔══██╗██║░░░░░██╔══╝░░  ██║░░██║  ██║╚████║██╔══██║██║░░██║██╔══██║
██████╔╝╚█████╔╝██████╦╝███████╗███████╗  ╚█████╔╝  ██║░╚███║██║░░██║██████╔╝██║░░██║
╚═════╝░░╚════╝░╚═════╝░╚══════╝╚══════╝  ░╚════╝░  ╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
"""


bbdd_players_ascii = """
██████╗░██████╗░██████╗░██████╗░  ██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗██╔════╝
██████╦╝██████╦╝██║░░██║██║░░██║  ██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝╚█████╗░
██╔══██╗██╔══██╗██║░░██║██║░░██║  ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗░╚═══██╗
██████╦╝██████╦╝██████╔╝██████╔╝  ██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║██████╔╝
╚═════╝░╚═════╝░╚═════╝░╚═════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░
"""
new_human_ascii = """
███╗░░██╗███████╗░██╗░░░░░░░██╗  ██╗░░██╗██╗░░░██╗███╗░░░███╗░█████╗░███╗░░██╗
████╗░██║██╔════╝░██║░░██╗░░██║  ██║░░██║██║░░░██║████╗░████║██╔══██╗████╗░██║
██╔██╗██║█████╗░░░╚██╗████╗██╔╝  ███████║██║░░░██║██╔████╔██║███████║██╔██╗██║
██║╚████║██╔══╝░░░░████╔═████║░  ██╔══██║██║░░░██║██║╚██╔╝██║██╔══██║██║╚████║
██║░╚███║███████╗░░╚██╔╝░╚██╔╝░  ██║░░██║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░  ╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝
██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗
██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""
new_bot_ascii = """
███╗░░██╗███████╗░██╗░░░░░░░██╗  ██████╗░░█████╗░████████╗  ██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░
████╗░██║██╔════╝░██║░░██╗░░██║  ██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
██╔██╗██║█████╗░░░╚██╗████╗██╔╝  ██████╦╝██║░░██║░░░██║░░░  ██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝
██║╚████║██╔══╝░░░░████╔═████║░  ██╔══██╗██║░░██║░░░██║░░░  ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗
██║░╚███║███████╗░░╚██╔╝░╚██╔╝░  ██████╦╝╚█████╔╝░░░██║░░░  ██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░  ╚═════╝░░╚════╝░░░░╚═╝░░░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""
show_remove_ascii = """
░██████╗██╗░░██╗░█████╗░░██╗░░░░░░░██╗░░░░░░██████╗░███████╗███╗░░░███╗░█████╗░██╗░░░██╗███████╗
██╔════╝██║░░██║██╔══██╗░██║░░██╗░░██║░░░░░░██╔══██╗██╔════╝████╗░████║██╔══██╗██║░░░██║██╔════╝
╚█████╗░███████║██║░░██║░╚██╗████╗██╔╝█████╗██████╔╝█████╗░░██╔████╔██║██║░░██║╚██╗░██╔╝█████╗░░
░╚═══██╗██╔══██║██║░░██║░░████╔═████║░╚════╝██╔══██╗██╔══╝░░██║╚██╔╝██║██║░░██║░╚████╔╝░██╔══╝░░
██████╔╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░░░░░░░██║░░██║███████╗██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░███████╗
╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝
██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░░██████╗
██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗██╔════╝
██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝╚█████╗░
██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗░╚═══██╗
██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║██████╔╝
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░
"""


settings_ascii = """
░██████╗███████╗████████╗████████╗██╗███╗░░██╗░██████╗░░██████╗
██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗░██║██╔════╝░██╔════╝
╚█████╗░█████╗░░░░░██║░░░░░░██║░░░██║██╔██╗██║██║░░██╗░╚█████╗░
░╚═══██╗██╔══╝░░░░░██║░░░░░░██║░░░██║██║╚████║██║░░╚██╗░╚═══██╗
██████╔╝███████╗░░░██║░░░░░░██║░░░██║██║░╚███║╚██████╔╝██████╔╝
╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═════╝░
"""
set_game_players_ascii = """
░██████╗███████╗████████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
██╔════╝██╔════╝╚══██╔══╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝
╚█████╗░█████╗░░░░░██║░░░  ██║░░██╗░███████║██╔████╔██║█████╗░░
░╚═══██╗██╔══╝░░░░░██║░░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
██████╔╝███████╗░░░██║░░░  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
╚═════╝░╚══════╝░░░╚═╝░░░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝

██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░░██████╗
██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗██╔════╝
██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝╚█████╗░
██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗░╚═══██╗
██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║██████╔╝
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░
"""
card_deck_ascii = """
░█████╗░░█████╗░██████╗░██████╗░  ██████╗░███████╗░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██║░██╔╝
██║░░╚═╝███████║██████╔╝██║░░██║  ██║░░██║█████╗░░██║░░╚═╝█████═╝░
██║░░██╗██╔══██║██╔══██╗██║░░██║  ██║░░██║██╔══╝░░██║░░██╗██╔═██╗░
╚█████╔╝██║░░██║██║░░██║██████╔╝  ██████╔╝███████╗╚█████╔╝██║░╚██╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝
"""
set_max_rounds_ascii = """
░██████╗███████╗████████╗  ███╗░░░███╗░█████╗░██╗░░██╗  ██████╗░░█████╗░██╗░░░██╗███╗░░██╗██████╗░░██████╗
██╔════╝██╔════╝╚══██╔══╝  ████╗░████║██╔══██╗╚██╗██╔╝  ██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗██╔════╝
╚█████╗░█████╗░░░░░██║░░░  ██╔████╔██║███████║░╚███╔╝░  ██████╔╝██║░░██║██║░░░██║██╔██╗██║██║░░██║╚█████╗░
░╚═══██╗██╔══╝░░░░░██║░░░  ██║╚██╔╝██║██╔══██║░██╔██╗░  ██╔══██╗██║░░██║██║░░░██║██║╚████║██║░░██║░╚═══██╗
██████╔╝███████╗░░░██║░░░  ██║░╚═╝░██║██║░░██║██╔╝╚██╗  ██║░░██║╚█████╔╝╚██████╔╝██║░╚███║██████╔╝██████╔╝
╚═════╝░╚══════╝░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░╚═════╝░
"""


seven_and_half_ascii = """
░██████╗███████╗██╗░░░██╗███████╗███╗░░██╗  ░█████╗░███╗░░██╗██████╗░  ██╗░░██╗░█████╗░██╗░░░░░███████╗
██╔════╝██╔════╝██║░░░██║██╔════╝████╗░██║  ██╔══██╗████╗░██║██╔══██╗  ██║░░██║██╔══██╗██║░░░░░██╔════╝
╚█████╗░█████╗░░╚██╗░██╔╝█████╗░░██╔██╗██║  ███████║██╔██╗██║██║░░██║  ███████║███████║██║░░░░░█████╗░░
░╚═══██╗██╔══╝░░░╚████╔╝░██╔══╝░░██║╚████║  ██╔══██║██║╚████║██║░░██║  ██╔══██║██╔══██║██║░░░░░██╔══╝░░
██████╔╝███████╗░░╚██╔╝░░███████╗██║░╚███║  ██║░░██║██║░╚███║██████╔╝  ██║░░██║██║░░██║███████╗██║░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝  ╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░
"""
stats_ascii = """
░██████╗████████╗░█████╗░████████╗░██████╗
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝
╚█████╗░░░░██║░░░███████║░░░██║░░░╚█████╗░
░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░░╚═══██╗
██████╔╝░░░██║░░░██║░░██║░░░██║░░░██████╔╝
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░
"""


ranking_ascii = """
██████╗░░█████╗░███╗░░██╗██╗░░██╗██╗███╗░░██╗░██████╗░
██╔══██╗██╔══██╗████╗░██║██║░██╔╝██║████╗░██║██╔════╝░
██████╔╝███████║██╔██╗██║█████═╝░██║██╔██╗██║██║░░██╗░
██╔══██╗██╔══██║██║╚████║██╔═██╗░██║██║╚████║██║░░╚██╗
██║░░██║██║░░██║██║░╚███║██║░╚██╗██║██║░╚███║╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
"""
more_earnings_ascii = """
███╗░░░███╗░█████╗░██████╗░███████╗  ███████╗░█████╗░██████╗░███╗░░██╗██╗███╗░░██╗░██████╗░░██████╗
████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔════╝██╔══██╗██╔══██╗████╗░██║██║████╗░██║██╔════╝░██╔════╝
██╔████╔██║██║░░██║██████╔╝█████╗░░  █████╗░░███████║██████╔╝██╔██╗██║██║██╔██╗██║██║░░██╗░╚█████╗░
██║╚██╔╝██║██║░░██║██╔══██╗██╔══╝░░  ██╔══╝░░██╔══██║██╔══██╗██║╚████║██║██║╚████║██║░░╚██╗░╚═══██╗
██║░╚═╝░██║╚█████╔╝██║░░██║███████╗  ███████╗██║░░██║██║░░██║██║░╚███║██║██║░╚███║╚██████╔╝██████╔╝
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═════╝░
"""
more_games_played_ascii = """
███╗░░░███╗░█████╗░██████╗░███████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗░██████╗
████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝██╔════╝
██╔████╔██║██║░░██║██████╔╝█████╗░░  ██║░░██╗░███████║██╔████╔██║█████╗░░╚█████╗░
██║╚██╔╝██║██║░░██║██╔══██╗██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗
██║░╚═╝░██║╚█████╔╝██║░░██║███████╗  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██████╔╝
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░

██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██║░░██║
██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██║░░██║
██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██████╔╝
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░
"""
more_minutes_played_ascii = """
███╗░░░███╗░█████╗░██████╗░███████╗  ███╗░░░███╗██╗███╗░░██╗██╗░░░██╗████████╗███████╗░██████╗
████╗░████║██╔══██╗██╔══██╗██╔════╝  ████╗░████║██║████╗░██║██║░░░██║╚══██╔══╝██╔════╝██╔════╝
██╔████╔██║██║░░██║██████╔╝█████╗░░  ██╔████╔██║██║██╔██╗██║██║░░░██║░░░██║░░░█████╗░░╚█████╗░
██║╚██╔╝██║██║░░██║██╔══██╗██╔══╝░░  ██║╚██╔╝██║██║██║╚████║██║░░░██║░░░██║░░░██╔══╝░░░╚═══██╗
██║░╚═╝░██║╚█████╔╝██║░░██║███████╗  ██║░╚═╝░██║██║██║░╚███║╚██████╔╝░░░██║░░░███████╗██████╔╝
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═════╝░

██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██║░░██║
██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██║░░██║
██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██████╔╝
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░
"""


reports_ascii = """
██████╗░███████╗██████╗░░█████╗░██████╗░████████╗░██████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░╚█████╗░
██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░░╚═══██╗
██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██████╔╝
╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░
"""

# Variables con los títulos centrados
# Título principal
title_main_centred = formatting.titleCentred(main_ascii)

# Títulos para las diferentes acciones de la opción 1 del menú principal.
title_bbdd_players_centred = formatting.titleCentred(bbdd_players_ascii)
title_new_human_centred = formatting.titleCentred(new_human_ascii)
title_new_bot_centred = formatting.titleCentred(new_bot_ascii)
title_show_remove_centred = formatting.titleCentred(show_remove_ascii)

# Títulos para las diferentes acciones de la opción 2 del menú principal.
title_settings_centred = formatting.titleCentred(settings_ascii)
title_set_game_players_centred = formatting.titleCentred(set_game_players_ascii)
title_card_deck_centred = formatting.titleCentred(card_deck_ascii)
title_set_max_rounds_centred = formatting.titleCentred(set_max_rounds_ascii)

# Títulos para el juego (opción 3).
title_seven_and_half_centred = formatting.titleCentred(seven_and_half_ascii)
title_stats_centred = formatting.titleCentred(stats_ascii)

# Títulos para las diferentes acciones de la opción 4 del menú principal.
title_ranking_centred = formatting.titleCentred(ranking_ascii)
title_more_earnings_centred = formatting.titleCentred(more_earnings_ascii)
title_more_games_played = formatting.titleCentred(more_games_played_ascii)
title_more_minutes_played = formatting.titleCentred(more_minutes_played_ascii)

# Título para los reports (opción 5).
title_reports_centred = formatting.titleCentred(reports_ascii)