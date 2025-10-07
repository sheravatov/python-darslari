
davlatlar = ['uzb' , 'rus' , 'aqsh' , 'korea' , 'xitoy' , 'russia']

print(len(davlatlar))

print(sorted(davlatlar))

print(sorted(davlatlar , reverse=True))

print(davlatlar)

davlatlar.reverse()
print(davlatlar)

davlatlar.sort()
print(davlatlar)

davlatlar.sort(reverse=True)

print(davlatlar)

sonlar = (list(range(120 , 1200 , 2)))

print(sum(sonlar))

print(max(sonlar)-min(sonlar))


print(len(sonlar))

print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])