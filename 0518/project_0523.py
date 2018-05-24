import random
lis=[]#存放所点菜品的列表
lis1=[]#办卡用存储账户和密码所用列表
def system():#人性化显示主菜单
    print('*'*30)
    print('欢迎使用街边早餐自助管理系统 --- 1388888888')
    print('店内优惠活动：现在办理会员卡可享受全店商品5折优惠！',end='\n\t')
    print('1.输入您要点菜名',end='\n\t')
    print('2.付款',end='\n\t')
    print('3.会员服务中心',end='\n\t')
    print('0.退出系统')
    print('*'*30)
def dianCai():#点菜函数
    dic={}#定义一个空字典
    print('*'*30)
    print('1.查看销售菜品')
    print('2.选择菜品')
    print('3.查看已点菜单')
    print('4.删除所选菜品')
    print('5.返回上级菜单')
    print('*'*30)
    while(True):
        zjL=int(input('根据提示选择点菜子菜单'))
        if(zjL==1):#如果中间变量=1，显示如下菜单
            print('*'*30)
            print('1.手抓饼        20RMB')
            print('2.煎饼果子      30RMB')
            print('*'*30)
        elif(zjL==2):#如果中间变量=2,显示选择菜品菜单
            while(True):#循环选择
                print('*'*30)
                caiMingI=int(input('请输入要点的菜名的编号 \t'))
                kouWeiI=input('请输入菜的口味 辣/微辣/不辣 \t')
                dic={'caiMing':caiMingI,'kouWei':kouWeiI}#将输入的value 菜名以及口味 存到字典
                lis.append(dic)#将字典存到列表
                print('*'*30)
                panD=input('是否选好菜 输入 Y/N')#判断是否选好菜，选好即可跳出循环
                if (panD=='Y'):
                    break
                print('*'*30)
        elif(zjL==3):
            displayAll()#功能 显示所点菜品
        elif(zjL==4):
            delete()#功能 删除所点菜品
        elif(zjL==5):
            print('返回上级菜单')
            break


def displayAll():#显示菜品函数
    print('*'*30)
    print('所点菜名如下 ： ')
    for a in lis:    #遍历列表查找相应的菜单
        print('菜名 :%s '% a['caiMing'])
        print('口味 :%s '% a['kouWei'])
        print('已显示所有菜单')
    print('*'*30)

def delete():#删除菜品函数
     print('*'*30)
     dCi=int(input('输入菜名字 \t'))
     print('请删除 %s 菜名' % dCi)
     for dic in lis:#在列表中循环遍历查找dic（所查键值为输入的键值  根据键值查找对应的字典）
         if dic['caiMing'] == dCi: #判等的输入菜单名字是否在字典中
             lis.remove(dic)#如果在，则删除此字典
     print('删除 %s 成功' % dCi)
     print('*'*30)


def fuKuanZ():#付款函数 调用 现金付款函数和刷卡付款函数
    print('*'*30)
    print('1.现金付款')
    print('2.刷卡付款')
    print('3.退出菜单')
    zjL=int(input('根据提示选择相应的付款方式'))
    if(zjL==1):
        fuKuan()
    elif(zjL==2):
        shuCard()
    elif(zjL==3):
        system()
    print('*'*30)


zl=0 #手抓饼找零变量
zl1=0 #煎饼果子找零变量
def fuKuan():#定义现金付款函数
    for dic in lis:
        if dic['caiMing']==1:   #如果遍历到的字典是手抓饼的 则执行以下语句
            mony=int(input('手抓饼   20 元 请输入'))
            print('付款成功')
            if mony>20: #判断如果输入的钱大于菜的单价即找零
                global zl
                zl=mony-20
        else:#(dir['caiMing']=='gbr'):
            mony=int(input('煎饼果子 30 元 请输入'))
            print('付款成功')
            if mony>30:
                global zl1
                zl1=mony-30
    zlz=zl+zl1
    print('找零 %d 元' %zlz)


money=0
money1=0
money2=0
def shuCard():#定义刷卡函数
    global money
    if money<=0:#判断账户中的钱是否有余额
        money=int(input('充值款'))#输入充值金额
    name=input('输入会员帐号')
    pas=int(input('输入会员密码'))
    for dic1 in lis1:#在存储密码 和 账户的列表中遍历字典
        if (dic1['name']==name) and (dic1['pas']==pas):#如果字典中name键值和pas键值对应的值等于输入的内容
            for dic in lis:#在菜单列表中遍历字典
                if(dic['caiMing']==1):#判断所选择的菜为1.西红柿鸡蛋
                    if(money<20):#因为菜价金额为20,不足的话会跳到主界面，可进行充值
                        print('您余额不足请充值，系统将自动为您退出到主界面')
                        break
                    print('手抓饼   20 元 刷卡成功 已5折优惠')
                    money=money-20*0.5#进行余额计算
                else:
                    if  money<30:
                        print('您余额不足请充值，系统将自动为您退出到主界面')
                        break
                    print('煎饼果子 30 元 刷卡成功 已5折优惠')
                    money=money-30*0.5
            print('卡内余额 %d 元' %money)
        else:
            print('密码/帐号错误重新输入')


def huiY():#会员函数，调用办理会员卡函数和会员卡充值函数
    print('1.办理会员卡')
    print('2.会员卡充值')
    print('3.退出子菜单')
    coo=int(input('根据提示输入相应选项'))
    if coo==1:
        banKa()
    elif coo==2:
        cunKuan()
    else:
        system()


def banKa():#办理会员卡函数
    dic1={}
    print('办理会员卡业务')
    name=input('设置会员帐号')
    pas=int(input('设置会员密码'))
    dic1={'name':name,'pas':pas}#设置存放帐号 和 密码的字典
    lis1.append(dic1)#将字典追加到列表
    #print(lis1)
    print('办理会员卡成功')

def cunKuan():#会员卡充值函数
    print('*'*30)
    global money
    if money<=0 and len(lis1)!=0:#判断卡中是否有余额，没有余额 提示 并充值
        print('卡内余额不足')
        print('请充值')
        jeIn=int(input('请冲入金额'))
        money=money+jeIn
        print('卡内余额 %d' %money)
    elif money>0 and len(lis1)!=0:#如果有余额，就直接冲入相应的充值金额
        jeIn=int(input('请冲入金额'))
        money=money+jeIn
        print('卡内余额 %d' %money)

    print('*'*30)

while(True):#while的主函数
    system()
    print('*'*30)
    coo=int(input('根据提示输入相应功能编号'))
    if(coo==1):#调用点菜函数
        dianCai()
    elif(coo==2):#调用付款函数
        fuKuanZ()
    elif(coo==3):#调用会员服务函数
        huiY()
    elif(coo==0):#退出系统函数
        print('-^ ^-'*7)
        print('已退出系统,欢迎下次光临')
        print('-^ ^-'*7)
        break
    print('*'*30)







