#FindingThePrecentage
n=int(input("")) #taking the number of inputs
a=[]
for i in range(n): #taking the input as string
    a.append(input(""))

query=input("") #taking the query 
ave=[]
for i in a: 
    val=i.split(" ") #spliting the string which has space in between.
    if(query==val[0]):
        ave= val[1:] #making a list of from the second element to end
        break

s=list(map(float, ave))#converting the list to float
average= sum(s)/len(s)
print ("{0:.2f}".format(average)) #printing it to 2decimal place
