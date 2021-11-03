def sort_item(item):
    return item[1]

def charFrequency(veta):
    zadani_list = list(veta)
    mylist = list(dict.fromkeys(zadani_list))
    print(mylist)
    numbers = []
    for x in mylist:
        numbers.append(zadani_list.count(x))
    print(numbers)
    vysledek = list(zip(mylist, numbers))

    vysledek.sort(key=sort_item, reverse=True)
    print(*vysledek, sep="\n")


text = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
charFrequency(text)
