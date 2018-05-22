
x=0.25
p=0.5
a=input('xuanze detie or bus')
b=input('xuanze buscard or studentcard shur x  p')
c=int(input('shuru gongli shu'))
if b=='x':

else:


if a=='detie':
    if c<=6:
        print('detie huafei 3 yuan')
    elif c>6 and c<=12:
        print('detie huafei 4 yuan')
    elif c>22 and c<=32:
        print('detie huafei 6 yuan')
    else:
        e=6+(c-22)//20
        print(e)
else:
    if c<10:
        print('bus huanfei 2yuan')
    else:
        if(2+(c-10)/5==0):
           d=2+(c-10)/5
           print(d)
        else:
            d=2+(c-10)//5+1
            print(d)





