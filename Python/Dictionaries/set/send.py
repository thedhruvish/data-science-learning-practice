set1 = {1,3,5,6,111,98}
set2 = {24,5,76,78,98}

"""
for i in set1:
    print(i)


#Join
#set3 = set1.union(set2)
set3 = set1 | set2

print(set3)
"""
"""
set1.update(set2)
print(set1)

set3 = set1.intersection(set2)
set3 = set1 & set2


set1.intersection_update(set2)
print(set1)
"""


#set3 = set1.difference(set2)
#set3 = set1 - set2

#set3 = set1.symmetric_difference(set2)
#set3 = set1 ^ set2

set1.symmetric_difference_update(set2)

print(set1)
