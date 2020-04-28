# W sesji interaktywnego środowiska stwórz następujące struktury danych korzystając ze skróconej wersji zapisu:
# - listę zawierającą liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
# - zbiór tupli zawierających 3 elementy - daną liczbę, jej kwadrat i jej sześcian - w przedziale od -10 do 10
# - słownik mapujący napisy na ich długość powstały ze zbioru napisów



# wyrazenie listowe
# # Po co jest? Co robi? Ma zrobić listę
# wynik2 = [wartosc for wartosc in range(0, 11)]
# print(wynik2)

for i in range (0,11):
    print(i/10, end="  ")

print()

lista = [i/10 for i in range(0,11)]
print(lista)

for i in range (-10, 11):
    print(i, i**2, i**3)

tupla = {(i, i**2, i**3) for i in range(-10,11)}

print(tupla)
print(type(tupla))

print('+'*30)

zbior_napisow = {'to', 'jest', 'zbior', 'napisow'}
slownik = {}
liczenie = 0

# 1 metoda

for slowo in zbior_napisow:
    slownik[slowo] = len(slowo)
print(slownik)

# 2 metoda (wyrazenie listowe)

slownik_2 = {slowo: len(slowo) for slowo in slownik}

print(slownik_2)