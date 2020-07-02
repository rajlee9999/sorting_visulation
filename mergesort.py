import time

def merge_sort(data, drawdata, timeTick):
    merge_sort_alg(data,0, len(data)-1, drawdata, timeTick)


def merge_sort_alg(data, left, right, drawdata, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawdata, timeTick)
        merge_sort_alg(data, middle+1, right, drawdata, timeTick)
        merge(data, left, middle, right, drawdata, timeTick)

def merge(data, left, middle, right, drawdata, timeTick):
    drawdata(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    l_Part = data[left:middle+1]
    r_Part = data[middle+1: right+1]

    l_Idx = r_Idx = 0

    for dataIdx in range(left, right+1):
        if l_Idx < len(l_Part) and r_Idx < len(r_Part):
            if l_Part[l_Idx] <= r_Part[r_Idx]:
                data[dataIdx] = l_Part[l_Idx]
                l_Idx += 1
            else:
                data[dataIdx] = r_Part[r_Idx]
                r_Idx += 1
        
        elif l_Idx < len(l_Part):
            data[dataIdx] = l_Part[l_Idx]
            l_Idx += 1
        else:
            data[dataIdx] = r_Part[r_Idx]
            r_Idx += 1
    
    drawdata(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)

def getColorArray(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")

    return colorArray
