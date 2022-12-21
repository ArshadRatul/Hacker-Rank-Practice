#RunnerUpScore
n=int(input(""))
x=input("")
score=x.split(" ")

second=list(map(int, score))
second.sort(reverse=True)

print(second)
for i in range(len(second)):
    if(second[i]>second[i+1]):
        print(second[i+1])
        break
