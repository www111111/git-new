zwq=int(input())
if zwq%4==0 and zwq%100!=0:
    print("润年")
elif zwq%400==0:
    print("润年")
else:
    print("平年")
