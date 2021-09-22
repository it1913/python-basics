def konec():
    print("Váš finální počet bodů je", body)
    if chyba == 3:
        print("Vaše výsledky jsou neprůkazné, kvůli neschopnosti odpověďet na jedinou otázku.")
    else:
        print("Váš výsledek je:")
        if body == -2:
            print("Jste velmi daleko od prozření.")
        elif body == -1:
            print("Jste daleko od prozření.")
        elif body == 0:
            print("Máte ještě na čem zapracovat.")
        elif body == 1:
            print("Jste na dobré cestě.")
        elif body == 2:
            print("Už jste skoro tam.")
        else:
            print("Jste dobrý občan!")


    hodnoceni = input('Oznámkujte tento dotázník 1 až 5: ')
    while int(hodnoceni) != 1:
        if 6 > int(hodnoceni) > 1:
            print('Zadali jste špatnou známku, zkuste to znovu.')
            hodnoceni = input('Oznámkujte tento dotázník 1 až 5: ')
        elif int(hodnoceni) == 1:
            break
        else:
            print('Nezadal jste číslo v rozmezí.')
            hodnoceni = input('Oznámkujte tento dotázník 1 až 5: ')
    print('Oh, to jsem nečekal.')

print("Jste řádný občan? Projděte tímto dotazníkem a zjistíte odpověď!")
body = 0
chyba = 0
volba = input('Půjdete volit? ano/ne:')
odpoved = volba.strip()
if odpoved.lower() == "ano":
    print("Dostáváte 1 bod")
    body += 1
elif odpoved.lower() == "ne":
    print("Dostáváte 0 bodů")
else:
    print("Špatně zadaná odpověď, přeskakujeme k další otázce.")
    chyba += 1

volba = input('Pokud půjdete volit, kdo bude Vaše volba? ANO/SPD/KSČM/jiné:')
odpoved = volba.strip()
if odpoved.upper() == "ANO":
    print("Špátná volba -2 body")
    body -= 2
elif odpoved.upper() == "SPD":
    print("Špátná volba -2 body")
    body -= 2
elif odpoved.upper() == "KSČM":
    print("Špátná volba -2 body")
    body -= 2
elif odpoved.lower() == "jiné":
    print("Dobrá volba +1 bod")
    body += 1
else:
    print("Špatně zadaná odpověď, přeskakujeme k další otázce.")
    chyba += 1

volba = input('Jste spokojeni se současnou vládou? ano/ne')
odpoved = volba.strip()
if odpoved.lower() == "ne":
    print("Dostáváte 1 bod")
    body += 1
elif odpoved.lower() == "ano":
    print("Dostáváte 0 bodů")
else:
    print("Špatně zadaná odpověď, přeskakujeme k další otázce.")
    chyba += 1


konec()