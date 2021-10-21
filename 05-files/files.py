import csv
import json


def textfile_read(path, encoding='utf-8'):
    try:
        with open(path, encoding=encoding) as file:
            data = file.read()
    except FileNotFoundError as error:
        return f'Soubor nebyl nalezen: {error}'
    except Exception as error:
        return f'Došlo k nějakému problému při otevírání souboru: {error}'
    finally:
        file.close()
    return data

def textfile_write(path, data='', encoding='utf-8'):
    try:
        with open(path, mode='w', encoding=encoding) as file:
            file.write(data)
    except FileNotFoundError as error:
        print(f'Soubor nebyl nalezen: {error}')
        return False
    except Exception as error:
        print(f'Došlo k nějakému problému při otevírání souboru: {error}')
        return False
    finally:
        file.close()
    return True

def jsonfile_read(path, encoding='utf-8'):
    try:
        with open(path, encoding=encoding) as file:
            data = json.load(file)
    except FileNotFoundError as error:
        return f'Soubor nebyl nalezen: {error}'
    except Exception as error:
        return f'Došlo k nějakému problému při otevírání souboru: {error}'
    finally:
        file.close()
    return data

def jsonfile_write(path, data={}, encoding='utf-8'):
    try:
        with open(path, mode='w', encoding=encoding) as file:
            json.dump(data,file)
    except FileNotFoundError as error:
        print(f'Soubor nebyl nalezen: {error}')
        return False
    except Exception as error:
        print(f'Došlo k nějakému problému při otevírání souboru: {error}')
        return False
    finally:
        file.close()
    return True

def csvfile_read(path, encoding='utf-8'):
    try:
        with open(path, encoding=encoding, newline='\n') as file:
            reader = csv.DictReader(file, delimiter =';', quotechar='"')
            dict_list = []
            for row in reader:
                dict_list.append(row)
    except FileNotFoundError as error:
        return f'Soubor nebyl nalezen: {error}'
    except Exception as error:
        return f'Došlo k nějakému problému při otevírání souboru: {error}'
    finally:
        file.close()
    return dict_list

def csvfile_write(path, data=[], encoding='utf-8'):
    try:
        with open(path, mode='w', encoding=encoding, newline='\n') as file:
            header = next(data)
            writer = csv.DictWriter(file,fieldnames=header,delimiter =';', quotechar='"')
            dict_list = []
            for row in writer:
                dict_list =writer(row)
    except FileNotFoundError as error:
        return f'Soubor nebyl nalezen: {error}'
    except Exception as error:
        return f'Došlo k nějakému problému při otevírání souboru: {error}'
    finally:
        file.close()
    return dict_list


csvdata = csvfile_read('./reality.csv')
print(csvfile_write('./novy.csv', csvdata))

# csvdata = csvfile_read('./reality.csv')
# print(type(csvdata))

# txt= textfile_read('./python.txt')
# print(textfile_write('./novy.txt', txt))

# jsondata = jsonfile_read('./pokus.json')
# print(jsonfile_write('./novy.json',jsondata))