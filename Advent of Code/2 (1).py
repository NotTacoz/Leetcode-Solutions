# im the goat im going to fix this

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

p1 = 0
p2 = 0
    
def isSafe(line):
    check = True
    
    line = list(map(int, line))

    
    if line != sorted(line, reverse=True) and line != sorted(line):
        check = False
        # print("order error")
        # print(sorted(line, reverse=True))
        # print(sorted(line))
        
    for x in range(1, len(line)):
        diff = abs(int(line[x-1])-int(line[x]))
        if diff < 1 or diff > 3:
            check = False
            # print("diff error")
    
    # print(check,line)
    if check == True:
        return True
    

with open(os.path.join(__location__, "2.txt"), "r") as f:
    for l in f:
        a = l.split()
        if (isSafe(a)):
            p1+=1 # part 1
            
        
        good = False    
        for y in range(len(a)):
            b = l.split()
            b.pop(y)
            # b.remove(a[y]) this doesnt work for some reason .. im not sure which cases and why? 
            # b = a[:y] + a[y+1:]
            
            if (isSafe(b)):
                good = True
        if good == True:
            p2+=1 # part 2
            
        
print(p1)
print(p2)