# Task-1. Написати функцію котра буде рахувати сумму зі списку чисел.
#  `ваша_функція([1, 2, 3, 4, 5, 6, 7, 8])
#  36`

def sum_from_list(your_list: list):
    s = 0
    for i in your_list:
        s += i
    return s
  
sum_from_list([1, 2, 3, 4, 5, 6, 7, 8])
#------------------------------------------
# Task-2. Написати функцію котра буде повертати сумму зі вложених списків також. Приклад
#  `ваша_.функція([1, 2, [3, 4, [5, 6], 7], 8])
#   36`
l = [1, 2, [3, 4, [5, 6], 7], 8]
def sum_from_matrix(your_list: list):
    while any(isinstance(val, list) for val in your_list):
        for i in range(len(your_list)):
            if isinstance(your_list[i], list):
                extract = your_list.pop(i)
                your_list.extend(extract)
            
    return sum_from_list(your_list)

sum_from_matrix(l)
