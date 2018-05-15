name='congc'
passwd=123
i=1
while(i<=4):
    user_in=input('请输入用户名')
    passwd_in=int(input('请输入密码'))
    if name==user_in and passwd==passwd_in:
        print('欢迎来到python')
        break

    else:
        if name!=user_in:
            print('用户名输入错误')
        if passwd!=passwd_in:
            print('密码输入错误')
    i=i+1



