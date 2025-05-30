N=int(input())

for i in range(1,N+1):
    for ii in range(1,N+1):
        if ii == N:
            print(f"{i} * {ii} = {i*ii}")
            break
        print(f"{i} * {ii} = {i*ii}", end=", ")


