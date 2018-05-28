

f=0
for i in range(1,5):
    for a in range (1,5):
        if a!=i:
            for c in range(1,5):
                if c!=i and c!=a:
                    print(i,a,c)

                    f+=1
print('一共有%d 个'%f)


list=[{'北京':{'面积':'1000平','人口':'200w'},'上海':{'面积':'600平','人口':'150w'}}]

for i in list:
    for a,b in i.items():
        for c,d in b.items():
            print(a,c,d)






