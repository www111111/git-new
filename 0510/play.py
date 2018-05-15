import random
pc=random.randint(1,3)
#pc=1
user=int(input('请输入123')
        if (user==1 and pc==2) or (user==2 and pc==3) or (user==3 and pc==1) :
    print('win')
elif user==pc:
    print('0')
else:
    print('lose')



