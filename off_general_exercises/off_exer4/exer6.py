
title = '''Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau'''
print(f'BT6: {title}\n')
while True:
    A = input('Enter a list A: ')
    A = A.split()
    if len(A) <= 2 or A[0] != A[-1]:
        print('Enter again!!!')
    else:
        print(f'---------------')
        print(f'Result of solve:')
        print(f'- A= {A}, length = {len(A)} ')
        print(f'- Fist and last index is {A[0]} : {A[-1]}')

        break