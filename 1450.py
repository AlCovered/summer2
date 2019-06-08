def bishop(i,j,n):
    result = 0
    i-=1
    j-=1
    n-=1
    if(min(i,j)>0):
        result+=min(i,j)
    if(min(j,n-i)>0):
        result+=min(j,n-i)
    if(min(n-j,n-i)>0):
        result+=min(n-j,n-i)
    if(min(n-j,i)>0):
        result+=min(n-j,i)
    return result
def knight(i,j,n):
    result = 0
    if(i-1>0 and j-2>0):
        result+=1
    if(i-2>0 and j-1>0):
        result+=1
    if(j+1<=n and i-2>0):
        result+=1
    if(i-1>0 and j+2<=n):
        result+=1
    if(i+1<=n and j+2<=n):
        result+=1
    if(i+2<=n and j+1<=n):
        result+=1
    if(i+1<=n and j-2>0):
        result+=1
    if(i+2<=n and j-1>0):
        result+=1
    return result

n = int(input())
i = int(input())
j = int(input())
print(bishop(i,j,n)+knight(i,j,n))
