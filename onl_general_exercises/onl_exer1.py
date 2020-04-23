"""
# circle area
s = 0
a = float(input())
s = float(math.pi * a**2)   # add lib: import math
print("s = ",round(s,2))    # round a number to only two decimals

# medium score
so_diem_10= 5
so_diem_9= 7
so_diem_8= 12
tong_diem=  so_diem_10*10 + so_diem_9*9 + so_diem_8*8
so_hs = so_diem_10 + so_diem_9 + so_diem_8
print("TB = ",round((tong_diem / so_hs),2))

"""
# print string first and last name
first_name = input("1.Enter ur first name: ")
last_name = input("2.Enter ur last name: ")

print(last_name +" "+ first_name)
print('%s %s' % (last_name, first_name))
print('{} {}'.format(last_name, first_name))
print('{last} {first}'.format(first=first_name, last=last_name))
