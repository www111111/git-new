def jaifa(x,y):
    return x+y
def jianfa (x,y):
    return x-y
def cengfa(x,y):
    return x*y
def chufa(x,y):
    return x/y
print('欢迎来到小艾超级计算机')
a=int(input('shurucengshu'))
while(True):
    fuHao=input('shurufuhao')
    while(fuHao!='+' and fuHao!='-' and fuHao!='*' and fuHao!='/' and fuHao!= 'q'):
        print('符号输入错误 请重新输入')
        fuHao=input('shurufuhao')
    if(fuHao=='q'):
        break
    b=int(input('shurubeicengshu'))
    if(fuHao=='+'):
        a=jaifa(a,b)
        print(a)
    elif(fuHao=='-'):
        a=jianfa(a,b)
        print(a)
    elif(fuHao=='*'):
        a=cengfa(a,b)
        print(a)
    elif(fuHao=='/'):
        a=chufa(a,b)
        print(a)




