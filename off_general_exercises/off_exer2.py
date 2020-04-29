# Sesion2_exercises
#DATE: 19/4/2020 by nmnhat

""" Bài tập về nhà:
Bài 1. Lập chương trình thực hiện công việc sau:
    Nhập ba số a, b, c bất kì từ bàn phím
    Giải nghiệm phương trình bậc 2: ax^2 + bx + c = 0  (Kể cả trường hợp a=0)
    
Bài 2. Lập chương trình tính các tổng sau:
    S_1 = 1 + x + x^2 + x^3 + ... + x^n 
    S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n 
    S_3 = 1 + \dfrac{x}{1!} + \dfrac{x}{2!} + ... + \dfrac{x^n}{n!}
    Trong đó, n là số nguyên dương và x là một số thực bất kì. Cả 2 đều được nhập từ bàn phím
    
Bài 3. Lập chương trình thực hiện các công việc sau:
    Nhập 1 số nguyên dương n bất kì (n<1000). Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại.
    Tính tổng các chữ số của số đó.
    Hiển thị kết qủa ra màn hình
    
Bài 4. Lập trình thực hiện các công việc sau:
    Nhập 3 số a, b, c bất kì
    Hãy kiểm tra xem ba số đó có phải là độ dài của các cạnh của một tam giác hay không? 
    Nếu đúng là tam giác thì xác định là tam giác vuông hay không?
"""
import math

#BT1
# print('BT1')
# a, b, c = int(input('a = ')), int(input('b = ')), int(input('c = '))
# Denta = 0
# Denta = b * b - 4 * a * c
#
#
# if (a == 0) and (b == 0) and (c == 0):
#     print('-------------')
#     print('Phuong trinh vo so nghiem!')
#
# elif (a == 0):
#     print('-------------')
#     print('Phuong trinh co mot nghiem: x = ', round(-c/b, 2))
#
# elif (Denta == 0):
#     x = (-b/2*a)
#     print('-------------')
#     print('Phuong trinh co nghiem kep: \n')
#     print('x1 = x2 = ', x)
#
# elif Denta > 0:
#     x1 = float((-b - (math.sqrt(Denta))) / (2 * a))
#     x2 = float((-b + (math.sqrt(Denta))) / (2 * a))
#     print('-------------')
#     print('Phuong trinh co hai nghiem: \n')
#     print('x1 = ', round(x1, 2))
#     print('x2 = ', round(x2, 2))
#
# else:
#     print('-------------')
#     print('Vo nghiem!')


#
# BT2
# print('BT2')
# S1, S2, S3 = 0, 0, 0
# i = 0
# while 69:
#     print(end='Nhập n =  ')
#     n = int(input())
#
#     if(n >= 0):
#         x = float(input('Nhập x = '))
#         while i < n + 1:
#             S1 += x ** i
#             S2 += (-x) ** i
#             S3 += x ** i / (math.factorial(i))
#             i += 1
#         break
#     print('Giá trị của n phải lớn hơn 0!')
# print('-------------')
# print('S1 = ', math.ceil(S1))
# print('S2 =', math.ceil(S2))
# print('S3 =', round(S3, 2))


# #BT3
# while 69:
#     print(end='Nhập n =  ')
#     n = int(input())
#     if(0 <= n < 1000):
#         SUM = ((1 + n) * n) / 2
#         print('KQ: S = ', math.ceil(SUM))
#         break
#     print('Nhập lại n!')


#BT4
while 69:
    a, b, c = int(input('a = ')), int(input('b = ')), int(input('c = '))
    n1 = a**2
    n2 = b**2
    n3 = c**2

    if(a < 0 or b < 0 or c < 0):
        print('Độ dài của tam giác không được âm!')

    elif(n1 == n2 + n3 or n2 == n1 + n3 or n3 == n1 + n2):
        print('-------------')
        print('Đây là một tam giác vuông có cạnh huyền là:')
        if(n1 > n2 and n1 > n3): print('a = ', a)
        else: print('b = ', b) if n2 > n1 and n2 > n3 else print('c = ', c)
        break

    else:print('Khong phai la tam giac vuong!')

        
