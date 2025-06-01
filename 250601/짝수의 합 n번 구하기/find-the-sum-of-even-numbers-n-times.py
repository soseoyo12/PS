n=int(input())

count=0

for i in range(n):
    a,b=map(int,input().split())
    if a % 2 == 0 and b % 2 ==0:
        for ii in range(a,b+1,2):
            count += ii
        print(count)
        count=0
    elif a % 2 == 0 and b % 2 !=0:
        for iii in range(a,b,2):
            count += iii
        print(count)
        count=0
    elif a % 2 != 0 and b % 2 == 0:
        for iv in range(a+1,b+1,2):
            count += iv
        print(count)
        count=0
    else:
        for V in range(a+1,b,2):
            count += V
        print(count)
        count =0
    