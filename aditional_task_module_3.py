coast = 0
def calculate_structure_sum(list):
    global coast
    for i in list:
        if isinstance(i, int):
            coast = coast + i
        elif isinstance(i, str):
                coast = coast + len(i)
        elif isinstance(i, dict):
            for j in i.items():
                for g in j:
                    if isinstance(g, int):
                        coast = coast + g
                    elif isinstance(g, str):
                        coast = coast + len(g)
        else:
            calculate_structure_sum(i)
    return coast

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)