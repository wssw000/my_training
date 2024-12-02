list = [2, 3, 4, 5, 6, 6, 2, 43]

def count_chisel(list1):
    n = 0
    for i in list:
        if i % 2 == 0:
            n = n + 1
        else:
            continue

    return n

def find_max(list_max):
    max = 0
    for i in list_max:
        if i > max:
            max = i
        else:
            continue
    return max

def unique(list_):
    unique_list = []
    for i in list_:
        if i in unique_list:
            continue
        else:
            unique_list.append(i)
    return unique_list

print(count_chisel(list))
print(find_max(list))
print(unique(list))