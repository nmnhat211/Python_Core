title = ''' Tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.'''

A = [1, 2, 3, 4]
print(f'BT3:{title}')
print(f'Input: A = {A}')
print('----------- ')
B = [print('Number: ', A[i]) for i in range(len(A))]
print('type of B: ', type(B))