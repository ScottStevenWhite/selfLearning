

def mergeSort(data):
    if len(data) <= 1:
        return data
    midpt = int(len(data)/2)
    left = mergeSort(data[0:midpt])
    right = mergeSort(data[midpt:len(data)])
    data = []
    l = r = 0
    while l < len(left) and r < len(right):
        print(str(l) + " " + str(len(left)))
        print(str(r) + " " + str(len(right)))
        if left[l] > right[r]:
            data.append(right[r])
            r += 1
        else:
            data.append(left[l])
            l += 1
            
    while l < len(left):
        data.append(left[l])
        l += 1
    while r < len(right):
        data.append(right[r])
        r += 1
    return data

stuff = [5, 6, 2, 1, 7, 3, 9, 2, 6, 23]

newstuff = mergeSort(stuff)
print(newstuff)



