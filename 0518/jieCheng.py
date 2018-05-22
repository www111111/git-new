



def jieC(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    print(a)
jieC(100)



'''
def jieC1(n):
    a=1
    while(n>0):
        a=n*a
        n=n-1
    print(a)

jieC1(3)
'''


def diGui(x):
    h=0
    if(x>=1):
        h=x*diGui(x-1)
    else:
        h=1
    return(h)

g=diGui(100)
print(g)


