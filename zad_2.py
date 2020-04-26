# Napisz program zamieniający miejscami w zadanej liście liczb element
# największy z najmniejszym.
# na wejsciu: [49, 50, 20, 40, 35, 10]
# na wyjsciu: [49, 10, 20, 40, 35, 50]

#         0   1   2   3   4   5
# liczby = [49, 50, 20, 40, 35, 10]

# Jak to zrobimy?
# 1. Musimy znaleźć indeks elementu o największej wartosci
# i indeks elementu o najmniejszej wartości
# 2. Zamiana miejscami elementów z tych indeksów

# Wersja A
# 1. używamy pętli for do znalezienia indeksów, patrz zadanie basics/zad_14
# 2. Zamieniamy wartości pod tymi indeksami

# Wersja B
# 1. Używając funkcji min(), max() znajduje najmniejszą i najwieksza wartosc
# 2. Znajduję indeks tych elementów w liscie
# 3. Zamieniam te elementy miejscami

# WERSJA B ##############


liczby = [49, 50, 20, 40, 35, 10]

max_number = max(liczby)
min_number = min(liczby)

# znalezienie indeksow szukanych liczb

print(liczby.index(max(liczby)))
print(liczby.index(min(liczby)))

# zamiana miejscami

tymczasowa = liczby[1]
liczby[1] = liczby[5]
liczby[5] = tymczasowa

print(liczby)
print("="*50)
print()


# WERSJA A ##############

liczby_2 = [49, 50, 20, 40, 35, 10]

max_wartosc = None
min_wartosc = None

for i in liczby_2:
    print(liczby.index(i), i)

    if max_wartosc == None or i > max_wartosc:
        max_wartosc = i
    if min_wartosc == None or i < min_wartosc:
        min_wartosc = i


print(max_wartosc, liczby_2.index(max_wartosc),"   ", min_wartosc, liczby_2.index(min_wartosc))

tymczasowa_2 = liczby_2[1]
liczby_2[1] = liczby_2[5]
liczby_2[5] = tymczasowa_2

print(liczby_2)



