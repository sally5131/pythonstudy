x,y,w,h=map(int,input().split())
# (x,y) : 한수의 위치, (w,h) : 오른쪽 위 꼭짓점 위치

if(x<=(w//2) and y<=(h//2)):
    if(x>=y):
        print(y)
    else:
        print(x)
elif (x<=(w//2) and y>(h//2)):
    print(x)
elif (x>(w//2) and y<=(h//2)):
    print(y)
elif (x>(w//2) and y>(h//2)):
    if (x >= y):
        print(y)
    else:
        print(x)
