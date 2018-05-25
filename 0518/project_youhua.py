import project_tool
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


def dianCai():#买家服务函数
    dic={}#定义一个空字典
    print('1.查看销售菜品')
    print('2.选择菜品')
    print('3.查看已点菜单')
    print('4.删除所选菜品')
    print('5.返回上级菜单')
    print('*'*30)
    while(True):
        zjL=int(input('根据提示选择点菜子菜单'))
        if(zjL==1):#如果中间变量=1，显示如下菜单
            project_tool.display_xiaos()
            print('*'*30)
        elif(zjL==2):#如果中间变量=2,选择菜品菜单
            project_tool.xuanzeC()
            print('*'*30)
        elif(zjL==3):
            project_tool.displayAll()#功能 显示所点菜品
            print('*'*30)
        elif(zjL==4):
            project_tool.delete()#功能 删除所点菜品
            print('*'*30)
        elif(zjL==5):
            print('返回上级菜单')
            break


def fuKuanZ():#付款函数 调用 现金付款函数和刷卡付款函数
    print('1.现金付款')
    print('2.刷卡付款')
    print('3.退出菜单')
    zjL=int(input('根据提示选择相应的付款方式'))
    if(zjL==1):
        project_tool.fuKuan()
        print('*'*30)
    elif(zjL==2):
        project_tool.shuCard()
        print('*'*30)
    elif(zjL==3):
        system()



def huiY():#会员函数，调用办理会员卡函数和会员卡充值函数
    print('*'*30)
    print('1.办理会员卡')
    print('2.会员卡充值')
    print('3.退出子菜单')
    coo=int(input('根据提示输入相应选项'))
    if coo==1:
        print('*'*30)
        project_tool.banKa()
        huiY()
    elif coo==2:
        print('*'*30)
        project_tool.cunKuan()
        huiY()
    else:
        print('返回主菜单')




while(True):# 主函数
    system()
    coo=int(input('根据提示输入相应功能编号'))
    if(coo==1):#调用买家函数
        dianCai()
    elif(coo==2):#调用付款函数
        fuKuanZ()
    elif(coo==3):#调用会员服务函数
        huiY()
    elif(coo==4):#卖家添加菜服务
        project_tool.cai()
    elif(coo==0):#退出系统函数
        print('-^ ^-'*7)
        print('已退出系统,欢迎下次光临')
        print('-^ ^-'*7)
        break







