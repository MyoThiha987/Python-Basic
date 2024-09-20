# Exception
class JustNotCoolError(Exception):
    pass
x = 2
try:
    raise JustNotCoolError('This just isn\'t cool, man')
    # if not type(x) is str: raise TypeError('Only strings are allowed! ')
except NameError:
    print('Name error mean something is probably undefined!')
except ZeroDivisionError:
    print('Please do not divide by zero')
except Exception as error:
    print(f'{error}')
else:
    print('No error!')
finally:
    print('I am going to print with error or without error!')