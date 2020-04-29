title = ''' Kiểm tra 2 list có phần tử chung hay không.'''

my_crush = [1, 'Taiwan', 'Student', 'Beauty', 'Talent']
me = [0, 'VietNam', 'Student']

print(f'BT7:{title}\n')
print('Input:')
print(f'\t\tMy Cush = {my_crush}')
print(f'\t\tMe = {me}')
same = []

for i in my_crush:
    for j in me:
        if i in same:
            break
        elif i == j:
            same.append(i)

print('--------------')
print(f'Output: {same}')

