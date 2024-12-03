import os 

# turn the file into a hashmap
# number: index

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

seen1 = []
seen2 = []


with open(os.path.join(__location__, "1.txt"), "r") as f:
    for line in f:
        # print(line.split())
        seen1.append(line.split()[0])
        seen2.append(line.split()[1])
       
# sort hash map by size 
        
seen1 = sorted(seen1)
seen2 = sorted(seen2)
        
        
# iterate through each line of hashmap
# add the "distance" to distance variable

distance = 0

j = 0 # count var

for x in seen1:
    distance = distance+(abs(int(x)-int(seen2[j])))
    j=+1
    
print(distance)