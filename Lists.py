n = int(input())
the_list = []

for i in range(n):
    value= input().split()
    
    if(value[0]=="insert"):
        the_list.insert(int(value[1]),int(value[2]))
    elif(value[0]=="print"):
        print(the_list)
    elif(value[0]=="remove"):
        the_list.remove(int(value[1]))
    elif(value[0]=="append"):
        the_list.append(int(value[1]))
    elif(value[0]=="sort"):
        the_list.sort()
    elif(value[0]=="pop"):
        the_list.pop()
    elif(value[0]=="reverse"):
        the_list.reverse()

print(the_list)