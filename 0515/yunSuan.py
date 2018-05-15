
def jaifa(x,y,z):
    return('x+y+z=',x+y+z)
def jianfa(x,y,z):
    return('x-y-z=',x-y-z)
def cengfa(x,y,z):
    return('x*y*z=',x*y*z)
def chufa(x,y,z):
    return('x/y/z=',x/y/z)
#def fH():
 #   if(fuHao!='+' or fuHao!='-' or fuHao!='*' or fuHao!='/'):
  #      print('qingchongxinshuru')
   #     fuHao=input('shurufuhao')


print('欢迎来到小艾超级计算机')
while(True):
    a=int(input('shurucengshu'))
    fuHao=input('shurufuhao')
    if fuHao=='exit':
        break
    b=int(input('shurubeicengshu'))
    fuHao=input('shurufuhao')
    if fuHao=='exit':
        break
    c=int(input('shurubeicengshu'))
    if(fuHao!='+' and fuHao!='-' and fuHao!='*' and fuHao!='/'):
        print('符号输入错误 请重新输入')
    if(fuHao=='+'):
        add=jaifa(a,b,c)
        print(add)
    elif(fuHao=='-'):
        jian=jianfa(a,b,c)
        print(jian)
    elif(fuHao=='*'):
        ceng=cengfa(a,b,c)
        print(ceng)
   # elif(a=='exit' or fuHao=='exit' or b=='exit'):
    #    break
    elif(fuHao=='/'):
        chu=chufa(a,b,c)
        print(chu)




