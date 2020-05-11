# -*- author:caoyue -*-
# a = [1,2,3]
# def func(a,b):
#     a.append(b)
#
# func(a, 3)
# print(a)

people_list = [
    {'name': 'lili', 'age': 18},
    {'name': 'xm', 'age': 17},
    {'name': 'lm', 'age': 19}
]

for i in range(len(people_list)-1):
    for j in range(len(people_list)-1-i):
        if people_list[j].get('age') < people_list[j+1].get('age'):
            people_list[j], people_list[j+1] = people_list[j+1], people_list[j]

print(people_list)