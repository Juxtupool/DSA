def sndlst(a):
    count=0
    while a:
        k=a%10
        if k%2==0:
            count+=1
            if count==2:
                print(k)
                break
            
        a=a//10

a=20582
sndlst(a)