import time
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def run(executor_class, n):
    start_time = time.time()
    cpu = os.cpu_count()
    with executor_class() as executor:
        results = list(executor.map(factorial, [n] * cpu))
    end_time = time.time()
    result_time = end_time - start_time
    return result_time

def run_normal(n):
    start_time = time.time()
    results = [factorial(n) for _ in range(8)]
    end_time = time.time()
    result_time = end_time - start_time
    return result_time

if __name__ == '__main__':
    n = 100000
    threadpoolexecutor =  run(ThreadPoolExecutor, n)
    processpoolexecutor = run(ProcessPoolExecutor, n)
    normal = run_normal(n)

    print(f"Results for test: threadpoolexecutor: {threadpoolexecutor} ")
    print(f"Results for test: processpoolexecutor : {processpoolexecutor} ")
    print(f"Results for test: normal : {normal} ")


    if threadpoolexecutor < processpoolexecutor and normal:
       print(f"Найшвидчий метод threadpoolexecutor: {threadpoolexecutor} seconds")
    elif processpoolexecutor < threadpoolexecutor and normal:
       print(f"Найшвидчий метод processpoolexecutor : {processpoolexecutor} seconds")
    elif normal < processpoolexecutor and threadpoolexecutor:
        print(f"Найшвидчий метод normal : {normal} seconds")

