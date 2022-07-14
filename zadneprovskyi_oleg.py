# Task 0

# strings
a = 'Hello'
b = 'World'
c = "I'm here"

d, e, f = 1, 2, 3 # integer

g, g1, g2 = 1.1, 5.5, 10.4 # float

# lists
my_list_1 = [1, a, 1.1]
my_list_2 = [True, b, 1.1, 'Yahoo']
my_list_3 = [my_list_1, my_list_2, False]

# dictionaries
my_dict_1 = {'age': 30, 'height': 180, 'weight': 75}
my_dict_2 = {'X0': True, 'X1': False, 'X2': True}
my_dict_3 = {1:my_list_1, 2: my_list_2, 3: my_list_3}

# tuples
t1 = (1, 2, 3)
t2 = ('h', 1, 5.5)
t3 = (True, False, None)

# sets
s1 = set()
s2 = {1, 2, 2, 3, 4, 1, 5}
s3 = {True, "str", True, 1, 2, 5}

# use max()/min()
m = max(d, e, f) # comparing of integers
m1 = max(m, g1, g2, g) # comparing of floats and integers
m2 = max(a, b, c) # comparing of strings
m4 = min(m, m1)

# use in
b = 1 in s2 # True
b1 = 10 in s2 # False
b2 = 'e' in a # True

# use if-->elif-->else
max_number = 10
if max(s2) > max_number:
    max_number = max(s2)
elif max(s2) == max_number:
    max_number = max(s2) + 1
else:
    max_number = max(s2) - 1

# -------------------------------------------------------

# Task 1
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 16 < age < 70:
    print('Welcome ' + name + ' on our website')
elif age == 16:
    print('Dear ' + name + ' you need to wait one year')
elif 70 <= age <= 90:
    print('You are lucky ' + name + ' and welcome')
elif age > 121:
    print('You are not real ' + name)
else:
    print("I'm sorry " + name + ' you are too young')

# In the task 1 we have no a logical point for the age between 91 and 121 year

# -------------------------------------------------------------------------

# Task 2
year_of_birth = input("Enter your year of birth: ")

if year_of_birth.isalpha():
    print('Please enter your age in integer format')
elif (2022 - int(year_of_birth)) == 21:
    print('You should visit Holland.')
elif (2022 - int(year_of_birth)) > 21:
    print('You should visit Vietnam.')
else:
    print('Travel everywhere')

# -----------------------------------------------------------------------------

# Task 3
print('Hello user')
name = input('What is your name: ')
sex = input('What is your sex (M or F): ')
age = input('What is your age: ')
age = int(age)

if name.find('admin') != -1:
    print('Привет, повелитель!')
elif ((10 < age < 14) and (sex == 'M')) or ((age > 30) and (sex == 'M')):
    if name == 'Guido':
        print("Советую Вам посмотреть ‘StarWars’ или 'Мандалорец'" + ' Огромное спасибо!')
    else:
        print("Советую Вам посмотреть ‘StarWars’ или 'Мандалорец'")
elif (22 < age < 32) and (sex == 'F'):
    if name == 'Guido':
        print("Советую Вам посмотреть 'Трансформеры'" + ' Огромное спасибо!')
    else:
        print("Советую Вам посмотреть 'Трансформеры'")
elif (age < 16) and (sex == 'F'):
    if name == 'Guido':
        print("Советую Вам посмотреть 'Инсургент'" + ' Огромное спасибо!')
    else:
        print("Советую Вам посмотреть 'Инсургент'")
elif name == 'Женя':
    print("Советую Вам посмотреть 'TENET'")
elif (age < 11) and (sex == 'M'):
    if name == 'Guido':
        print("Советую Вам посмотреть 'TMNT'" + ' Огромное спасибо!')
    else:
        print("Советую Вам посмотреть 'TMNT'")
