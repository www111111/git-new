


tu1=(1,2,3,)
for i in tu1:
    print(i)

a=0
while(a<=2):
    b=tu1[a]
    print(b)
    a+=1

tu1=((1,2,3),(4,5,6),(7,8,9))
for i in tu1:
    for a in i:
        print(a)

print('*'*30)
for g in range(0,3):
   h=tu1[g]
   for j in h:
       print(j)







a=0
b=0
c=0
e=0
while(a<=2):
    c=0
    b=tu1[a]
    while(c<=2):
        d=b[c]
        print(d)
        c+=1
    a+=1














liebiao = [{'name':'xiaobu','age':11,'sex':'nan'},{'name':'jin','age':31,'sex':'nv'}]
for i in liebiao:
    print('name : %s'% i['name'])
    print('age : %s'% i['age'])
    print('sex : %s'% i['sex'])

z=0
while(z<=1):
    x=liebiao[z]
    print('name : %s'% x['name'])
    print('age : %s'% x['age'])
    print('sex : %s'% x['sex'])
    z+=1


