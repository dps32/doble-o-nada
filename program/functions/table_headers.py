"""
En este archivo se presentan las cabeceras para las tablas principales de este programa.

Grupo: Doble o Nada
"""

import functions.titles as titles

show_remove_header = "*" * 136 + titles.title_show_remove_centred + "*" * 136 + "\n" + "Select players".center(136,"*") + "\n" + "Bot Players".center(67) + "||" + "Human Players".center(67) \
                 + "\n" + "-" * 136 + "\n" + "ID".ljust(20) + "Name".ljust(27) + "Type".ljust(20) + "||" + " " + "ID".ljust(19) + "Name".ljust(27) + "Type".ljust(20) + "\n" + "*" * 136

show_players_header = "Select players".center(136,"*") + "\n" + "Human Players".center(67) + "||" + "Bot Players".center(67) \
                 + "\n" + "-" * 136 + "\n" + "ID".ljust(20) + "Name".ljust(27) + "Type".ljust(20) + "||" + " " + "ID".ljust(19) + "Name".ljust(27) + "Type".ljust(20) + "\n" + "*" * 136

participants_header = "Current Game Participants".center(60,"*") + "\n" + "ID".ljust(15) + "Name".ljust(15) + "Human".ljust(15) + "Type".ljust(15) + "\n" + "*"*60