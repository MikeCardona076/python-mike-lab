setA = {1,2,23,5}
setB = {1,2,3,4,5,6,7,8,9,10,1,2,3}

#This function returns the intersection of two sets
print(setA.intersection(setB))

#This function returns the union of two sets
print(setA.union(setB))

#This function returns the difference of two sets or rest of the elements in setA
print(setA.difference(setB))

#This function returns the symmetric difference of two sets or rest of the elements in setA
print(setA.symmetric_difference(setB))


print(setA.issubset(setB))


print(setA.issuperset(setB))


print(setA.isdisjoint(setB))


