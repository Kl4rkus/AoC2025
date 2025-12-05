from pathlib import Path
import time

data_path = Path(__file__).resolve().parent / 'data' / 'day5.txt'
start_time = time.time()
with data_path.open() as f:
    ranges, products = f.read().split("\n\n")
    ranges=ranges.split("\n")
    products=products.split("\n")
    
    for i in range(len(ranges)):
        ranges[i]=ranges[i].split("-")
    for i in range(len(products)):
        products[i] = int(products[i])

#part 1
fresh_product_amount = 0
for p in products:
    fresh = False
    for a in ranges:
        if int(a[0]) <= p <= int(a[1]):
            fresh = True
    if fresh:
        fresh_product_amount+=1
print("part one answer:", fresh_product_amount)

#part 2
#Start with making all the ranges numbers:
for i in range(len(ranges)):
    ranges[i][0], ranges[i][1] = int(ranges[i][0]), int(ranges[i][1])
#the idea here is to recursively "absorb" all range that come in contact with r from rs, and if there's none, add r to rs
rs=[ranges[0]]
def merge_ranges(r):
    #print(rs,r)
    for i in range(len(rs)):
        #Check if range is included in new range:
        if r[0]< rs[i][0] < rs[i][1] < r[1]:
            #print("includes")
            rs.pop(i)
            merge_ranges(r)
            return
        #Check if r extends a range from upper values
        if rs[i][0] <= r[0] <= rs[i][1] and r[1] > rs[i][1]:
            #print("top extention")
            new_r = [rs[i][0], r[1]]
            rs.pop(i)
            merge_ranges(new_r)
            return
        #Check if r extends a range from lower values
        if  r[0] < rs[i][0] and rs[i][0] <= r[1] <= rs[i][1]:
            #print("bottom extension")
            new_r = [r[0], rs[i][1]]
            rs.pop(i)
            merge_ranges(new_r)
            return
        #Check if r is in another range
        if rs[i][0]<=r[0]<=r[1]<=rs[i][1]:
            #print("included")
            return
    #print("add range")
    rs.append(r)

#print("merge start")
for r in ranges[1:]:
    #print(rs, r)
    merge_ranges(r)
#print("merge end:", rs)
products_amount = 0
for r in rs:
    products_amount+=r[1]-r[0]+1

print("part 2 answer:", products_amount)
print(f"Time: {time.time() - start_time:.2f}s")