#Addition string
a = int(input("Input an integer : "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))

print(f'n1 = {n1}')
print(f'n2 = {n2}')
print(f'n3 = {n3}')
print('-------------')
print (f'Result: {n1+n2+n3}')