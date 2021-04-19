try:
    x=int(input('Enter ONe Number:'))
    y=int(input('Enter Anoher Number:'))
    result=x/y
    print('Result:',result)
except ZeroDivisionError:
    print('Zero Can Not Be Divisible')
# finally:
#     print('Program Executed')
else:
    print('Programme Executed')