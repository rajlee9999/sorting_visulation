import time

def partition(data, head, tail, drawdata, timeTick):
    border = head
    pivot = data[tail]

    drawdata(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawdata(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawdata(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)


    #swap pivot with border value
    drawdata(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]
    
    return border

def quick_sort(data, head, tail, drawdata, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawdata, timeTick)

        #LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawdata, timeTick)

        #RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawdata, timeTick)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray






