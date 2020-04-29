title = ''' Chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím. '''
print(f'BT4:{title}')

A, B = [], []
print('S = [A, B]')
lenght_input = int(input('Length of A: '))
while 69:

    A = input('Enter a list of A: ')
    A = A.split()
    if len(A) > lenght_input or len(A) < lenght_input:
        print(f'The length of A must be {lenght_input}, ', end='')
        print(f'curent is = {len(A)}, enter again!  !!! ')
    else:
        break

B = input("Enter a list of B: ")
B = B.split()
S = [A, B]
print('--------------')
print(f'Result: [A,B] = {S}')
