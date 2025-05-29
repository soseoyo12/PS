A, B = map(int, input().split())

print(A,end=" ")
while True:
    if A % 2 == 0:
        A+=3
    else:
        A*=2
    if A <=B:
        print(A, end=" ")
    else:
        break