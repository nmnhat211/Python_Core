# Sesion3_exercises
#Date = 21/4/2020

'''
BÀI TẬP VỀ NHÀ BUỔI 03 - String

Viết chương trình:
BT1:  Thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.

BT2: Xoá bỏ ký tự thứ m trong chuỗi không rỗng
     Với m là số không âm, nhập từ bàn phím.

BT3: Xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.

BT4: In ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào
     Nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.

BT5: Tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.

BT6: In ra chuỗi ngược,
     Ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
'''

print('BT1')
Str = input('Str = ')
temp = ''
for i in range(len(Str)):

    if(Str[i] == Str[0]):
        print('-----------')
        print(f'Replace: {Str[0]}')
        print('Result: ', Str.replace(Str[0], '$')) # Replace Str[0] = $
        break

# print('BT2')
# while 9999:
#     Str = input('Str = ')
#     if(Str != ''):
#         print('-----------')
#         print(end='Result: ')
#         for i in range(len(Str)):
#             if Str[i] < '0' or Str[i] > '9':
#                 print(end=Str[i])
#         break
#     print('Nhập lại!')


# print('BT3')
# while 9999:
#     Str = input('Str = ')
#     if(Str != ''):
#         print('-----------')
#         print(end=f'Result: {Str[::2]}')
#     break
#     print('Nhập lại!')


# print('BT4')
# while 9999:
#     Str = input('Str = ')
#     if len(Str) > 2:
#         print('-----------')
#         print(f'Result: {Str[:2],Str[-2:]}')
#         # Str[i, j]: i begin, j:end
#         # Str[:2] begin of Str to: j-1, j = 2
#         # Str[-2:] begin i to end, i = -2
#         break
#     print('Chuỗi rỗng, xin nhập lại!')

# print('BT5')
# Str = input('Str = ')
# min_str = Str[0]
# max_str = ''
#
# for i in range(len(Str)):
#         if max_str < Str[i]:
#             max_str = Str[i]
#             if min_str > Str[i]:
#                 min_str = Str[i]
#             continue
# print('-----------')
# print(f'Result: Min = {min_str}, Max = {max_str}')

# print('BT6')
# Str = input('Str = ')
# print('-----------')
# print(f"Result: {Str.swapcase()}")
