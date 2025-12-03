from pathlib import Path

class Dial():
    def __init__(self):
        self.current_number=50
        self.zero_counter = 0
    def increment(self, code): #code is a string of the format "R34" or "L2"
        o=self.zero_counter
        if code[0]=="R":
            if self.current_number==100:
                self.zero_counter-=1
            self.zero_counter+=(self.current_number+int(code[1:]))//100
            self.current_number = (self.current_number+int(code[1:]))%100
        else:
            if self.current_number==0:
                self.zero_counter-=1
            self.current_number -= int(code[1:])
            while (self.current_number)//100 <0: 
                self.current_number += 100 
                self.zero_counter +=1
            if self.current_number==0:
                self.zero_counter +=1
'''        print("code:", code)
        print("zero_counter:", self.zero_counter)
        print("has incremented:", self.zero_counter>o)
        print("new_number:", self.current_number)
        print("\n")'''


dial = Dial()

data_path = Path(__file__).resolve().parent / 'data' / 'day1.txt'

with data_path.open() as f:
    for data in f.read().split("\n"):
        dial.increment(data)
print("current number:",dial.current_number)
print("zero counter:", dial.zero_counter)
print(0//100)