import time

def Bsort(data, drawdata, timeTick):
    n=len(data)
    for i in range(n):
        for j in range(n-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawdata(data, ['green' if x == j or x == j+1 else 'red' for x in range(n)] )
                time.sleep(timeTick)
    drawdata(data, ['green' for x in range(len(data))])




    


