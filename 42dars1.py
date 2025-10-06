nums1 = {1 , 2 , 3}
nums2 = {2 , 3 , 4 , 5}

#union
a= nums1 | nums2
print(a)


#intersection
b = nums1 & nums2
print(b)

#difference
c = nums1 - nums2
print(c)

#difference
d = nums2 - nums1
print(d)

# symmetric difference

e = nums1 ^ nums2
print(e)