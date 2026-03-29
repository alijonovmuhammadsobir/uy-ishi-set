set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

farq = list(set1 ^ set2) 

n = len(farq)
for i in range(n):
    for j in range(0, n - i - 1):
        if farq[j] < farq[j + 1]: 
            farq[j], farq[j + 1] = farq[j + 1], farq[j]
print(farq)
