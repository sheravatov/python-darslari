'''
1 dan n gacha, har bir son uchun:
     - 3 ga bo'linsa, fiz deb
     - 5 ga bo'linsa, buz deb
     - ikkisiga ham bo'linsa, fizbuz deb
     - hech qaysida bo'linmasa, sonni o'zini

ekranga chiqaring
'''

n = int(input("Son kiriting: "))

son = 1  # 1 dan boshlaymiz
while son <= n:
    fiz = (son % 3 == 0)
    buz = (son % 5 == 0)

    if fiz and buz:
        print("fizbuz")
    elif buz:
        print("buz")
    elif fiz:
        print("fiz")
    else:
        print(son)

    son += 1  # har safar bittaga oshiramiz
