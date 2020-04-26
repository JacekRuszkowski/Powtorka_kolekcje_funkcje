# Napisz program wyświetlający minimalną oraz maksymalną liczbę z wszystkich
# liczb wprowadzonych przez użytkownika.
# Daj użytkownikowi możliwość zakończenia wprowadzania liczb odpowiednią komendą.
# Zadbaj o obsłużenie przypadku gdy użytkownik nie wprowadzi żadnej liczby.


znalezione_minimum = None
znalezione_maximum = None

while True:
    wprowadzona_liczba = input("Podaj liczbę lub napisz 'end': ")

    if wprowadzona_liczba == 'end':
        break

    if wprowadzona_liczba.isdecimal() == False:
        print("Wprowadzona dana nie jest iczbą. Spróbój jeszcze raz: ")
        continue

    liczba = int(wprowadzona_liczba)

    if znalezione_minimum is None or liczba < znalezione_minimum:
        znalezione_minimum = liczba
    if znalezione_maximum is None or liczba > znalezione_maximum:
        znalezione_maximum = liczba


if znalezione_maximum is None and znalezione_minimum is None:
    print ("Nie podałeś żadnej liczby")
else:
    print(f"Znalezione maximum to {znalezione_maximum}, natomist minimum to {znalezione_minimum}.")
