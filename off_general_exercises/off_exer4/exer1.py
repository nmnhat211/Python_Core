title = ''' Tính tổng, tích của các phần tử trong một list.'''

print(f'BT1:{title}')
s = 0
m = 1

input_string = input("Enter a list numbers: ")
userList = input_string.split()
for temp in userList:
    s += int(temp) # s: sum sequence in list
    m *= int(temp) # m: multiply

print('---------------')
print(f'Result: S = {s} ,\tM = {m},\tL = {len(userList)}')


