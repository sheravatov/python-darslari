"""R13:

Listda nechta integer bor ekanligini aniqlovchi dastur tuzing.

Input:
[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

Output:


list = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
def  newlist(list):
    count = 0
    for li in list:
         if type(li) == int:  #if isinstance(li, int):
            count+=1

    return count          
       
print(newlist(list))


R12:

List ichidagi yi'gindisi eng katta bo'lgan listni toping.

Berilgan list: 
[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

Result:
[10, 11, 12]



dic = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
newdic = []
max_sum = 0

for lst in dic:
    if sum(lst)>max_sum:
        max_sum=sum(lst)
        newdic=lst

print(newdic)   




nums = [[5,6,7], [1,2,3], [9,0,1], [3,4,5]]

newnums = []
nums_sum = sum(nums[0])

for lst in nums:
    if sum(lst)<nums_sum:
        nums_sum = sum(lst)
        newnums = lst
print(newnums)


nums = [[5,6,7], [1,9,3], [9,0,1], [3,4,5]]

new_nums = []
som = 0


for num in nums:
    for n in num:
        if n > som:
            som = n

found = False
for i in range(len(nums)):
    for j in nums[i]:
        if som == j:
            print(nums[i])
            found = True
            break
            
    if found:   # tashqi siklni ham to‘xtatish
        break



R1:

Ikkita listning o'rta arifmetigini chiqaring.

Input:
[1, 1, 3, 4, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 4, 5, 7, 8]

Output:
3.823529411764706




list1 = [1, 1, 3, 4, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
count = 0
num = 0
for lis in list1+list2:
    num+=lis
    count+=1

print(num/count)



list1 = [1, 1, 3, 4, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
count = 0
num = 0

for lis in list1:
    num+=lis
    count+=1

for lists in list2:
    num+=lists
    count+=1

print(num/count)


R2:

Listning oxirgi elementini boshqa listga o'zgartirib qo'ying.

Input:
[1, 3, 5, 7, 9, 10], [2, 4, 6, 8]

Output:
[1, 3, 5, 7, 9, 2, 4, 6, 8]


list1 = [1, 3, 5, 7, 9, 10]
list = [2, 4, 6, 8]

del list1[-1]

print(list1+list)


R3:

Kiritilgan stringni listdagi har bir elementning boshiga qo'shadigan dastur tuzing.

Input:
[1, 4, 3, 9]
"RM"

Output:
['RM1', 'RM4', 'RM3', 'RM9']




numbers = [1, 4, 3, 9]
word = "RM"

for i in range(len(numbers)):
    numbers[i]=str(numbers[i])
    numbers[i]+=word

print(numbers)




Nollarni orqaga surish

Berilgan sonlar ro'yxatidagi nollarni ro'yxat orqasiga o'tkazing, lekin boshqa elementlar ketma-ketligi buzilmasin.

Imkon qadar kamroq amal bajaring.

Qo'shimcha xotiradan foydalanmang - amallarni ro'yxat ustida bajaring.

Misol 1:

Kiritish: nums = [0,1,0,3,12]
Natija: [1, 3, 12, 0, 0]
Misol 1:

Kiritish: nums = [0]
Natija: [0]


nums = [0,1,0,3,12]

def moveZeroes(nums: list) -> list:
    zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_index] = nums[i]
            zero_index += 1

    for i in range(zero_index , len(nums)):
        nums[i] = 0
    return nums
        

print(moveZeroes(nums))

"""

nums = [0,1,0,3,12]

def moveZeroes(nums: list) -> list:
    zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_index] = nums[i]
            zero_index+=1

    for i in range(zero_index , len(nums)):
        nums[i] = 0
    return nums

print(moveZeroes(nums))
