from pathlib import Path
import time
data_path = Path(__file__).resolve().parent / 'data' / 'day7.txt'
start_time = time.time()
with data_path.open() as f:
    data = f.read().split("\n")
    for i in range(len(data)):
        data[i]=list(data[i])



#Part 1 
# To solve part 1, we will draw all the tachions, and count all splits.
# To do so, we will look at two rows at the same, and propagate information down.
total_splits=0
for i in range(len(data)-1):
    for j in range(len(data[0])):
        if data[i][j]=="S" or data[i][j]=="|":
            if data[i+1][j]== "^": #Potential issue: two ^ are next to each other. Assumed this is impossible.
                data[i+1][j+1] = "|"
                data[i+1][j-1] = "|"
                total_splits+=1
            else:
                data[i+1][j]="|"
print("part 1 result:", total_splits)


#Part 2
#for this one, we will count how many paths lead to each location. Add the end,summing those paths up will lead to the answer
#start by reloading and formating the data in a nicer manner.
with data_path.open() as f:
    data = f.read().split("\n")
    for i in range(len(data)):
        data[i]=list(data[i])
        for j in range(len(data[0])):
            if data[i][j]==".":
                data[i][j]=0

#same logic as in 1, except instead of drawing the tachions, we add them.
for i in range(len(data)-1):
    for j in range(len(data[0])):
        if data[i][j]=="S":
            data[i+1][j]=1
        elif data[i][j]=="^":
            data[i+1][j]=0
        else:
            if data[i+1][j]== "^": 
                data[i+1][j+1] += data[i][j]
                data[i+1][j-1] += data[i][j]
            else:
                data[i+1][j]+=data[i][j]
result=0
for i in data[-1]:
    result+=i
print("part 2 result:", result)    