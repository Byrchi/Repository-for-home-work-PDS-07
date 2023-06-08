import random
from random_words import RandomWords
import time


int_list = []
float_list = []
str_list = []
word = RandomWords()
for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.01, 100.0))
    str_list.append(word.random_word())


# print(int_list)
# print(float_list)
# print(str_list)

##### Task_02 #####
def bubble_sort(data):
    lenght = len(data)
    for iIndex in range(lenght):
        swapped = False
        for jIndeex in range(0, lenght - iIndex -1):
            if data [jIndeex] > data[jIndeex + 1]:
                data[jIndeex], data[jIndeex + 1] =  data[jIndeex + 1], data[jIndeex]
                swapped = True
        if not swapped:
            break
    # print('Sorted data', data)


cor_time = time.time()
bubble_sort(int_list)
print('*'*50)
print(f'Duration time: {time.time() - cor_time}')

cor_time = time.time()
bubble_sort(float_list)
print('*'*50)
print(f'Duration time: {time.time() - cor_time}')

cor_time = time.time()
bubble_sort(str_list)
print('*'*50)
print(f'Duration time: {time.time() - cor_time}')


def average_time(arr, q_iteration):
    results_sum = 0
    for i in range(q_iteration):
        cor_time = time.time()
        bubble_sort(arr)
        res_time = time.time() - cor_time
        results_sum  += res_time
    result = results_sum/q_iteration
    return print(result)
print('*'*50)
average_time(int_list, 10)
average_time(float_list, 10)
average_time(str_list, 10)
