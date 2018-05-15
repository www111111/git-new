import random
for i in range(1,11):
        suiJi=random.randint(1,100)
        a=int(input('shuru'))
        if a>101 or a<=0:
            print('输入错误')
            break
        if(a>suiJi):
            print('caidale')
            continue
        elif(a==suiJi):
            break
        else:
            print('caixiaole')
           # continue


