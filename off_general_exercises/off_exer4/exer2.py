# BT2: Tìm số lớn nhất, nhỏ nhất trong một list.

print('BT2:')
input_string = input("Enter a list numbers: ")
userList = input_string.split()
print('Min: ', sorted(userList)[0]) # Sorted: Return a new list, all items from the iterable in ascending order.
print('Max: ', sorted(userList)[-1])