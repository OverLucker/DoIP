def min(arr):
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    return min
    
def avg(arr):
    avg = 0
    for i in arr:
        avg = avg + i
    return avg / len(arr)
    
if __name__ == "__main__":
    arr = [1, 2, 4, 5]
    print(arr)
    print('Минимум ' + str(min(arr)))
    print('Среднее ' + str(avg(arr)))