""" Student ID: 20CS076
    Student Name : AKSHAT SHAH
"""
x = input()
roomlist = input().split()
roomset = set(roomlist)

for y in list(roomset):
    roomlist.remove(y)

CAP_RO_NUM = roomset.difference(set(roomlist)).pop()
print(CAP_RO_NUM)
