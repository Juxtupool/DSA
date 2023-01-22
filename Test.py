
def case(n):
    str1=str(n)
    for i in str1:
        if i.islower():
            print(i.upper(),end='')
        else:
            print(i.lower(),end='')

n=input('Enter a Random String')
case(n)
