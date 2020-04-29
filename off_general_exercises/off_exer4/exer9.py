title = '''Tính tích của 2 ma trận vuông cấp 3. '''
A = [[1, 2],
     [3, 4]]
B = [[0, 1],
     [0, 0]]
C = [[0 for x in range(2)] for y in range(2)]

# explicit for loops
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            # resulted matrix
            C[i][j] += A[i][k] * B[k][j]

print(f'BT9: {title}')
print('Input:')
print(f'\tA = {A[0]} \n\t\t{A[1]}\n')
print(f'\tB = {B[0]} \n\t\t{B[1]}')
print('------------------')
print(f'Output: ')
print(f'\tC = {C[0]} \n\t\t{C[1]}')