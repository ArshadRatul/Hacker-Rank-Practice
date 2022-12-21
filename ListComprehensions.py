#ListComprehension 
x = int(input(""))
y = int(input(""))
z = int(input(""))
n = int(input(""))
list1=[]


for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            list2=[i,j,k]
            list1.append(list2)


list3=[]
for i in list1:
    a=i[0]+i[1]+i[2]
    if a!=n:
        list3.append(i)

print(list3)