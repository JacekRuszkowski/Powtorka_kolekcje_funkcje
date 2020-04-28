# def powiedz_czesc(imie, nazwisko):
#     imie = input("Podaj imie: ")
#     nazwisko = input("Podaj nazwisko: ")
#     print(f'Cześć {imie} {nazwisko}!')
#
#
# powiedz_czesc("Piotr", "GG")

# Kalkulator oparty o funkcje
# 1. Pobierz od użytkwownika 2 liczby
# 2. Pytamy o działanie: (+, -, *, /)
# 3. Na podstawie działania wykonyjemy obliczenia i je pokazujemy


def dodawanie(a, b):
    return a + b


def odejmowanie(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def dzielenie(a, b):
    return a / b


while True:

    a_podane = input("Podaj pierwszą liczbę: ")
    b_podane = input("Podaj drugą liczbę: ")
    # dzialanie = input("Jaki rodziaj dzialania chcesz wykonać? (+,-,*,/)")

    if not a_podane.isdecimal() or not b_podane.isdecimal():
        print("Musisz podać liczby całkowite. Spróbuj jeszcze raz.")
        continue
    else:
        a = int(a_podane)
        b = int(b_podane)
        dzialanie = input("Jaki rodziaj dzialania chcesz wykonać? (+,-,*,/)")

    if dzialanie == '+':
        print(f"Wynik działania to {dodawanie(a,b)}.")
        break
    elif dzialanie == '-':
        print(f"Wynik działania to {odejmowanie(a,b)}.")
        break
    elif dzialanie == '*':
        print(f"Wynik działania to {mnozenie(a,b)}.")
        break
    elif dzialanie == '/':
        print(f"Wynik działania to {dzielenie(a, b)}.")
        break
    else:
        print("Nie ma takiego działania. Spróbuj jeszcze raz.")







