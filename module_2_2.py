first = int(input('Ведите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second and third == second:
    print(3)
elif first == second or third == second or first == third:
    print(2)
else:
    print(0)