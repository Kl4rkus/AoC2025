from pathlib import Path

def find_joltage(battery, joltage_length):

    current_joltage=""
    prev_maxindex=0
    for i in range(joltage_length):
        maxnum, maxnum_index = 0, 0
        for j in range(prev_maxindex, len(battery)-joltage_length+1+i):
            if int(battery[j])>maxnum:
                maxnum, maxnum_index = int(battery[j]), j
        prev_maxindex=maxnum_index+1
        current_joltage+=str(maxnum)
    return current_joltage

    
print(find_joltage("811111111111119",12))

data_path = Path(__file__).resolve().parent / 'data' / 'day3.txt'

with data_path.open() as f:
    sum_joltages=0
    for data in f.read().split("\n"):
        sum_joltages+=int(find_joltage(data,12))
print(sum_joltages)