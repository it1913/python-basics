'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''

film= {
  'film_1': {
    'name': 'No Time to Die (James Bond)',
    'year': 2021,
    'genre': {"Akční", "Dobrodružný"},
    'isInCinema': True,
    'directors': ("Cary Fukunaga", "USA"),
    'actors': ["Daniel Craig", "Ralph Fiennes", "Léa Seydouxová", "Rami Malek", "Ana de Armasová"]
  },
  'film_2' : {
    'name': 'Kingsman: První mise',
    'year': 2021,
    'genre': {"Akční", "Komedie"},
    'isInCinema': False,
    'directors': ("Matthew Vaughn", "Velká Británie"),
    'actors': ["Colin Firth", "Stanley Tucci", "Gemma Artertonová", "Ralph Fiennes"]
  },
  'film_3' : {
    'name': 'Matrix',
    'year': 1999,
    'genre': {"Sci-fi", "Akční"},
    'isInCinema': True,
    'directors': ("Lana Wachowski", "USA", "Lilly Wachowski", "USA"),
    'actors': ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Mossová", "Hugo Weaving"]
  }
}
del film['film_1']

#print('We are the {} who say "{}!"'.format('knights', 'Ni'))

from tabulate import tabulate

informace = ["name", "year", "genre", "isInCinema", "directors", "actors"]
pocet = []
for f in film.keys():
  pocet.append(f)


# print("Slovník film")
# print("-------------------------------------------------------------------------------")
# print("Číslo filmu", "Jméno filmu",  "Rok vydání", "Žánr", "jeVKinech", "Režiséři", "Herci", sep="   ")
#
# for y in pocet:
#   text = []
#   text.append(y)
#   for x in range(0, len(informace)):
#     text.append(film[y].get(informace[x]))

# s = ""
# for t in text:
#   s = s + str(t) + "\t"
# print(s)
  #print(f" {text[0]} {text[1]} {text[2]} {text[3]} {text[4]} {text[5]} {text[6]}")

# print(tabulate(film["film_1"]))
# for y in pocet:
#   for x in range(0, len(informace)):
#       print(tabulate(film[y].get(informace)))


from texttable import Texttable

t = Texttable()
rows = [informace]
#t.add_rows([informace])
for y in pocet:
  text = []
  for x in range(0, len(informace)):
    v = film[y].get(informace[x])
    text.append(v)
    # if type(v) is str:
    #   text.append(v)
    # elif type(v) is int:
    #   text.append(v)
    # elif type(v) is bool:
    #   text.append(str(v))
    # elif type(v) is set:
    #   text.append(str(v))
    # elif type(v) is tuple:
    #   text.append(str(v))
    # elif type(v) is list:
    #   text.append(str(v))
  rows = rows + [text]
t.add_rows(rows)

print(t.draw())

film['film_4'] = {
    'name': 'No Time to Die (James Bond)',
    'year': 2021,
    'genre': {"Akční", "Dobrodružný"},
    'isInCinema': True,
    'directors': ("Cary Fukunaga", "USA"),
    'actors': ["Daniel Craig", "Ralph Fiennes", "Léa Seydouxová", "Rami Malek", "Ana de Armasová"]
  }

pocet = []
for f in film.keys():
  pocet.append(f)

t = Texttable()
rows = [informace]
for y in pocet:
  text = []
  for x in range(0, len(informace)):
    v = film[y].get(informace[x])
    text.append(v)

  rows = rows + [text]
t.add_rows(rows)

print(t.draw())