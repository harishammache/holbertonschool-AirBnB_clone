from datetime import datetime, date, time


def now_date(): #affiche la date et l'heure actuel
    now = datetime.now()
    print(now)

now_date()

def ajd_date(): #affiche la date actuel
    now_date = datetime.now().date()
    print(now_date)

ajd_date()

def date_anniversaire(): #afficher une date souhaité
    anniversaire_date = date(1995, 12, 20)
    print(anniversaire_date)

date_anniversaire()

def date_formatage(): #affiche la date et l'heure dans le format souhaité
    now = datetime.now()
    formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
    print(formatted_date)

date_formatage()



