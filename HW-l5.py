# Task-1
"""
passw = input('Enter your password: ')
rep_passw = input('Repeat your password: ')
if passw == rep_passw:
    print('Welcome')
else:
    while passw != rep_passw:
        rep_passw = input('Repeat your password: ')
        if passw == rep_passw:
            print('Welcome')
            break
        else:
            rep_passw = input('Repeat your password: ')
            if passw == rep_passw:
                print('Welcome')
                break
"""
# Task-2
"""
l = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
while 'eg' in l:
    l.remove('eg')
print(l)
"""
# Task-3
"""
l = [1, 22, 66, 44, 76, 534]
i = 0
s = 0
while i < len(l):
    s = s + l[i] % 2
    i += 1
if s == 0:
    print("all numbers are even")
else:
    print("NO")
"""
# Task-4
"""
l = dir(set)
l1 = []
for e in l:
    if e[0] != '_':
        l1.append(e)
print(l1)
"""
# Task-4
"""
l = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
l1 = ['c', 'a', 'b']
print(l[4::-2])
"""
# Task-5

s = {1, 2, 3}
s.add(5)
print(s)

s1 = {1, 2, 3}
s1.clear()
print(s1)

s2 = {1, 2, 3}
s3 = s2.copy()
print(s3)

s4 = {1, 2, 3}
s5 = {1, 2, 4}
print(s4.difference(s5))

s4.difference_update(s5)
print(s4)

s6 = {1, 2, 3}
s6.discard(2)
print(s6)

s7 = set('abcdef')
s8 = set('defghi')
s7.intersection_update(s8)
print(s7)

s7 = set('abcdef')
s8 = set('defghi')
s9 = s7.intersection(s8)
print(s9)

s4 = {1, 2, 3}
s5 = {5, 6, 4}
print(s4.isdisjoint(s5))

s4 = {1, 2, 3}
s5 = {5, 6, 4, 1, 2, 3}
print(s4.issubset(s5))

s4 = {1, 2, 3}
s5 = {5, 6, 4, 1, 2, 3}
print(s5.issuperset(s4))

s4 = {4, 6, 3}
print(s4.pop())

s4 = {4, 6, 3}
s4.remove(4)
print(s4)

s4 = {1, 2, 3}
s5 = {5, 6, 4, 1, 2, 3}
s6 = s4.symmetric_difference(s5)
print(s6)

s4 = {1, 2, 3}
s5 = {5, 6, 4, 1, 2, 3}
s4.symmetric_difference_update(s5)
print(s4)

s4 = {1, 2, 3}
s5 = {5, 6, 4, 1, 2, 3}
print(s4.union(s5))

s4 = {1, 2, 3}
s5 = {5, 6, 4, 1, 2, 3, 7}
s4.update(s5)
print(s4)