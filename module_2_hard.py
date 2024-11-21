import random

random =  random.randint(3, 20)
list2 = []

for i in range(1, random):
    for j in range(1, random):
        if random % (i + j) == 0 and i != j:
            couple = []
            list2.append(i)
            list2.append(j)
        else:
            continue

new_list2 = list2[:int(len(list2) / 2)]
print(*new_list2)