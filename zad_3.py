# Napisz program zliczający liczbę wystąpień samogłosek (a, e, i, o, u, y)
# w podanym przez użytkownika napisie.

# 1. Pobieramy napis od użytkownika
# 2. Przechodzimy po kazdej literze z napisu (for)
# 3. Sprawdzamy czy znak znajduje sie w samogloskach -> tak? to go zliczamy

# Jak poradzić sobie ze zliczaniem dużych liter?
# 1. Możemy je dodać do tupli z samogłoskami
# 2. Użyć metody .lower()

napis = input("Napisz jakieś zdanie: ")
samogloski = ('a', 'e', 'i', 'o', 'u', 'y')

liczenie = 0

for i in napis.lower():
    if i in samogloski:
        liczenie += 1

print(liczenie)