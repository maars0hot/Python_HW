ls1=[1,2,3,5,8,15,23,38]

res=map(int,ls1)
print(res)
res=filter(lambda x: x % 2 ==0,res)
print(res)
res=list(map(lambda x:(x,x*x),res))
print(res)

