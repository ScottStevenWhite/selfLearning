import random
def makeRandom(n):
    randy = []
    for i in range(0, n):
        randy.append(random.randint(0, 100))
    return randy

listToSort = makeRandom(100000)
print("Orginal List: ", end = ' ')
print(listToSort)

sortedList = []
for j in range(len(listToSort)) :
    minNum = listToSort[0]
    smallestIndex = 0
    for i in range(1, len(listToSort)):
        if minNum > listToSort[i]:
            minNum = listToSort[i]
            smallestIndex = i
    sortedList.append(minNum)
    del listToSort[smallestIndex]



print("Sorted: " + str(sortedList))

