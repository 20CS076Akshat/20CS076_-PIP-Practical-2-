""" Student ID: 20CS076
    Student Name : AKSHAT SHAH
"""
num = int(input())
lists = map(int, input().split(' '))
new_list = []
for i in lists:
    new_list.append(i)

new = []
for i in new_list:
    if i not in new:
        new.append(i)

sort = sorted(new)
print(sort[-2])
