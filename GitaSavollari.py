"""
1.if12. Uchta son berilgan. Shu sonlarning kichigini aniqlovchi programma tuzilsin.


def uchson(x:int , y: int , z: int)->int:
    return min(x , y , z)

print(uchson(5 , 3 , 9))


2.if28. Yil berilgan (musbat butun son). Berilgan yilda nechta kun borligini aniqlovchi 
programma tuzilsin. Kabisa yilida 366 kun bor, kabisa bolmagan yilda 365 kun bor. 
Kabisa yil deb 4 ga karrali yillarga aytiladi. Lekin 100 ga karrali yillar ichida faqat 400
ga karrali bolganlari kabisa yil hisoblanadi. Masalan 300, 1300 va 1900 kabisa yili 
emas. 1200 va 2000 kabisa yili.


yil = 1200
if yil % 4==0 and yil % 100 != 0 or yil % 400 == 0:
    print("kabisa yili")
else:
  print("kabisa yili emas")

#Tushuntirish:

Agar yil 4 ga bo‘linib, 100 ga bo‘linmasa, yoki 400 ga bo‘linsa — u kabisa.




3.x,y haqiqiy sonlari berilgan. Ularning kichigini sonlar yig’indisining yarmiga, kattasini 
ko’paytmasining ikkilanganiga almashtiruvchi programma tuzilsin. Agar sonlar teng 
bo'lsa, o'zgarishsiz qoldirilsin.



def ikkison(x , y) :

    if x<y:
        return (x+y)/2 , x*y*2
    elif y<x:
        return x*y*2 ,(x+y)/2
    else:
        return x , y


print(ikkison(8 , 8 ))

4.Case9. Ikkita butun son berilgan Day (kun) va Month (oy). (Kabisa bo`lmagan yil sanasi 
kiritiladi). Berilgan sanadan keyingi sanani ifodalovchi programma tuzilsin.

"""
month = 3
day = 3
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month == (days_in_month[month-1]):
    print()




