import random
shuRu='go'
while shuRu=='go':
    pc=random.randint(1,3)
#print(pc)
    if(pc==1):
        pcStr='石头'
    elif(pc==2):
        pcStr='剪刀'
    else:
        pcStr='布'
    shiTou='石头'
    jianDao='剪刀'
    bu='布'
    user=input('猜拳')
    if user=='exit':
        shuRu='exit'
    if(pc==1):

        print('电脑出了石头')
    elif(pc==2):

        print('电脑出了剪刀')
    elif(pc==3):

        print('电脑出了布')
#pc=1;
#user=int(input('猜拳'))
    if(user==shiTou):
        print('玩家出了石头')
    elif(user==jianDao):
        print('玩家出了剪刀')
    elif(user==bu):
        print('玩家出了布')
  #  else:
   #     print('重新输入')
       # q='石头'
       # j='剪刀'
       # b='布'
    if(user==shiTou and pc==2) or (user==jianDao and pc==3) or (user==bu and pc==1):
        print('win')
    elif user==pcStr:
        print('level')
   # elif user<4:
       # print('lose')
    else:
        print('lose')
