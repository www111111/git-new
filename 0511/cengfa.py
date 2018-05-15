
row=1
while(row<10):
    col=1
    while(col<=row):
        print('%d*%d=%d'%(col,row,row*col),end='\t')
        col=col+1
    row=row+1
    print('\n')


