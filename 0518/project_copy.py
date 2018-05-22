lis=[]
def system():
    print('*'*30)
    print('欢迎使用无人餐厅管理系统',end='\n\t')
    print('1.输入您要点菜名')
    print('2.付款')
    print('3.刷卡')
    print('4.显示菜单菜')
    print('5.存钱')
    print('6.删除')
    print('0.退出系统')
    print('*'*30)
def dianCai():
    dic={}
    print('*'*30)
    print('菜单选项如下 ：')
    print('1.西红柿鸡蛋')
    print('2.锅包肉')
    while(True):
        caiMingI=int(input('请输入要点的菜名的编号 \t'))
        kouWeiI=input('请输入菜的口味 辣或者不辣 \t')
        dic={'caiMing':caiMingI,'kouWei':kouWeiI}
        lis.append(dic)
        print(lis)
        print('已点 %s \t 口味 %s\t ' % (dic['caiMing'],dic['kouWei']))
        print('*'*30)
        panD=input('是否选好菜 输入 Y/N')
        if (panD=='Y'):
            break


def delete():
     print('*'*30)
     dCi=int(input('输入菜名字 \t'))
     print('请删除 %s 菜名' % dCi)
     for dic in lis:
         print(dic)
         if dic['caiMing'] == dCi:
             print(dic)
             #lis.remove(dic)
             lis.remove(dic)
             print(lis)
     print('删除 %s 成功' % dCi)
     print('*'*30)

zl=0
zl1=0
def fuKuan():
    print('*'*30)
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
    print('*'*30)

def displayAll():
    print('*'*30)
    print('所点菜名如下 ： ')
    for a in lis:
        print('菜名 :%s '% a['caiMing'])
        print('口味 :%s '% a['kouWei'])
        print('已显示所有菜单')
    print('*'*30)

def zhaoCai():
    pass


money=0
money1=0
money2=0
def shuCard():
    print('*'*30)
    #print('第一次刷卡送20元')

    card_num=input('输入卡号')
    passwd=int(input('输入密码'))
    if money<=0:
        global money
        money=int(input('充值款'))
    if card_num=='www' and passwd==123:
        for dic in lis:
            if(dic['caiMing']==1):
                if(money<20):
                    print('您余额不足请充值，系统将自动为您退出到主界面')
                    break
                print('西红柿鸡蛋 20 元 刷卡成功')
               # lis.remove(dic)
                money=money-20
                #print('卡内余额 %d' %money)
                #lis.remove(dir)
            else:#(dir['caiMing']=='gbr'):
                if  money<30:
                    print('您余额不足请充值，系统将自动为您退出到主界面')
                    break
                print('锅包肉 30 元 请刷卡')
                money=money-30
                #print('卡内余额 %d' %money)
                #lis.rmove(dir)
    #global money1,money2
    #money=money1+money2
    print('卡内余额 %d' %money)
    print('*'*30)
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





system()
while(True):
    coo=int(input('根据提示输入相应编号'))
    if(coo==1):
        dianCai()
    if(coo==2):
        fuKuan()

    if(coo==3):
        shuCard()

    if(coo==4):
        displayAll()

    if(coo==6):
        delete()

    if(coo==5):
        cunKuan()

    if(coo==0):
        print('-^ ^-'*30)
        print('已退出系统')
        print('欢迎下次光临')
        print('-^ ^-'*30)
        break







