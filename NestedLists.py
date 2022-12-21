#nested List
n=int(input(""))
record=[] #list to keep records

for i in range(n): #Input in the nested list
    name=input("")
    marks=float(input(""))
    details=[name,marks]
    record.append(details)

def marks(m): #Function to return the second element of the list
    return m[1]

record.sort(key=marks)#sort function sending the elements of the list to sort according to marks
heighest=record[0][1] 
for i in range(len(record)): #Just keeping the second lowest number
    if(record[i][1]>heighest):
        heighest=record[i][1]
        break

names=[]

for i in range(len(record)): #Making the list who have the second lowest number
    if(record[i][1]==heighest):
        names.append(record[i][0])

names.sort() #sorting the names alphabetically 

for i in range(len(names)): #printing the names
    print(names[i])