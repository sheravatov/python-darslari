#while
i=0
while i < 10:
    print(i)
    i+=1

print(i)
while True:
    print(i)
    i+=1

    if i==121:
        break

k=0

while k<=10:
    k+=1
    if k%2==1:
        continue
    print(f"{k} musbat")


#for loop

nums = [1 , 2 , 3]

for num in nums:
    print(num)



for char in "Shaxzod":
    print(char)


for num in set ([3 , 2 , 1]):
    print(num)


fruits = {"olma" : 42 , "anor" :12}

for fruit , count in fruits.items():
    print(fruit , count)


nums = list(range(10000))
print(nums)