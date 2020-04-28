# Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika.
# Sprawdź jak dużo z tych liczb jest liczbami parzystymi
# w zakresie 0-100 - w tym celu skorzystaj z operatora iloczynu.

# 1 czesc - ile unikalnych liczb uzytkownik wprowadzil
# w petli (while) wczytujemy dane do zbioru, koniec przerywa petle
# po petli pokazujemy ile unikalnych liczb zostalo wczytanych i jakie to byly

# 2 czesc - ile wprowadzonych liczb bylo parzystych w zakresie od 0 do 100
# trzeba sobie zrobic zbior liczb parzystych - mozna uzyc petli for i funkcij range(0, 101, 2)
# robimy iloczyn teoriomnogosciowy na dwoch zbiorach, zeby pokazac ktore wprowadzone, byly parzyste

liczby = set()

while True:
    liczba = input("Podaj liczbę: ")
    if liczba.lower() == "end":
        break
    else:
        liczby.add(int(liczba))

print(f"w zbiorze {liczby} znajduje sie {len(liczby)} unikalnych liczb")

zbior_parzyste = set()

for i in range (0,101, 2):

    zbior_parzyste.add(i)


#  jak duzo jest parzystych w zakresie 1 - 100

parzyste = zbior_parzyste & liczby

print(f"W stworzonym zbiorze jest {len(parzyste)} liczb parzystych z przedziału 0-100.")
