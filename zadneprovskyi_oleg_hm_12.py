# Написать 3 примера генераторных функций с различными последовательностями.
def my_gen_1(val):
    for x in val:
        yield x
        
for i in my_gen_1('Hello'):
    print(i)
    
#------------------------------------------------------------------------
def my_gen_2(num):
    if num >= 0:
        for x in range(0, num, 1):
            yield x
    else:
        for x in range(num, 0, 1):
            yield x
            
for i in my_gen_2(-10):
    print(i)
#------------------------------------------------------------------------

def my_gen_3(l1, l2):
    d = {}
    for x, y in zip(l1, l2):
        d[x] = y
        yield d.items()

list1 = list(range(10))  
list2 = [x * 2 for x in list1]

for i in my_gen_3(list1, list2):
    print(i)
    
# Написать свою реализацию функции reduce() с описанием ее работы в однострочных и многострочных комментариях.
def add(x, y):
    return x + y


def my_reduce(func, coll, st = None):
    if st == None:
        res = coll[0]
    else:
        res = st
    for i in range(1, len(coll)):
        res = func(res, coll[i])
    return res

#print(my_reduce(add, [1, 2, 3, 4]))
print(my_reduce(add, ['h', 'e', 'l', 'l', 'o'], 'H'))

# Написать функцию которая с помощью assert будет тестировать ваш самопистный reduce


# Создать класс с методом которого можно будет возвращать область видимости(local) созданного экземпляра класса.
class Test:
    val1 = 1
    val2 = 2
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        
    def get_view():
        
