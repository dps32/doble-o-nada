import functions.titles as titles
import functions.database as database

ranking = database.getRanking()


def rankingMoreEarnings():
    print("*"*136 + titles.title_more_earnings_centred + "*"*136)
    ranking_earnings = list(ranking.keys())

    if len(ranking_earnings) > 1:
        for sweep in range(len(ranking_earnings) - 1):  # Ordenamos la lista por los earnings
            cambio = False
            for i in range(len(ranking_earnings) - (sweep + 1)):
                if ranking[ranking_earnings[i+1]]["total_gains"] > ranking[ranking_earnings[i]]["total_gains"]:
                    cambio = True
                    aux = ranking_earnings[i+1]
                    ranking_earnings[i+1] = ranking_earnings[i]
                    ranking_earnings[i] = aux
            if not cambio:
                break

    data = "*"*90 + "\n" + "DNI".ljust(15) + "Name".ljust(25) + "Earnings".rjust(15) + "Games Played".rjust(15) + "Minutes Played".rjust(20) + "\n" + "*"*90 + "\n"
    for dni in ranking_earnings:
        data += dni.ljust(15) + ranking[dni]["name"].ljust(25) + str(ranking[dni]["total_gains"]).rjust(15) + str(ranking[dni]["total_games"]).rjust(15) + str(ranking[dni]["total_minutes"]).rjust(20) + "\n"

    print(data)

    input("Enter to continue\n")

def rankingMoreGames():
    print(titles.title_more_games_played)

    ranking_games = list(ranking.keys())

    if len(ranking_games) > 1:
        for sweep in range(len(ranking_games) - 1):  # Ordenamos la lista por los earnings
            cambio = False
            for i in range(len(ranking_games) - (sweep + 1)):
                if ranking[ranking_games[i + 1]]["total_games"] > ranking[ranking_games[i]]["total_games"]:
                    cambio = True
                    aux = ranking_games[i + 1]
                    ranking_games[i + 1] = ranking_games[i]
                    ranking_games[i] = aux
            if not cambio:
                break

    data = "*" * 90 + "\n" + "DNI".ljust(15) + "Name".ljust(25) + "Earnings".rjust(15) + "Games Played".rjust(
        15) + "Minutes Played".rjust(20) + "\n" + "*" * 90 + "\n"
    for dni in ranking_games:
        data += dni.ljust(15) + ranking[dni]["name"].ljust(25) + str(ranking[dni]["total_gains"]).rjust(15) + str(
            ranking[dni]["total_games"]).rjust(15) + str(ranking[dni]["total_minutes"]).rjust(20) + "\n"

    print(data)

    input("Enter to continue\n")

def rankingMoreMinutes():
    print(titles.title_more_minutes_played)

    ranking_minutes = list(ranking.keys())

    if len(ranking_minutes) > 1:
        for sweep in range(len(ranking_minutes) - 1):  # Ordenamos la lista por los earnings
            cambio = False
            for i in range(len(ranking_minutes) - (sweep + 1)):
                if ranking[ranking_minutes[i + 1]]["total_minutes"] > ranking[ranking_minutes[i]]["total_minutes"]:
                    cambio = True
                    aux = ranking_minutes[i + 1]
                    ranking_minutes[i + 1] = ranking_minutes[i]
                    ranking_minutes[i] = aux
            if not cambio:
                break

    data = "*" * 90 + "\n" + "DNI".ljust(15) + "Name".ljust(25) + "Earnings".rjust(15) + "Games Played".rjust(
        15) + "Minutes Played".rjust(20) + "\n" + "*" * 90 + "\n"
    for dni in ranking_minutes:
        data += dni.ljust(15) + ranking[dni]["name"].ljust(25) + str(ranking[dni]["total_gains"]).rjust(15) + str(
            ranking[dni]["total_games"]).rjust(15) + str(ranking[dni]["total_minutes"]).rjust(20) + "\n"

    print(data)

    input("Enter to continue\n")