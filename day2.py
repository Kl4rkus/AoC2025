from pathlib import Path
### Part 1
def is_real_id(id):
    id=str(id) 
    if len(id)%2!=0:
        return True
    lengde = len(id)//2
    if id[:lengde] == id[lengde:] :
        return False
    else:
        return True
    


### Part 2
def is_real_id(id):
    id=str(id)
    
    for i in range(1,len(id)//2+1):
        a=False
        if len(id)%i==0:
            repetitions = len(id)//i # i = 2, repetitions = 5
            for j in range(repetitions - 1): # j = 0, 1, 2, 3
                if not id[j*i:(j+1)*i] == id[(j+1)*i:(j+2)*i]:
                    a = True
            if not a: 
                print(id)
                return(False)
                


def get_sum_false_id_in_range(n1, n2):
    sum_false_id = 0
    for n in range(n1,n2+1):
        if is_real_id(n) == False:
            sum_false_id += n
    return sum_false_id

data_path = Path(__file__).resolve().parent / 'data' / 'day2.txt'

with data_path.open() as f:
    sum_false_ids=0
    for data in f.read().split(","):
        n1, n2 =data.split("-")
        
        sum_false_ids+=get_sum_false_id_in_range(int(n1),int(n2))
    print(sum_false_ids)