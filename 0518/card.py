import tool
lis=[]
'''
def systemMnue():
    print('欢迎使用【名片管理系统】V1.0')
    print('*'*30)
    print('1. 新建名片')
    print('2. 显示全部')
    print('3. 查询名片')
    print('0. 退出系统')
    print('*'*30)
'''

def newCard():
    dir={}
    print('*'*30)
    print('请新建名片 \t')
    name=input('请输入名字 \t')
    age=int(input('请输入年龄 \t'))
    email=input('请输入邮箱 \t')
    dir={'name':name,'age':age,'email':email}
    #dir['name']=name
    #dir['age']=age
    #dir['email']=email
    lis.append(dir)
    #print(lis)
    print('已创建 %s 名片'%(dir['name']))
    print('*'*30)

def displayAll():
    print('*'*30)
    print('所有名片显示内容如下 ： ')
    for a in lis:
        print('姓名 :%s '% a['name'])
        print('年龄 :%d '% a['age'])
        print('邮箱 :%s '% a['email'])
    print('已显示所有名片')
    print('*'*30)

def searchCard():
    print('*'*30)
    nameShuR=input('输入查询的名字 \t')
    print('正在查询 %s 的名字 '%nameShuR)
    for dir in lis:
        if dir['name']== nameShuR:
           print('姓名：%s' % dir['name'])
           print('年龄：%s' % dir['age'])
           print('邮箱：%s' % dir['email'])
    print('已查询到名片')
    print('*'*30)

def exitSys():
    print('已退出系统,欢迎下次使用')

def delete():
    print('*'*30)
    a=input('输入删除的名片名字 \t')
    print('请删除 %s 名片' % a)
    for dir in lis:
        print(dir)
        if dir['name']== a:
            lis.remove(dir)
            print(lis)
    print('删除 %s 成功' % a)
    print('*'*30)

def xiuGai(f):
    print('*'*30)
    print('请修改 %s 的名片' % f)
    #print(f)
    for dir in lis:
        if dir['name']== f:
            dir['name']=input('输入修改后名字')
            dir['age']=int(input('输入修改后age'))
            dir['email']=input('输入修改后email')
    print('已修改 %s 的名片' % f)
    print('*'*30)
#systemMnue()
tool.systemMnue()
while(True):
    sr=int(input('请根据提示输入相应的编号 \t'))
    if sr == 1:
        newCard()
    elif sr == 2:
        displayAll()
    elif sr ==3:
        searchCard()
    elif sr ==4:
        delete()

    elif sr ==5:
        f=input('输入')
        xiuGai(f)
        #f=input('输入')
    else:
        jub=input('确定退出系统？ Y/N \t')
        if(jub =='Y'):
            exitSys()
            break

