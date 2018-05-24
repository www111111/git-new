import random
lis=[]#存放所点菜品的列表
lis1=[]#办卡用存储账户和密码所用列表
lis_addcai=[]#卖家添加菜单
def system():#人性化显示主菜单
    print('*'*30)
    print('欢迎使用街边早餐管理系统 --- 1388888888')
    print('店内优惠活动：现在办理会员卡可享受全店商品5折优惠！',end='\n\t')
    print('1.买家服务',end='\n\t')#查看销售菜品 选择菜品 查看已点菜单 删除所选菜品 返回上级菜单
    print('2.付款结帐',end='\n\t')      #现金付款 会员卡付款  返回上级菜单
    print('3.会员服务',end='\n\t')      #办卡  会员卡充值  返回上级菜单
    print('4.卖家服务',end='\n\t')      #添加菜品
    print('0.退出系统')
    print('*'*30)


def cai():#卖家添菜函数
    i=1
    maiJia=int(input('输入卖家密码'))#防止买家篡改密码设置固定密码
    n=int(input('输入添加菜的个数'))#循环次数  卖家根据添加菜数设置循环次数,在循环中可以循环输入菜名
    if maiJia==123:
        while(i<=n):
            caiMingI=input('卖家请添加菜名 \t')
            priceI=int(input('卖家请添加价钱 \t'))
            dic_addcai={'caiMing':caiMingI,'price':priceI}#将输入的value 菜名以及价格 存到字典
            lis_addcai.append(dic_addcai)#将字典存到列表
            i+=1
    else:
        print('密码输入错误')
def dianCai():#买家服务函数
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
            display_xiaos()



        elif(zjL==2):#如果中间变量=2,选择菜品菜单
            while(True):#循环选择
                print('*'*30)
                display_xiaos()
                dianCai=input('菜名')
                for dic_addcai in lis_addcai:
                    if dic_addcai['caiMing']==dianCai:
                        print('已点菜：%s' % dic_addcai['caiMing'] )
                        lis.append(dic_addcai)
                        panD=input('是否选好菜 输入 Y/N\t')#判断是否选好菜，选好即可跳出循环，未选择好继续循环
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

def display_xiaos():#显示销售的产品
    print('所点菜名如下 ： ')
    for a in lis_addcai:    #遍历列表查找相应的菜单
        print('菜名 :%s '% a['caiMing'])#显示菜名
        print('价格 :%d '% a['price'])
        print('已显示所有菜单')




def displayAll():#显示已点菜品函数
    print('*'*30)
    print('所点菜名如下 ： ')
    for a in lis:    #遍历列表查找相应的菜单
        print('菜名 :%s '% a['caiMing']) #输出菜名
        print('已显示所有菜单')
    print('*'*30)

def delete():#删除已点菜品函数
     print('*'*30)
     dCi=input('输入菜名字 \t')
     print('请删除 %s 菜名' % dCi)
     for dic in lis:#在列表中循环遍历查找dic（所查键值为输入的键值  根据键值查找对应的字典）
         #print(lis)
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

#mony=0
def fuKuan():#定义现金付款函数
    for dic in lis:

        print('菜名 ： %s 价格 ： %d '%(dic['caiMing'],dic['price']))
        mony=int(input('price'))
        if mony>dic['price']: #判断如果输入的钱大于菜的单价即找零
        #    global mony #引用全局变量
            zl=mony-dic['price'] #计算找零 给的价钱-商品价格
            print('找零 %d 元' %zl)
        elif mony<dic['price']:
            print('输入金额不足')

        else:#(dir['caiMing']=='gbr'):
            print('付款成功')

money=0
#money1=0
#money2=0
def shuCard():#定义刷卡函数
    #global money
    #if money<=0:#判断账户中的钱是否有余额
     #   money=int(input('充值款'))#输入充值金额
    name=input('输入会员帐号')
    pas=int(input('输入会员密码'))
  #  print(lis1)
    for dic1 in lis1:#在存储密码 和 账户的列表中遍历字典
        if (dic1['name']==name) and (dic1['pas']==pas):#如果字典中name键值和pas键值对应的值等于输入的内容
         #   print(dic1)
            for dic in lis:#在菜单列表中遍历字典
                if(money<dic['price']):#如果付款金额小于菜价,不足的话会跳到主界面，可进行充值
                    print('您余额不足请充值，系统将自动为您退出到主界面')
                    break
                print('菜名 ： %s 价格 ： %.2f'%(dic['caiMing'],dic['price']*0.5))
                print('付款成功')
                dic1['money']=dic1['money']-dic['price']*0.5
                print('卡内余额 %.2f元' %dic1['money'])
        #else:
         #   print('密码/帐号错误重新输入')


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
    dic1={'name':name,'pas':pas,'money':money}#设置存放帐号 和 密码的字典
    lis1.append(dic1)#将字典追加到列表
    #print(lis1)
    print('办理会员卡成功')

def cunKuan():#会员卡充值函数
    print('*'*30)
    global money
    name_chongZhi=input('输入充值的帐号')
    for dic1 in lis1:
        if(dic1['name']== name_chongZhi):
          #  print(dic1)
            if dic1['money']<=0 and len(lis1)!=0:#判断卡中是否有余额，没有余额 提示 并充值
                print('卡内余额不足')
                print('请充值')
                money=int(input('请冲入金额'))
           #     print(dic1)
                dic1['money']=dic1['money']+money
            #    print(dic1)
                print('卡内余额 %d' % dic1['money'])
            elif dic1['money']>0 and len(lis1)!=0:#如果有余额，就直接冲入相应的充值金额
                jeIn=int(input('请冲入金额'))
                dic1['money']=dic1['money']+jeIn
                print('卡内余额 %d' %dic1['money'])
                print(dic1)
            print('*'*30)

while(True):# 主函数
    system()
    print('*'*30)
    coo=int(input('根据提示输入相应功能编号'))
    if(coo==1):#调用买家函数
        dianCai()
    elif(coo==2):#调用付款函数
        fuKuanZ()
    elif(coo==3):#调用会员服务函数
        huiY()
    elif(coo==4):#卖家添加菜服务
        cai()
    elif(coo==0):#退出系统函数
        print('-^ ^-'*7)
        print('已退出系统,欢迎下次光临')
        print('-^ ^-'*7)
        break
    print('*'*30)







