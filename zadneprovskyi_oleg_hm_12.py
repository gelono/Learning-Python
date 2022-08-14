# Написать функцию генератор с помощью range которая будет выводить числа по порядку и в обратном направлении.

def my_gen(start, finish, step):
    for x in range(start, finish, step):
        yield x
    for x in range(finish, start, -step):
        yield x
        
for i in my_gen(0, 10, 1):
    print(i)
