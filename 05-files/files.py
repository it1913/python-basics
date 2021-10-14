def readFile(filename):
    try:
        with open(filename, encoding='utf-8')as file:
            data = file.read()
    except FileNotFoundError as error:
        return f'Soubor nebyl nalezen: {error}'
    except Exception as error:
        return f'Došlo k nìjakému problému pøi otevírání souboru: {error}'
    finally:
        file.close()
    return data

print(readFile('python.txt'))