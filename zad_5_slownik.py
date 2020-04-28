# Napisz program wyliczający kwotę należną za zakupiony towar
# na podstawie podanej przez użytkownika wagi i nazwy produktu.
# Do przechowywania informacji o cenie za kilogram
# danego produktu użyj słownika.
# Wypisz wszystkie dostępne produkty w sklepie.


# 1. Robimy słownik z produktami, dodajmy:
#       ziemniaki 1.2
#       pomiodory 4.5
#       marchew 0.5
# 2. Wyświetlam słownik
# 3. Pytam użytkownika o produkt i sprawadzam czy jest w produktach
# 4. Wczytujemy ile kg uzytkownik chce kupic
# 5. Liczymy należnosc


produkty = {
    'ziemniaki': 1.2,
    'pomidory': 4.5,
    'marchew': 0.5
}

print("Oto nasze produkty:")

for produkt, cena in produkty.items():  # wyswietlanie wartosci i klucza slownika
    print(f"{produkt} - {cena} zł")

while True:

    co_kupic = input("\nJaki produkt chcesz kupić? ")

    if co_kupic not in produkty:
        print("Nie mamy takiego produktu.Spróbuj jeszcze raz.")
        continue

    else:
        ilosc = int(input(f"Wybrałeś produkt - {co_kupic}. Ile kilogramów chcesz kupić? "))
        break

cena_produktu = produkty.get(co_kupic)

do_zaplaty = ilosc * cena_produktu

print(f"\nTwoje zamówienie:\n{co_kupic} - {ilosc}kg.\nkoszt: {do_zaplaty:.2f} zł.")
