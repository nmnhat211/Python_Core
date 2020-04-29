import random
title = ''' Tạo list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc. '''
A = [1, 2, 3, 4, 5, 6, 7]
B = random.choices(A, k=5) # choice != choices
print(f'BT0: {title} ')
print(f'Input: A = {A}')
print('----------------')
print(f'Result of solve: ')
print(f'=> Output: B = {B} ')