import random

lettersNIF = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
def newHuman():
    while True:
        name = input("Name: ")
        if not name.isalpha():
            print("\nInvalid name.\n")
        elif len(name) > 32:
            print("\nThe name is too long.\n")
        else:
            name = name.title()
            break
    while True:
        nif = input("NIF: ")
        if not len(nif) == 9:
            print("\nIncorrect NIF length.\n")
        elif not nif[:-1].isdigit():
            print("\nInvalid NIF\n")
        else:
            if not nif[-1].upper() == lettersNIF[int(nif[:-1]) % 23]:
                print("\nIncorrect DNI letter.\n")
            else:
                break
    while True:
        opt = input("Select your Profile:\n1) Cautious\n2) Moderated\n3) Bold\nOption: ")
        if not opt.isdigit():
            print("\nInvalid option.\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 3:
                print("\nInvalid option.\n")
            elif opt == 1:
                profile = 30
                break
            elif opt == 2:
                profile = 40
                break
            else:
                profile = 50
                break
    while True:
        save = input("Is it ok? (Y/N) ")
        if not save.isalpha():
            print("\nInvalid answer.\n")
        else:
            save = save.upper()
            if save == "Y":
                return nif, name, profile
            elif save == "N":
                return False
            else:
                print("\nInvalid answer.\n")

def newBot():
    while True:
        name = input("Name: ")
        if not name.isalpha():
            print("\nInvalid name.\n")
        elif len(name) > 26:
            print("\nThe name is too long.\n")
        else:
            name = name.title()
            break
    nif = random.randint(10000000,99999999)
    nif = str(nif) + lettersNIF[nif%23]
    print("NIF: ",nif)
    while True:
        opt = input("Select your Profile:\n1) Cautious\n2) Moderated\n3) Bold\nOption: ")
        if not opt.isdigit():
            print("\nInvalid option.\n")
        else:
            opt = int(opt)
            if opt < 1 or opt > 3:
                print("\nInvalid option.\n")
            elif opt == 1:
                profile = 30
                break
            elif opt == 2:
                profile = 40
                break
            else:
                profile = 50
                break
    while True:
        save = input("Is it ok? (Y/N) ")
        if not save.isalpha():
            print("\nInvalid answer.\n")
        else:
            save = save.upper()
            if save == "Y":
                return nif, name, profile
            elif save == "N":
                return False
            else:
                print("\nInvalid answer.\n")

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