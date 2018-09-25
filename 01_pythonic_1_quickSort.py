import numpy

import time

def timmer(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        output = func(*args, **kwargs)
        time_end = time.time()
        print(f"耗时：{round(time_end-time_start,4)}s")
        return output
    return wrapper


def quicksort(array):
    less=[]
    greater=[]
    if len(array)<=1:
        return array
    pivot=array.pop()
    for x in array:
        if x < pivot:
            less.append(x)
        else:
            greater.append(x)
    less=quicksort(less)
    less.extend([pivot])#执行extend后直接在原列表后增加，返回空值，extend的参数必须为列表
    less.extend(quicksort(greater))
    return less


@timmer
def quickSortT(array):
    return quicksort(array)





if __name__ == '__main__':
    array= numpy.random.randint(1,20000000,size=10000000).tolist()
    # array=[10, 18, 3, 14, 10, 3, 11, 11, 18, 6]
    # print(array)
    sortedArray=quickSortT(array)
    # print(sortedArray)
    #一千万快排36秒
