def hnt(n,a,b,c):
    if n==1:
        print(a,"-",c)
    else:
        hnt(n-1,a,c,b)
        hnt(1,a,b,c)
        hnt(n-1,b,a,c)
print(hnt(5,"A","B","C"))
