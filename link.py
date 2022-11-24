

# To convert matrix to dictionary with keys as row numbers 
# and values as list

n=int(input())
d={}
for x in range(1,n+1):
    s=list(map(int,input().split(",")))
    d[x]=s
print(d)






   


