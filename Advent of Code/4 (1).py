import os

__location__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))

chars = []
width = 0
height = 0

with open(os.path.join(__location__, "4.txt"), "r") as f:
    for l in f:
        l = l.strip()
        # print(l)
        li = list(l)
        width = len(li)
        # print(li)
        for c in list(li):
            # print(c)
            chars.append(c)
            
        height+=1
        
count = 0

horizontalCount = 0
diagonalCount = 0

for x in range(len(chars)):
    n = x+1 # for easier mental stuff LOL
    
    # horizontal count
    if x < len(chars)-3 and ((n)/width).is_integer() == False and ((n+1)/width).is_integer() == False and ((n+2)/width).is_integer() == False:
        wordhorizontal = chars[x] + chars[x+1] + chars[x+2] + chars[x+3]
        # print(wordhorizontal)
        if (wordhorizontal) == "XMAS" or wordhorizontal == "SAMX":
            horizontalCount+=1
    
# diagonal count
nHeight = height - 3
nWidth = width - 3
firstNumbersList = []
allNumbersList = []
for i in range(nWidth):
    firstNumbersList.append(i)
    
firstcolumnboxonright = []
for i in range(nWidth):
    firstcolumnboxonright.append(3+i)

for yoo in range(len(firstNumbersList)):
    for foo in range(nWidth):
        allNumbersList.append(yoo + foo*width)
        
newnumberallnumberlist = []
for doodoo in (firstcolumnboxonright):
    for foo in range(nWidth):
        newnumberallnumberlist.append(doodoo + foo*width)

# print(newnumberallnumberlist)
# allNumbersList.sort()
# print(allNumbersList)

for fuckthis in allNumbersList:
    worddiagonal = chars[fuckthis] + chars[fuckthis+width+1] + chars[fuckthis+2*(width+1)] + chars[fuckthis+3*(width+1)]
    # print(worddiagonal)
    if (worddiagonal == "XMAS" or worddiagonal == "SAMX"):
        diagonalCount+=1

for fuckshit in newnumberallnumberlist:
    worddiagonal2 = chars[fuckshit] + chars[fuckshit+width-1] + chars[fuckshit+2*(width-1)] + chars[fuckshit+3*(width-1)]
    # print(worddiagonal)
    if (worddiagonal2 == "XMAS" or worddiagonal2 == "SAMX"):
        diagonalCount+=1
        
        
verticalCount = 0

for widthTemp in range(width): #0-9
    for heightTemp in range(height-3): #0-7
        # print("stating char",chars[widthTemp + width* (heightTemp)])
        wordvertically = chars[widthTemp + width*(heightTemp)] + chars[widthTemp + width*(heightTemp+1)] + chars[widthTemp + width*(heightTemp+2)] + chars[widthTemp + width*(heightTemp+3)]
        if wordvertically == "XMAS" or wordvertically == "SAMX":
            verticalCount+=1

print(diagonalCount, horizontalCount, verticalCount, (diagonalCount+horizontalCount+verticalCount))
# print(height, width)