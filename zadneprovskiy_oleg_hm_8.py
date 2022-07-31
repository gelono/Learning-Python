import datetime
# Task-1 Написать функцию которая будет принимать 3 аргумента (int) и находить максимум из них
def max_of_value(a, b, c):
    return max(a, b, c)
print(max_of_value(3, 5, 10))
""""
Task-2 Написать функцию которая будет принимать 2 аргумента (int) и находить максимум из них.
Затем используя функцию1 (вызвать ее) написать функцию2 которая будет принимать 
3 аргумента и находить максимум с помощью функции1.
"""
def max_of_value_2x(a, b):
    return max(a, b)

def max_of_value_3x(a, b, c):
    mid = max_of_value_2x(a, b)
    return max_of_value_2x(mid, c)

print(max_of_value_3x(3, 5, 20))
# Task-3 Lambda function. с помощью Анонимной функции остортировать список кортежей по цифре.

my_list = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
my_list.sort(key = lambda el_in_list: el_in_list[1])
print(my_list)
# Task-4 познакомиться с модулем datetime и написать программу с помощью lambda для возвращение
# текущего года, месяца , дня

now = datetime.datetime.now()
year = lambda now: [now.year, now.month, now.day]
print(year(now))

# link to the documentation: https://docs.python.org/3/library/datetime.html#date-objects