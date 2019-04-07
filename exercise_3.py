liczba = int(input("Pomyśl liczbę od 0 do 1000, "
                   "a ja ją zgadnę w maksymalnie 10 próbach"))

min, max = 0, 1000

warunek_stopu = False
# val1 = input("za dużo")
# val2 = ("za mało")
# val3 = ("zgadłeś")

while not warunek_stopu:
    guess = int((max - min) / 2 + min)
    print("Zgaduję: {}".format(guess))

    print("Pobierz odpowiedź z zestawu")
    odpowiedz = input("(1) za dużo, (2) za mało (3) zgadłeś")
    odpowiedz = int(odpowiedz)

    if odpowiedz == 3:
        warunek_stopu = True
    elif odpowiedz == 1:
        max = guess
        guess = int((max - min) / 2 + min)
    elif odpowiedz == 2:
        min = guess
        guess = int((max - min) / 2 + min)





# for i in range(1,11):
#     print("Wybierz właściwą w twoim wypadku odpowiedź:")

