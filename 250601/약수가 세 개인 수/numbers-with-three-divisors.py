start, end = map(int, input().split())
count=0
result_count=0

for i in range(start,end+1):
    for ii in range(1,i+1):
        if i % ii == 0:
            count += 1
    if count == 3:
        result_count += 1
    count = 0
        
        
print(result_count)