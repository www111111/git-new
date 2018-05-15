import random
while(True):
    pc=random.randint(1,3)
#print(pc)
    user=int(input('猜拳'))
    if(pc==1):
        print('电脑出了石头')
    elif(pc==2):
        print('电脑出了剪刀')
    elif(pc==3):
        print('电脑出了布')
#pc=1;
#user=int(input('猜拳'))
    if(user==1):
        print('玩家出了石头')
    elif(user==2):
        print('玩家出了剪刀')
    elif(user==3):
        print('玩家出了布')
    else:
        print('重新输入')
    if(user==1 and pc==2) or (user==2 and pc==3) or (user==3 and pc==1 ):
        print('win')
    elif user==pc:
        print('level')
    elif user<4:
        print('lose')
    else:
        print('重新输入')
