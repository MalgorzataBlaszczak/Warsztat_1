# czy wprowadzony ciąg znakówjest poprawną liczbą
# czy użytkownik nie wpisał tej liczby już poprzednia
# czy liczba należy do zakresu 1 - 49

#
#
# liczby_uzytkownika = []
# try:
#     while len(liczby_uzytkownika) <= 6:
#
#         liczba = int(input("Podaj liczbę: "))
# except ValueError:
#     print("Takich rzeczy nie da się wylosować w lotto. Podaj liczbę naturalną z zakresu 1 - 49")
#     continue
#     if liczba in liczby_uzytkownika:
#         print("Hej, wylosowałeś już tę liczbę. Nie wolno się powtarzać")
#         continue
#     if liczba > 49 or liczba <1:
#         print("Przesadziłeś! Takiego lotto jeszcze nie było! Pamiętaj: od 1 do 49!")
#         continue
#     liczby_uzytkownika.append(liczba)
#
# print(liczby_uzytkownika)
# try...except
#
#
#
# list = [i for i in range(1,50)]
# print(list)
# l1 = input("Podaj liczbę

liczby_uzytkownika = []

while len(liczby_uzytkownika) < 6:
   try:
       liczba = int(input("Podaj liczbę: "))
   except ValueError:
       print("Takich rzeczy nie da się wylosować w lotto!")
       continue

   if liczba in liczby_uzytkownika:
       print("Hej wylosowałeś już tą liczbę. Powinienś czegoś nowego!")
       continue

   if liczba > 49 or liczba < 1:
       print("Takiego lotto jeszcze nie było!")
       continue

   liczby_uzytkownika.append(liczba)
# 1 sposób
liczby_użytkownika = sorted(liczby_uzytkownika)

# 2 sposób
liczby_uzytkownika.sort()
print(liczby_uzytkownika)

# maszyna losująca
import random
numerki_maszyny_losujacej = list(range(1, 49+1))
random.shuffle(numerki_maszyny_losujacej)
twoje_szczesliwe_numery = numerki_maszyny_losujacej[:6]
print(twoje_szczesliwe_numery)

# zgadniete_numery = []
# for i in liczby_uzytkownika:
#     if i in twoje_szczesliwe_numery:
#         zgadniete_numery.append(i)
#     else:5
#         continue
# if len(zgadniete_numery) >=3:
#     print("Trafiłeś co najmniej 3!" + str(zgadniete_numery) # niesprawdzony kod

counter = 0
for moj_numer in liczby_uzytkownika:
    if moj_numer in twoje_szczesliwe_numery:
        counter+=1
if counter>=3:
    print("Trafiłeś {} liczb".format(counter))
else:
    print("Słabo trafiłeś. Trafione {}".format(counter))
