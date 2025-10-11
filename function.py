#python3 -i function.py
def square(son):
    return son*son

#ans = square(int(input("son kiriting: ")))
#print(ans)

def add(x : str, y : str) -> str:
    return x+y

#print(add('salom' , '2'))

def absolute(num : int) -> int:
    """
bu manfiy sonlarni ham musbat qilib beradi
"""
    if num<0:
      return -1*num
    return num

#print(absolute(int(input("son kiriting:"))))


"""
def absolute(num : int) -> int:
    if num<0:
        return -1*num
    return num

son = (int(input("son kiriting:")))
print(absolute(son))

----------------------------------------------------------
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
def ikki_son_yigindisi(array, targetSum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return sorted([array[i], array[j]])
    return []

"""


array = [7, 1, 9, 4]
min_x = []
def ikkiSonFarqi(array):
    for i in range(len(array)):
        for j in range(i+1 , len(array)):
            if array[i]-array[j] > array[j]-array[j+1]:
                return sorted([array[i] , array[j]])
             
print(ikkiSonFarqi(array))