import random
def arrayIndexing(a):
    temp = []
    for i in range(len(a)):
        temp.append([a[i], i, 0])
    temp.sort(reverse=True)
    for i in range(len(a)):
        temp[i][2] = i
    return temp

a1 = []
# a1 = [9, 5, 4, 3, 2, 1, 8, 6, 7, 10]
for i in range(10):
    a1.append(random.randint(1, 10))

print(random.randint(1, 10))
a2 = arrayIndexing(a1)

#a2 holds a list in which the first value is the values from array, second is the original index, third is the index after sorting
# [[<value>, #original_index, #new_index], [<value>, #original_index, #new_index]]