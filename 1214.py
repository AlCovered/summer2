n,k = map(int,input().split(" "))
res = 1
flag = False
while n>0:
    if(10**18/n<res):
        flag = True
        break
    res*=n
    n -= k
if flag:
    print("overflow")
else:
    print(res)
