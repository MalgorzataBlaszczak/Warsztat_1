from random import randint
def dicethrow(code):
    try:
        code = input("Podaj kod rzutu kością")
        dice_n = 1
        dice_t = None
        m = 0
        d_pos = code.find("D")
        if d_pos == -1:
            print("Kod kości nieprawidłowy! Kod musi zawierać symbol 'D' i odpowiednie liczby.")
            return None
        else:
            if d_pos >= 1:
                dice_n = int(code[:d_pos])
            #     print("Pozycja D to {}".format(d_pos))
            # print("Ilość kości to: {}".format(dice_n))

        plus_pos = code.find("+")
        minus_pos = code.find("-")
        sign_pos = -1
        if plus_pos == -1 and minus_pos == -1:
            m = 0
            dice_t = int(code[d_pos+1:])
        elif plus_pos > 0 and minus_pos == -1:
            sign_pos = plus_pos
            m = int(code[sign_pos+1:])
            dice_t = int(code[d_pos+1:sign_pos])
        elif plus_pos == -1 and minus_pos > 0:
            sign_pos = minus_pos
            m = int(code[sign_pos + 1:])
            dice_t = int(code[d_pos + 1:sign_pos])
        # print("Typ kości to:{}, modifier to {}".format(dice_t, m))
        # print("Pozycja plusa lub minusa to {}".format(sign_pos))

        allowed_dice_t = [3, 4, 6, 8, 10, 12, 20, 100]
        if dice_t in allowed_dice_t:
            my_sum = 0
            for i in range(0, dice_n):
                my_sum += randint(1, dice_t)
                # print("Suma moich rzutów: " + str(my_sum))
                if code[sign_pos] == "+":
                    result = my_sum + m
                else:
                    result = my_sum - m
            return "Ostateczny wynik: " + str(result)

        else:
            print("Kod kości nieprawidłowy! Nie możesz użyć kości o takiej liczbie ścianek!")
            return None
    except TypeError:
        print("Kod kości nieprawidłowy! Typ i ilość kości oraz modyfikator muszą być wyrażone liczbami!")
    except ValueError:
        print("Kod kości nieprawidłowy!")
    except Exception:
        print("Wystąpił nieznany błąd!")
        return None

#  zakomentowane printy powyżej służyły do bieżącego sprawdzania czy dobrze liczy zmienne
#  dlatego zostawiłąm je specjalnie w takiej formie


#
#



check1 = dicethrow("2D10+10")
print(check1)
# # check1 = roll(2,4)
# # print(check1)
# #
# # check2 = roll(3,6,1)
# # print(check2)
#
# check3 = roll(4.5)
# print(check3)


