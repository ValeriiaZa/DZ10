import keyword
import string
x = input('Write a str:')
b = keyword.kwlist
c = '''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''
for i in x:
    if (x[0].isdigit()):
        print('False')
        break
    elif (x.isdigit()):
        print('False')
        break
    elif(i.isupper()):
        print('False')
        break
    elif (x in b[:]):
        print('False')
        break
    elif (i in c):
        print('False')
        break
    elif (' ' in x):
        print('False')
        break
else:
    print('True')


