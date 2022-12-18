#Day 2
    
nums=list(map(int,input().split()))
new=[]
for i in nums:
    product=1
    for j in nums:
        if(i!=j):
            product=product*j
    new.append(product)
print(new)

