def jaifa(x,y):
    return('x+y=',x+y)
def jianfa(x,y):
    return('x-y=',x-y)
def cengfa(x,y):
    return('x*y=',x*y)
def chufa(x,y):
    return('x/y=',x/y)
print('欢迎来到小艾超级计算机')
while(True):
    a=int(input('shurucengshu'))
    fuHao=input('shurufuhao')
    while(fuHao!='+' and fuHao!='-' and fuHao!='*' and fuHao!='/' and fuHao!= 'q'):
        print('符号输入错误 请重新输入')
        fuHao=input('shurufuhao')
    if(fuHao=='q'):
        break
    b=int(input('shurubeicengshu'))
    if(fuHao=='+'):
        print(jaifa(a,b))
    elif(fuHao=='-'):
        print(jianfa(a,b))
    elif(fuHao=='*'):
        print(cengfa(a,b))
    elif(fuHao=='/'):
        print(chufa(a,b))




