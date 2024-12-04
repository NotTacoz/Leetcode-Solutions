import os

__location__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))

txt = []

with open(os.path.join(__location__, "4simple.txt"), "r") as f:
    for l in f:
        l = l.strip()
        # print(l)
        txt.append(list(l))
        
print(txt)

def horizontal(p):
    count = 0
    for line in p:
        # left to right
        for i in range(len(line)-3):
            wordlist = [line[i], line[i+1],line[i+2],line[i+3]]
            if ("").join(wordlist) == "XMAS":
                count+=1
        # right to left
        line.reverse()
        for i in range(len(line)-3):
            wordlist = [line[i], line[i+1],line[i+2],line[i+3]]
            if ("").join(wordlist) == "XMAS":
                count+=1
    return count

print(horizontal(txt))