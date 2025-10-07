#Conditions, If va Else
#boolean
'''
print(True)#true
age = 6
print(age>12)#false
print(age>=12)#false
print(age<=12)#true
print(age!=6) #false
print(not age == 6) #false


print(10 < age < 15) #false
print(10 < age < 15 or age == 6) #True
print(1 < age < 15 and age == 6) #True


if age < 18:
    print("voyaga yetmagan!")

text=42
name="shaxzod"
if text == 42 and name == "shaxzod":
    print("true")
else:
         print("yo'q")

'''
#kabisa yili

yil = int(input("Yilingizni kiriting: "))

if (yil % 400 == 0) or (yil % 4 == 0 and yil % 100 != 0):
    print("Kabisa yili")
else:
    print("Kabisa yili emas")