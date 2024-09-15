n = int(input()) #declaring variable for numbers input
temp = [] #list to store the values
val= input().split() #spliting the input values

for i in range(n):
    temp.append(int(val[i])) #insert in the list 
    



t=tuple(temp) #converting the list to tuple
print(hash(t)) #Hashing the tuple
