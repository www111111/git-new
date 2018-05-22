import random
lis=[]
lis1=[]
def system():
    print('*'*30,end='\n\t')
    print('欢迎使用无人餐厅管理系统',end='\n\t')
    print('1.输入您要点菜名',end='\n\t')
    print('2.付款',end='\n\t')
    print('3.会员服务中心',end='\n\t')
    print('0.退出系统')
    print('*'*30)
def dianCai():
    dic={}
    print('*'*30)
    print('1.查看菜单')
    print('2.选择菜品')
    print('3.查看菜单')
    print('4.删除所选菜品')
    print('5.返回上级菜单')
    print('*'*30)
    while(True):
        zjL=int(input('根据提示选择点菜子菜单'))
        if(zjL==1):#如果中间变量=1，显示如下菜单
            print('*'*30)
            print('1.西红柿鸡蛋  20RMB')
            print('2.锅包肉      30RMB')
            print('*'*30)
        if(zjL==2):#如果中间变量=2,显示选择菜品菜单
            while(True):#循环选择
                print('*'*30)
                caiMingI=int(input('请输入要点的菜名的编号 \t'))
                kouWeiI=input('请输入菜的口味 辣/微辣/不辣 \t')
                dic={'caiMing':caiMingI,'kouWei':kouWeiI}#将输入的value存到字典
                lis.append(dic)#将字典存到列表
                print('*'*30)
                panD=input('是否选好菜 输入 Y/N')#判断是否选好菜，选好即可跳出循环
                if (panD=='Y'):
                    break
                print('*'*30)
        if(zjL==3):
            displayAll()
        if(zjL==4):
            delete()
        if(zjL==5):
            print('返回上级菜单')
            break
def delete():
     print('*'*30)
     dCi=int(input('输入菜名字 \t'))
     print('请删除 %s 菜名' % dCi)
     for dic in lis:#循环遍历查找dic
         print(dic)
         if dic['caiMing'] == dCi: #判等的输入菜单名字是否在字典中
             print(dic)
             lis.remove(dic)#如果在，则删除此字典
             print(lis)
     print('删除 %s 成功' % dCi)
     print('*'*30)


def fuKuanZ():#付款函数调用现金付款函数和刷卡付款函数
    print('*'*30)
    print('1.现金付款')
    print('2.刷卡付款')
    print('3.退出菜单')
    zjL=int(input('根据提示选择相应的付款方式'))
    if(zjL==1):
        fuKuan()
    elif(zjL==2):
        shuCard()
    #elif(zjl==3):
     #   break
    print('*'*30)



def huiY():#会员函数，调用办理会员卡函数和会员卡充值函数
    print('1.办理会员卡')
    print('2.会员卡充值')
    coo=int(input('根据提示输入相应选项'))
    if coo==1:
        banKa()
    else:
        cunKuan()


zl=0
zl1=0
def fuKuan():
   # print('*'*30)
    for dic in lis:
        if dic['caiMing']==1:
           # lis.remover(dir)
            mony=int(input('西红柿鸡蛋 20 元 请输入'))
            print('付款成功')
            if mony>20:
                global zl
                zl=mony-20
        else:#(dir['caiMing']=='gbr'):
            mony=int(input('锅包肉 30 元 请输入'))
            print('付款成功')
            if mony>30:
                global zl1
                zl1=mony-30
    zlz=zl+zl1
    print('找零 %d 元' %zlz)
   # print('*'*30)

def displayAll():
    print('*'*30)
    print('所点菜名如下 ： ')
    for a in lis:
        print('菜名 :%s '% a['caiMing'])
        print('口味 :%s '% a['kouWei'])
        print('已显示所有菜单')
    print('*'*30)


money=0
money1=0
money2=0
def shuCard():

   # card_num=input('输入卡号')
   # passwd=int(input('输入密码'))
    if money<=0:#判断账户中的钱是否有余额
        global money
        money=int(input('充值款'))#输入充值金额
    #huiyuanYz()
    #if card_num=='www' and passwd==123:#判断密码和账户是否匹配

    name=input('输入会员帐号')
    pas=int(input('输入会员密码'))
    for dic1 in lis1:
        if (dic1['name']==name) and (dic1['pas']==pas):
            for dic in lis:
                if(dic['caiMing']==1):#判断所选择的菜为1.西红柿鸡蛋
                    if(money<20):#因为菜价金额为20,不足的话会跳到主界面，可进行充值
                        print('您余额不足请充值，系统将自动为您退出到主界面')
                        break
                    print('西红柿鸡蛋 20 元 刷卡成功')
                    money=money-20#进行余额计算
                else:
                    if  money<30:
                        print('您余额不足请充值，系统将自动为您退出到主界面')
                        break
                    print('锅包肉 30 元 刷卡成功')
                    money=money-30
            print('卡内余额 %d 元' %money)
        else:
            print('密码/帐号错误重新输入')
'''
def banKa():
    print('现在办理会员卡业务')
    sJacc=random.randint(100,999)
    print(sJacc)
    pas=input('输入会员密码')
    print('办卡成功')
'''

def banKa():
    dic1={}
    print('办理会员卡业务')
    name=input('设置会员帐号')
    pas=int(input('设置会员密码'))
    dic1={'name':name,'pas':pas}
    lis1.append(dic1)
    print(lis1)
    print('办理会员卡成功')



def cunKuan():
    print('*'*30)
    global money
    if money<=0:
        print('卡内余额不足')
        print('请充值')
        jeIn=int(input('请冲入金额'))
        money=money+jeIn
        print('卡内余额 %d' %money)
    else:
        jeIn=int(input('请冲入金额'))
        money=money+jeIn
        print('卡内余额 %d' %money)

    print('*'*30)

while(True):#while的主函数
    system()
    print('*'*30)
    coo=int(input('根据提示输入相应编号'))
    if(coo==1):
        dianCai()
    if(coo==2):
        fuKuanZ()
    if(coo==3):
        huiY()
    if(coo==0):
        print('-^ ^-'*7)
        print('已退出系统,欢迎下次光临')
        print('-^ ^-'*7)
        break
    print('*'*30)







