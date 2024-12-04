# parse data

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))

seen = []

safe = 0

check = True

cont = False

with open(os.path.join(__location__, "2.txt"),"r") as f:
    for line in f:
        cont = False
        # convert line to int
        line1 = list(map(int, line.split()))
        line2 = list(map(int, line.split()))
        line3 = list(map(int, line.split()))
        line2.sort()
        line3.sort(reverse = True)
        if line1 == line2 or line1 == line3:
            i = 0 # index
            check = True
            for x in line1:
                if i != 0: # for all values in line except first value
                    difference = abs(x - line1[i-1])
                    if difference == 0 or difference > 3:
                        check = False
                    # if differnece is 1,2,3
                i+=1
            if check == True:
                print(safe, line1, "order good, difference good")
                safe+=1
            else:
                cont = False
                for x in line1:
                    line1 = list(map(int, line.split()))
                    line1.remove(x)
                    # print(line1)
                    i = 0 # index
                    check = True
                    for y in line1:
                        if i != 0: # for all values in line except first value
                            difference = abs(y - line1[i-1])
                            if difference == 0 or difference > 3:
                                check = False
                            # elif x==21:
                            #     print(y,line1[i-1],"difference:", difference)
                            # if differnece is 1,2,3
                        i+=1
                    if check == True:
                        print("Works by removing ",x)
                        cont = True
                        break
                if cont == True:
                    line1 = list(map(int, line.split()))
                    print(safe, line1, "order good, difference bad, removed a number")
                    safe+=1
                else:
                    line1 = list(map(int, line.split()))
                    # print("NO WORKY!", line1)
                    
        else:
            i = 0
            cont = False
            for x in line1:
                line1 = list(map(int, line.split()))
                line2 = list(map(int, line.split()))
                line3 = list(map(int, line.split()))
                line2.sort()
                line3.sort(reverse = True)
                cont = False
                line1.remove(x)
                line2.remove(x)
                line3.remove(x)
                if line1 == line2 or line1 == line3:
                    i = 0 # index
                    check = True
                    for y in line1:
                        if i != 0: # for all values in line except first value
                            difference = abs(y - line1[i-1])
                            if difference == 0 or difference > 3:
                                check = False
                            # if differnece is 1,2,3
                        i+=1
                    if check == True:
                        print("Works by removing ",x)
                        cont = True
                        break
            if cont == True:
                line1 = list(map(int, line.split()))
                print(safe, line1, "order bad, removed a number")
                safe+=1
            else:
                line1 = list(map(int, line.split()))
                # print("NO WORKY!", line1)
                
            
print(safe)
    
        




# check if the sorted version = unsorted
# if true, +1 to safe

#trash ahh code