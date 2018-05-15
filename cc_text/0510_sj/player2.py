
import random
pc=random.randint(1,3)
print(pc)

if(user==1 and pc==2) or (user==2 and pc==3) or (user==3 and pc==1 ):
    print('win')
elif user==pc:
    print('ping')
else:
    print('lose')
