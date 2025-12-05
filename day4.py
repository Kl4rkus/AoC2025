from pathlib import Path

data_path = Path(__file__).resolve().parent / 'data' / 'day4.txt'

with data_path.open() as f:
    data = f.read().split("\n")
    for i in range(len(data)):
        data[i]=list(data[i])

def check_if_roll(x,y):
    if x<0 or x>len(data)-1 or y<0 or y>len(data[0])-1:
        return 0
    if data[x][y]=="@" or data[x][y]=="x":
        return 1
    return 0

def check_total_availability(x,y):
    proximity_count = -1
    for i in range(x-1,x+2):
        for j in range(y-1, y+2):
            proximity_count+=check_if_roll(i,j)
    if proximity_count<4:
        data[x][y]="x"
        return 1
    return 0


available_rolls=0
removed_rolls = 1
infloop=0
while removed_rolls and  infloop<100:
    removed_rolls =0
    infloop+=1
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]=="@":
                available_rolls+=check_total_availability(i,j)
    # Remove rolls marked for removal
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]=="x":
                data[i][j]="."
                removed_rolls+=1
    print("rolls removed this itteration:", removed_rolls)
    print("loop:", infloop)
print("Total removed roll", available_rolls)