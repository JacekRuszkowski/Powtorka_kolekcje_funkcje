# Napisz program zliczający liczbę wystąpień każdego znaku
# w podanym przez użytkownika napisie.

# 0. Robimy pusty słownik, w którym będziemy zliczac litery
# 1. Wczytujemy napis od użytkownika
# 2. Przechodzimy przez wszystkie znaki (for)
#   2a. jesli nie ma danego znaku w slowniku to dodajemy
#   2b. jezeli jest to zwiększamy liczbe o 1

# slownik
# klucz  => wartość
# litera => liczba wystąpień (int)

wystapienia = {}

napis = input("Wprowadź jakieś zdanie: ")

for litera in napis.lower():
    if litera not in wystapienia:
        wystapienia[litera] = 1
    else:
        wystapienia[litera] += 1

for klucz, wartosc in wystapienia.items():
    print(f"{klucz} - {wartosc}")