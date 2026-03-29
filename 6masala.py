set1 = {4,5,6,7,8,9}
set2 = {5,6,7,10,11}

umumiy=set1.intersection(set2)
umumiymas = set1.symmetric_difference(set2)

result = sum(umumiymas) - sum(umumiy)
print(result)