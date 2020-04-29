#Session4
#Date = 26/4/2020
#Subject: List

input_string = input("Enter a list numbers: ")
userList = input_string.split()
print('max: ', sorted(userList)[0])
print('max: ', sorted(userList)[-1])


# min_str = userList[0]
# max_str = ''
#
# for i in range(len(userList)):
#         if max_str < userList[i]:
#             max_str = userList[i]
#         elif min_str > userList[i]:
#             min_str = userList[i]
#             continue
# print(f'Result: Min = {min_str}, Max = {max_str}')
# sum1 = 1
# sum2 = 1
# for temp in userList:
#     sum1 += int(temp)
#     sum2 *= int(temp)
# print(f'{sum1} ,{sum2}')

# food =["cơm", "cá", "trứng", "gà"]
# for i in range(len(food)):
#     print('Tôi muốn ăn: ', food)




# my_list = [0, 3, -2, 4, 5]
# my_list.sort(key=abs)
# print('Result: ', my_list)




# l = [i for i in range(30)]
# a = [[1, 2, 3],[1, 2, 3]]
# b = list(a)
# b[0][1] = 'Text'
# print(a)
# print(b)

# input_string = input("Enter a list numbers or elements separated by space: ")
# userList = input_string.split()
# print("user list is ", userList)
#
# # print("Calculating sum of element of input list")
# sum = 0
# for num in userList:
#     sum += int(num)
# print("Sum = ", sum)