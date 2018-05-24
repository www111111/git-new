'''
import time
import random
while(True):
    a=random.randint(1,100)
    c=random.randint(1,100)
    b=a*' '
    print(b+'$')
    time.sleep(0.3)
    print(c*' ','钱来了')
'''
'''
a=lambda a,b: a+b
print(a(1,2))

f=lambda a,b :a+b
q=f(1,1)
x=int(input('shur'))
a=lambda a,b,c,d :(a+b-c)*d
print(a(q,3,2,x))
'''
l=[(lambda a=1,b=2:a*b),(lambda a,b :a+b),(lambda a,b,c :(a+b)*c-2 ),(lambda a,b=1 :a*b)]
print(l)
'''
print(l[0](1,2))
print(l[1](1,1))
print(l[2](1,1,3))
print(l[3](2))
print(l[0](1,2),l[1](1,1),l[2](1,1,3),l[3](2))
print(l)
'''




