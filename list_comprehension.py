#explicit for loop takes more time
# thus if possible use list comprehension
#This program shows the difference in time between these two implementation

from timeit import timeit

def for_loop():
    result = []
    for i in range(1000):
        result.append(i)
        return result

def list_comprehension():
    return [i for i in range(1000)]

expSize = 1000
time1 = timeit(for_loop, number=expSize)
time2 = timeit(list_comprehension,number=expSize)

print(f'list comprehension is {round(time1/time2,2)} times faster than for-loop')

#output: list comprehension is 0.01 times faster than for-loop