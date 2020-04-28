# Napisz program zliczający liczbę znaków w podanym przez użytkownika napisie
# pomiędzy nawiasami <>. Nawiasy mogą wystąpić tylko raz.
# Ala ma <kota>, a kot ma Alę
# 4

# 1. Sprawdzam liczbę < i > - powinno ich być po jednym,
#       jeżeli liczba tych nawiasów jest inna, to kończę program
# 2. W pętli sprawdzam czy:
#       - mam zliczac
#       - mam przestać zliczać
#       - czy zliczanie jest włączone i wtedy zliczam


sentence = input("Podaj napis zawierający jedennawias kwadratowy: ")


# 1 metoda

# for i in sentence:
#     if sentence.count('<') != 1 or sentence.count('>') != 1:
#         print("Zła ilość nawiasów.")
#         exit(1)
#
# count = sentence.index(">") - sentence.index("<") - 1
#
# print(count)

# 2 metoda

count = 0
to_count = False # zmienna, kóry włącza i wyłącza liczenie. wlacza sie na True przy pierwszym nawiasie i pozastaje True dopóki nie napiszemy, że ma być False (przy drugim nawiasie).

for i in sentence:
    if i == "<":
        to_count = True
    elif i == ">":
        to_count = False
    elif to_count == True:
        count += 1

print(count)
