# Работа с словарями
my_dict = {'Artem' : 1987, 'Vasya' : 2005, 'Nikita' : 2008}
print(my_dict)
print(my_dict.get('Artem'))
print(my_dict.get('Oleg'))

my_dict.update({'Stepa': 2006, 'Petr': 2000})
print(my_dict.pop('Artem'))
print(my_dict)

# Работа с множествами
my_set = {1, 2, 2, 1, 3, 'string', True, False, 'string'}
print(my_set)
my_set.add(4)
my_set.add('secondstring')
my_set.remove('string')
print(my_set)