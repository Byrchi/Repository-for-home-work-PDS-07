print('Hello world!')


import time
def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1

start = time.time()
lys = list(range(0, 100000))

val = 5628
print(InterpolationSearch(lys, val))
end = time.time()
print('Час виконання даної функції', end-start, 'c')