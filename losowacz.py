from random import choice
ludki = list()
pary_prezentowe = dict()



def pobranie_listy():
    global ludki
    global count
    plik = open(input("Podaj nazwę pliku txt z listą imion po przecinku: "), "r")
    for line in plik:
        ludki = line.split(", ")
    plik.close()
    count = len(ludki)
    return ludki
    return count

def take_user():
    global user
    global count
    user = input("Podaj swoje imię: ")
    while user not in ludki:
        print ("Nie ma Cię na liście!")
        user = input("Podaj swoje imię: ")
        continue
    else:
        pass
    if user in pary_prezentowe:
        print ("Użytkownik już głosował!")
        take_user()
    count -= 1
    return user
    return count

def losowanie():
    obdarowany = choice(ludki)
    if obdarowany in pary_prezentowe.values() or obdarowany == user:
        losowanie()
    else:
        pary_prezentowe[user] = obdarowany


pobranie_listy()

while count > 0:
    take_user()
    losowanie()
    print (pary_prezentowe[user])
else:
    print ("Losowanie zakończone")
wyniki = pary_prezentowe.items()
for item in wyniki:
    print (item)




