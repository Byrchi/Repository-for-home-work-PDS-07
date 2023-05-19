



print('Hello world!')



def binary_search(lst, val):
    first = 0
    last = len(lst) - 1
    index = -1
    while (first <= last) and (index== -1):
        mid = (first + last) // 2
        if lst[mid] == val:
            index = mid
        else:
            if val < lst[mid]:
                last = mid-1
            else:
                first = mid +1
    return index


l = list(range(0, 101))
# l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# l = [70, 30, 20, 70, 100, 60, 400, 20, 30, 100]
print(binary_search(l, 48))


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



