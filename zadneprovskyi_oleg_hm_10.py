# Task-0 Замыкания просмотреть и повторить за автором. мне скинуть файлик с повтором или своим примером
def func():
    x = 10
    def inner_f(y):
        return x * y
    return inner_f

z = func()
z(3)

# Task-1 Написать функцию которая будет добовлять код страны к номеру телефона с помощью замыкания
def user_telephone(code: str):
    def inner(number: str):
        return code + number
    return inner

my_number = user_telephone('+044')
my_number('838372893')


# Task-2 Написать функцию которая будет у пользователя брать python обект в любом виде и выводить все его не магические методы в списке.
# Написать декторатор который будет выводить колличество методов в объекте.

def decor(str_obj: str):
    def inner_func(function):        
        def wrapper(obj):
            methods = function(obj)
            amount = len(methods)
            return str_obj + ' ' + str(amount)
        return wrapper
    return inner_func

@decor('need to learn')        
def object_methods(obj):
    list_of_m = dir(obj)
    new_list = []
    for method in list_of_m:
        if method[0] != '_':
            new_list.append(method)
    return new_list

object_methods([])
