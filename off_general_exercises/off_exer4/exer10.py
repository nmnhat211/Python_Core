title = ''' A là mảng chứa id của mỗi bài hát
        Output: Độ dài cần tìm'''
'''
Example:
    Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
    => Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]
'''

A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
temp_A = []
print(f'BT10:{title}\n')
print(f'Input: A = {A}')
for i in A:
    if i not in temp_A:
        temp_A.append(i) #Append object to the end of the list
print(f'--------------------')
print(f'Result of solve.')
print(f'=> Output: A = {temp_A} , length: {len(temp_A)}')
