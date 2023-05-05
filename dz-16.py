def masgen(n):
 
    for i in range(1,10):
        mlist.append(i)
 
 
 
    print(mlist)
    print(mlist.count(n))
 
if __name__ == '__main__':
 
    mlist=[]
    n=int(input())
    masgen(n)