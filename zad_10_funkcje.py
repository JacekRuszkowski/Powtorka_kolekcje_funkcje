# Napisz funkcję sprawdzającą, czy dana liczba jest liczbą pierwszą.
# Przykład użycia:
# >>> czy_jest_pierwsza(10)
# False
# >>> czy_jest_pierwsza(17)
# True

# Liczba pierwsza
# - bedzie intem
# - wieksza od 1
# - dzieli sie tylko przez 1 i przez sama siebie

# def czy_pierwsza(liczba):
#     if liczba <= 1:
#         return False
#     for i in range(3, liczba):
#         if liczba % i == 0:
#             return False
#     return True



def czy_pierwsza(liczba):
    if liczba <= 1:
        return False
    elif liczba == 4:
        return False
    for i in range(3, liczba):
        if liczba % i == 0:
            return False
    return True



while True:

    liczba_podana = input("Podaj liczbę całkowitą: ")

    if liczba_podana.isdecimal():
        liczba = int(liczba_podana)
    elif liczba_podana == "end":
        break
    else:
        print("Prosiłem o liczbę całkowitą. Spróbuj jeszcze raz.")
        continue

    if not czy_pierwsza(liczba):
        print("To nie jest liczba pierwza.")
    else:
        print("To jest liczba pierwsza.")
