# Task-1

a = input('Enter text: ')
if len(a) < 2:
    print('Ваша строка слишком короткая - %s' % a)
else:
    b = a[:2] + a[-2:]
    print(b)


# Task-2

s = 'Hillel school'
d = {}
for i in range(len(s)):
    if s[i] in list(d.keys()):
        i = i + 1
    else:
        count = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                count = count + 1
                j = j + 1
            else:
                j = j + 1
        d[s[i]] = count
print(d)


# Task-3

my_list = ['milk', 'kolbasa', 'bread']
max_s: int = 0
product: str = ''
for i in range(len(my_list)):
    if len(my_list[i]) > max_s:
        max_s = len(my_list[i])
        product = my_list[i]

print('Самое длинное название продукта {} длинна {} символов'.format(product, max_s))

# Task-4

name = input('Enter name: ')
b_name = name.upper()
l_name = name.lower()
print(b_name + ' {}'.format(l_name))

# Task-5

your_list = input("Enter your list: ")
your_list = your_list.split(sep=', ')
your_list = set(your_list)
your_list = list(your_list)
your_list.sort()
print(your_list)

# Task-6

a = (1, 2, 3)
a = list(a)
a.remove(a[len(a)-1])
a = tuple(a)
print(a)

# Task-7

list_of = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
for i in range(len(list_of)):
    list_of[i] = list(list_of[i])
print(list_of)

# Task-8

a = list(range(-99, 99, 3))
for e in a:
    if e % 3 == 0:
        print(f'это {e} делится без остатка на 3')

# Task-9
a = [1, 2, 3, 4, 5]
b = [0, -1, 3, 4, 6, 7]
for element in a:
    if element in b:
        print(element)
