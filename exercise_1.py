import random
zgadniete = False
zgadywana_liczba = random.randint(0,100)
print(zgadywana_liczba)
while not zgadniete:
    try:
        liczba = input("Zgadnij liczbę")
        liczba = int(liczba)
        if liczba > zgadywana_liczba:
            print("Za dużo!")
        elif liczba < zgadywana_liczba:
            print("Za mało!")
        else:
            print("Zgadłeś!")
            # break    sposób pierwszy
            zgadniete = True
    except ValueError:
        print("To nie jest liczba")

print("Liczba jest poprawna".format(liczba))