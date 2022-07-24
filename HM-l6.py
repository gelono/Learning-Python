# Task-1--------------------------------------------------------------
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}

total_d = {}
l = [first, second, third, fourth, fifth]
for d in l:
    total_d.update(d)
print(total_d)

# Task-2--------------------------------------------------------------
my_dict = {}
keys = list(range(11, 21))
for e in keys:
    my_dict[e] = e ** 2
s = sum(list(my_dict.values()))
print(s)

# Task-3--------------------------------------------------------------
my_d = {"b": 20, "f": 6, "c": 3, "a": 30, "e": 5, "d": 4}
a = list(my_d.items())
a.sort()
my_d.clear()
my_d.update(a)
print(my_d)

# Task-4--------------------------------------------------------------
my_dict = {'id1':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
},
'id2':
{
'name': 'Mark',
'class': 2,
'subjects' : {'Geometry', 'Java', 'Cooking'}
},
'id3':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
}
}
new_dict = {}
l = list(my_dict.items())
k = list(my_dict.keys())
for i_k, i_l in zip(k, l):
    if i_l[1] not in list(new_dict.values()):
        new_dict[i_k] = i_l[1]
        
print(new_dict)

# Task-5-------------------------------------------------------------
my_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
list_of_values = []
list_of_keys = []
temp_list = []
new_list = []
for i in my_list:
    list_of_values.append(list(i.items())[0][1])
    list_of_keys.append(list(i.items())[0][0])
    
for v, k in zip(list_of_values, list_of_keys):
    if v not in temp_list:
        temp_list.append(v)
        new_list.append(dict([(k, v)]))
print(new_list)

# Task-6-------------------------------------------------------------
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
count = 0
for i in shedule:
    if type(shedule[i]) == list:
        count += len(shedule[i])
print(count)
