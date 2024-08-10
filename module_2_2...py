#first, second и third
print('введите данные first:')
first= ('веденное сисло =',int(input()))
print('введите данные second:')
second =('веденное сисло =', int(input()))
print('введите данные third')
third=('веденное сисло =', int(input()))
print('выполняется программа')

if first==second and third: # и
    print(3)
elif first==second:
    print(2)
elif second==third or first==third:
    print(2)
else:                       # иначе
    print(0)




