import math
p=0.5
x=0.25





jiaoT=input(' B D')
km=int(input('shuru km'))
yh=input('shuru p or x')
if jiaoT== 'B':
    if(yh==p):
        if(km<=10):
            print(2*p)
        else:
           print( (2+math.ceil((km-10)/5))*p)

    elif(yh=='x'):
        if(km<=10):
            print(2*x)
        else:
            print((2+math.ceil((km-10)/5))*x)
    if(km<=10):
        print('2 yuan')

    else:
       print (2+math.ceil((km-10)/5))

Zong=0
a=0
b=0
c=0
d=0
if jiaoT== 'D':
    if(yh=='p'):
        if(km<=6):
            a=3*p
            print(a)
        elif( km>6 and km<=12):
            b=4*p
            print(b)


        #eiif(km>12) and( km<=22):
            print('5 yuan')
        elif (km >22 and km<=32):
            c=6*p
            print(c)
        else:
           d=(6+math.ceil((km-32)/20))*p
           print(d)
    Zong=a+b+c+d
    if(Zong>=200):
        print('aaaaaa')
    elif(yh=='x'):

        if(km<=6):
            print('3 yuan')
        elif (km>6 and km<=12):
            print('4 yuan')
       # eiif (km>12 and km<=22):
            print('5 yuan')
        elif (km >22 and km<=32):
            print('6 yuan')
        else:
           print( (6+math.ceil((km-32)/20))*x)


    else:
        if(km<=6):
            print('3 yuan')
        elif( km>6 and km<=12):
            print('4 yuan')
   # eiif (km>12 and km<=22):
            print('5 yuan')
        elif (km >22 and km<=32):
            print('6 yuan')
        else:
            print(6+math.ceil((km-32)/20))













