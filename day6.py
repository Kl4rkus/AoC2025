from pathlib import Path
import time
data_path = Path(__file__).resolve().parent / 'data' / 'day6.txt'
start_time = time.time()
with data_path.open() as f:
    data = f.read().split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(" ")
        while "" in data[i]:
            data[i].remove("")
#Now that the data has been formatted correclty, let's start for real!


total=0 #Keeps track of the sum of all problems
for i in range(len(data[0])):
    p=int(data[0][i]) #Keeps track of the current problem
    for j in range(1,len(data)-1):
        if data[-1][i]=="*":
            p*=int(data[j][i])
        else:
            p+=int(data[j][i])
    total+=p
print("part 1 result:", total)

# Part 2
with data_path.open() as f:
    data = f.read().split("\n")

total=0

current_numbers=[]  #keeps track of every number in each problem
operation=""   #keeps track of the operation to make (+ or *)
for i in range(len(data[0])): #itterates through every column
    if data[-1][i]!=" ":
        operation = data[-1][i]
    #print(i)
    is_done = True
    current_number=""    #keeps track of the number in each column
    for j in range(len(data)-1): #itterates through every digit in each column
        if data[j][i]!=" ":
            is_done=False
            current_number+=data[j][i]
    if is_done:     # if the current column is empty, and thus the problem is done, calculate stuff and add it to the total, before resetting the current_numbers.
        p=current_numbers[0]
        if operation=="+":
            for n in current_numbers[1:]:
                p+=n
        if operation=="*":
            for n in current_numbers[1:]:
                p*=n
        total+=p
        current_numbers=[]

    else:  #if the column isn't empty, add the current_number to the current_numbers list, then reset it
        current_numbers.append(int(current_number))
        current_number=""

p=current_numbers[0]
if operation=="+":
    for n in current_numbers[1:]:
        p+=n
if operation=="*":
    for n in current_numbers[1:]:
        p*=n
total+=p
print("part 2 result:",total)


    
    



