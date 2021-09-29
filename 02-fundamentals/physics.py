'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''
import math

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu
CIRCUMFERENCE_OF_THE_EARTH = 40075
CIRCUMFERENCE_OF_THE_SUN =  4379000


''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
import math
def casARychlostDopadu():
    """
    Funkce, která vypočítá čas a rychlost v okamžiku dopadu, za uživatelem zadenou výšku.
    """
    print(casARychlostDopadu.__doc__)
    logicka = 0
    moznost = input('Pro gravitaci na zemi, zadej 1; pro gravitaci na měsíci, zadej 2: ')
    while(logicka !=1):
        if(int(moznost) == 1):
            vyska = input('Zadej výšku ze které bude těleso padat(m): ')
            vysledekCasu = math.sqrt((2*float(vyska)/EARTH_GRAVITY))
            vysledekRychlosti = math.sqrt(2*EARTH_GRAVITY*float(vyska))
            print(f'Objekt bude padat {vysledekCasu:.2f} sekund')
            print(f'Rychlost v moment dopadu bude {vysledekRychlosti:.2f} m/s')
            logicka = 1
        elif(int(moznost) == 2):
            vyska = input('Zadej výšku ze které bude těleso padat(m): ')
            vysledekCasu = math.sqrt((2 * float(vyska) / MOON_GRAVITY))
            vysledekRychlosti = math.sqrt(2 * MOON_GRAVITY * float(vyska))
            print(f'Objekt bude padat {vysledekCasu:.2f} sekund')
            print(f'Rychlost v moment dopadu bude {vysledekRychlosti:.2f} m/s')
            logicka = 1
        else:
            moznost = input('Nezadal jste číslo z výběru, zkuste to znovu. Pro gravitaci na zemi, zadej 1; pro gravitaci na měsíci, zadej 2: ')


def vzdalenostZaCas():
    """
    Funkce, která vypočítá dráhu světla a zvuku, za uživatelem zadaný čas.
    """
    print(vzdalenostZaCas.__doc__)
    logicka = 0
    moznost = input('Rychlost světla = 1; rychlost zvuku = 2: ')
    while (logicka != 1):
        if (int(moznost) == 1):
            cas = input('Zadejte jak dlouho světlo \"poletí\" (s): ')
            vysledekVzdalenostiVM = float(cas) * SPEED_OF_LIGHT
            vysledekVzdalenostiVKM = vysledekVzdalenostiVM / 1000
            pocetObehuZeme = vysledekVzdalenostiVKM / CIRCUMFERENCE_OF_THE_EARTH
            pocetObehuSlunce = vysledekVzdalenostiVKM / CIRCUMFERENCE_OF_THE_SUN
            print(f'Světlo bude {vysledekVzdalenostiVM:.2f} m daleko.')
            print(f'Světlo bude {vysledekVzdalenostiVKM:.2f} km daleko.')
            print(f'Světlo oběhne Zemi {pocetObehuZeme:.3f} krát!')
            print(f'Světlo oběhne Slunce {pocetObehuSlunce:.3f} krát!')
            logicka = 1
        elif (int(moznost) == 2):
            cas = input('Zadejte jak dlouho zvuk \"poletí\" (min): ')
            vysledekVzdalenostiVM = float(cas) * SPEED_OF_SOUND * 60
            vysledekVzdalenostiVKM = vysledekVzdalenostiVM / 1000
            pocetObehuZeme = vysledekVzdalenostiVKM / CIRCUMFERENCE_OF_THE_EARTH
            pocetObehuSlunce = vysledekVzdalenostiVKM / CIRCUMFERENCE_OF_THE_SUN
            print(f'Zvuk bude {vysledekVzdalenostiVM:.2f} m daleko.')
            print(f'Zvuk bude {vysledekVzdalenostiVKM:.2f} km daleko.')
            print(f'Zvuk oběhne Zemi {pocetObehuZeme:.10f} krát!')
            print(f'Zvuk oběhne Slunce {pocetObehuSlunce:.10f} krát!')
            logicka = 1
        else:
            moznost = input('Nezadal jste číslo z výběru, zkuste to znovu. Rychlost světla = 1; rychlost zvuku = 2:')
