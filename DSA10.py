def exconse(a):
    sum1=0
    while a:
        k=(a%10)*10
        a=a//10
        k=k+(a%10)
        if a%10==0:
            break
        sum1+=k

        # print(k)
    print(sum1)

a =24159
exconse(a)
