import functions.database as database
import functions.titles as titles


def report1():
    print("*" * 136 + titles.title_reports_centred + "*" * 136)
    report1 = database.query("SELECT * FROM player_initial_card_statistics")

    data = "*" * 80 + "\n" + "DNI".ljust(10) + "Name".ljust(15) + "Suit".rjust(10) + "Initial Card".rjust(
        15) + "Times Repeated".rjust(15) + "Total Games".rjust(15) + "\n" + "*" * 80 + "\n"

    for entry in report1:
        nif = database.query("SELECT dni FROM players WHERE player_id = %s", (entry['player_id'],))
        nif = nif[0]['dni']
        data += nif.ljust(10) + entry['player_name'].ljust(15) + entry['suit'].rjust(10) + entry['initial_card_name'].rjust(15) + entry['times_repeated'].rjust(15) + entry['total_games'].rjust(15) + "\n"

    print(data)
    input("Enter to continue\n")

def report2():
    print("*" * 136 + titles.title_reports_centred + "*" * 136)
    report2 = database.query("SELECT * FROM highest_bet_per_game")

    data = "*" * 35 + "\n" + "Game ID".ljust(10) + "DNI".ljust(10) + "Highest bet".rjust(15) + "\n" + "*" * 35 + "\n"

    for entry in report2:
        nif = database.query("SELECT dni FROM players WHERE player_id = %s", (entry['player_id'],))
        nif = nif[0]['dni']
        data += str(entry['game_id']).ljust(10) + nif.ljust(10) + str(entry['highest_bet']).rjust(15) + "\n"

    print(data)
    input("Enter to continue\n")

def report3():
    print("*" * 136 + titles.title_reports_centred + "*" * 136)
    report3 = database.query("SELECT * FROM lowest_bet_per_game")

    data = "*" * 35 + "\n" + "Game ID".ljust(10) + "DNI".ljust(10) + "Lowest bet".rjust(15) + "\n" + "*" * 35 + "\n"

    for entry in report3:
        nif = database.query("SELECT dni FROM players WHERE player_id = %s", (entry['player_id'],))
        nif = nif[0]['dni']
        data += str(entry['game_id']).ljust(10) + nif.ljust(10) + str(entry['lowest_bet']).rjust(15) + "\n"

    print(data)
    input("Enter to continue\n")

def report7():
    print("*" * 136 + titles.title_reports_centred + "*" * 136)
    report7 = database.query("SELECT * FROM bank_users_per_game")

    data = "*" * 25 + "\n" + "Game ID".ljust(10) + "Bank Users".rjust(15) + "\n" + "*" * 25 + "\n"

    for entry in report7:
        data += str(entry['game_id']).ljust(10) + str(entry['bank_users_count']).rjust(15) + "\n"

    print(data)
    input("Enter to continue\n")

def report8():
    print("*" * 136 + titles.title_reports_centred + "*" * 136)
    report8 = database.query("SELECT * FROM average_bet_per_game")

    data = "*" * 25 + "\n" + "Game ID".ljust(10) + "Average Bet".rjust(15) + "\n" + "*" * 25 + "\n"

    for entry in report8:
        data += str(entry['game_id']).ljust(10) + str(entry['average_bet']).rjust(15) + "\n"

    print(data)
    input("Enter to continue\n")

def report9():
    print("*" * 136 + titles.title_reports_centred + "*" * 136)
    report9 = database.query("SELECT * FROM average_first_round_bet")

    data = "*" * 40 + "\n" + "Game ID".ljust(10) + "Average Bet (1st Round)".rjust(30) + "\n" + "*" * 40 + "\n"

    for entry in report9:
        data += str(entry['Game ID']).ljust(10) + str(entry['Average Bet (First Round)']).rjust(30) + "\n"

    print(data)
    input("Enter to continue\n")

def report10():
    print("*" * 136 + titles.title_reports_centred + "*" * 136)
    report10 = database.query("SELECT * FROM average_last_round_bet")

    data = "*" * 40 + "\n" + "Game ID".ljust(10) + "Average Bet (Last Round)".rjust(30) + "\n" + "*" * 40 + "\n"

    for entry in report10:
        data += str(entry['Game ID']).ljust(10) + str(entry['Average Bet (Last Round)']).rjust(30) + "\n"

    print(data)
    input("Enter to continue\n")