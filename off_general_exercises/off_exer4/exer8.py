
title = ''' Cho list các số nguyên dương A. Đếm số lượng tập gồm 2 phần tử:
    A[i] và A[j] thỏa mãn A[i] > A[j] và i < j. '''


print(f'BT8:{title}\n')
A = [6, 1, 3, 8, 8, 9, 1]
count = 0
for i in range(len(A)-1):
    j = i+1
    if A[i] > A[j] and i < j:count += 1
print(f'Input: A = {A}')
print('----------------')
print(f'Result of correct element is = {count}')