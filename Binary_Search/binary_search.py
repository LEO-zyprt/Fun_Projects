import random
import time 


def naive_search(l, target):
    # l is a list or something
    for i in range(len(l)):
        if l[i] ==  target:
            return i
    return -1 

# binary search uses divide and conquer
# we will leverage the fact that our list is sorted (this is the fact)
def binary_search(i, target, low = None, high = None):
    
    if low == None:
        low = 0
    if high == None:
        high = len(i) - 1

    midpoint = (low + high) // 2
    
    if low > high:
        return -1

    if i[midpoint] == target:
        return midpoint
    elif target < i[midpoint]:
        return binary_search(i, target, low, midpoint-1)
    else:
        # target > i[midpoint]
        return binary_search(i, target, midpoint+1, high)

if __name__ == '__main__':
    # i = [1, 4, 5, 8, 10, 15]
    # target = 10
    # print(naive_search(i, target))
    # print(binary_search(i, target))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < 10000:
        sorted_list.add(random.randint(-3*length, +3*length))
    sorted_list = sorted(list(sorted_list))
    
    # naive search
    start_time = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end_time = time.time()
    print('Navie Search Time', (end_time - start_time)/length)

    # binary search
    start_time = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end_time = time.time()
    print('Navie Search Time', (end_time - start_time)/length)





