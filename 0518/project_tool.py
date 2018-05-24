import random
lis=[]#存放所点菜品的列表
lis1=[]#办卡用存储账户和密码所用列表
lis_addcai=[]#卖家添加菜单


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



#mony=0
def fuKuan():#定义现金付款函数
    for dic in lis:

        print('菜名 ： %s 价格 ： %d '%(dic['caiMing'],dic['price']))
        mony=int(input('price'))
        if mony>dic['price']: #判断如果输入的钱大于菜的单价即找零
            zl=mony-dic['price'] #计算找零 给的价钱-商品价格
            print('找零 %d 元' %zl)
        elif mony<dic['price']:
            print('输入金额不足')
        else:#(dir['caiMing']=='gbr'):
            print('付款成功')

money=0
def shuCard():#定义刷卡函数
    name=input('输入会员帐号')
    pas=int(input('输入会员密码'))
    for dic1 in lis1:#在存储密码 和 账户的列表中遍历字典
        if (dic1['name']==name) and (dic1['pas']==pas):#如果字典中name键值和pas键值对应的值等于输入的内容
            for dic in lis:#在菜单列表中遍历字典
                if(money<dic['price']):#如果付款金额小于菜价,不足的话会跳到主界面，可进行充值
                    print('您余额不足请充值，系统将自动为您退出到主界面')
                    break
                print('菜名 ： %s 价格 ： %.2f'%(dic['caiMing'],dic['price']*0.5))
                print('付款成功')
                dic1['money']=dic1['money']-dic['price']*0.5
                print('卡内余额 %.2f元' %dic1['money'])

def banKa():#办理会员卡函数
    dic1={}
    print('办理会员卡业务')
    name=input('设置会员帐号')
    pas=int(input('设置会员密码'))
    dic1={'name':name,'pas':pas,'money':money}#设置存放帐号 和 密码的字典
    lis1.append(dic1)#将字典追加到列表
    print('办理会员卡成功')

def cunKuan():#会员卡充值函数
    print('*'*30)
    global money
    name_chongZhi=input('输入充值的帐号')
    for dic1 in lis1:
        if(dic1['name']== name_chongZhi):
            if dic1['money']<=0 and len(lis1)!=0:#判断卡中是否有余额，没有余额 提示 并充值
                print('卡内余额不足')
                print('请充值')
                money=int(input('请冲入金额'))
                dic1['money']=dic1['money']+money
                print('卡内余额 %d' % dic1['money'])
            elif dic1['money']>0 and len(lis1)!=0:#如果有余额，就直接冲入相应的充值金额
                jeIn=int(input('请冲入金额'))
                dic1['money']=dic1['money']+jeIn
                print('卡内余额 %d' %dic1['money'])
                print(dic1)
            print('*'*30)


def  xuanzeC():
    while(True):#循环选择
        print('*'*30)
        display_xiaos()
        dianCai=input('菜名')
        for dic_addcai in lis_addcai:
            if dic_addcai['caiMing']==dianCai:
                print('已点菜：%s' % dic_addcai['caiMing'] )
                lis.append(dic_addcai)
                panD=input('是否选好菜 输入 Y/N \t')#判断是否选好菜，选好即可跳出循环，未选择好继续循环
        if (panD=='Y'):
            break
            print('*'*30)









