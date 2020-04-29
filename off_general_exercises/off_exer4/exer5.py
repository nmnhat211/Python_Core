
title = ''' In ra phần tử có số lần xuất hiện nhiều nhất trong một list.
Phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
'''
print(f'BT5: {title}')
A = [2, 3, 2, 3, 999999999, 3, 3, 8]
max = 0
value = 0
for i in A:
    if max < A.count(i):
        max = A.count(i)
        if value < max:
            value = A[i]
print(f'Input: A = {A}')
print('-----------------')
print(f'Result: Value = {value}, max count = {max}')