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

def czy_pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

def test_czy_jest_pierwsza():
    liczba = 5
    wynik = czy_pierwsza(liczba)
    assert wynik == True
#
def test_wielu_liczb_pierwszych():
    liczby = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for liczba in liczby:
        assert czy_pierwsza(liczba)


