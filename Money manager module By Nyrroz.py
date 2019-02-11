"""
Money manager simulation script in three accounts: personnal, business, saves/taxes
Credits: Nyrroz
Github: https://github.com/Nyrroz
"""
perso_acct = 0
bus_acct = 0
sav_acct = 0


def acct_updt(perso_acct, bus_acct, sav_acct, money_income):
    money_income = float(money_income)

    perso_acct = (money_income * 34 / 100)
    bus_acct = (money_income * 33 / 100)
    sav_acct = (money_income * 33 / 100)

    print("Personnal Account: " + str(perso_acct))
    print("Business Account " + str(bus_acct))
    print("Saves Account: " + str(sav_acct))
    print("Total Balance: " + str(perso_acct+bus_acct+sav_acct))
    print("\n\n")


while True:
    money_income = input("Money Income: ")
    try:
        acct_updt(perso_acct, bus_acct, sav_acct, money_income)
    except:
        print("Error! please enter a valid number\n\n")
