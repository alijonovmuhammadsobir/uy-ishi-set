set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

birlashma = set1 & set2
set = set1 - set2

natija = sum(birlashma) - sum(set)
print(natija)