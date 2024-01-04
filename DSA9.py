def Consec(a):
    sum1=0
    while a:
        k=a%100
        if a%100<10:
        	break
        sum1+=k
        #print(k)
        a=a//10
    print(sum1)
a=24159
Consec(a)