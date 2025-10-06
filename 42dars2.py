words  = {

   "apple" : "olma" , 
   "pear" : "nok",
   "banana": "banan"
}

print(words)

print(words["apple"])
print(words["pear"])

#print(words['berry'])

print(words.get("berry"))


counter = {

    "apple" : 42,
    "pear" : 31
}

counter["apple"] += 3

print(counter)

print(counter.keys())

print(counter.values())

del counter["apple"]
print(counter)

counter.pop("pear")

print(counter)

counter["melon"] = 43
print(counter)

#nasted
cities =[
    {
        "name":"Tashkent",
        "population": 2.4e9 , #2_400_000
        "coord":(41.15 , 69.24),  #qavs ichida yozilsa Tuple buladi
        "is_ancient":True
    }
]

a=cities[0]["coord"]
print(type(a)) # --> tuple

print(a)

