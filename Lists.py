n=int(input(""))
TheList=[]
for i in range(n):
    inp=input("")
    val=inp.split(" ")
    if(val[0]=='insert'):
        TheList.insert(val[1],val[2])
        print(TheList)
        
    elif(val[0]=='print'):
        print(TheList)

    elif(val[0]=='remove'):
        for j in range(len(TheList)):
            TheList.remove(val[1])
        print(TheList)
    
    elif(val[0]=='append'):
        TheList.append(val[1])
        print(TheList)

    elif(val[0]=='sort'):
        TheList.sort()
        print(TheList)
    
    elif(val[0]=='pop'):
        TheList.pop()
        print(TheList)
    
    elif(val[0]=='reverse'):
        TheList.reverse()
        print(TheList)