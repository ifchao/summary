#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 排序算法的原理以及Python实现
冒泡, 选择, 插入, 希尔, 归并, 快速, 堆排序, 计数排序, 桶排序, 基数排序
排序算法的说明:
    稳定: 如果a在b前面, a=b, 排序后a仍然会在b的前面
    不稳定: 如果a在b前面, a=b, 排序后a可能会在b的后面
    内排序: 所有排序操作都在内存中完成
    外排序: 由于数据太大, 因此把数据放在磁盘中, 而排序通过磁盘和内存的数据传输才能进行
    时间复杂度: 一个算法执行耗费的时间, (我们一般情况下说的都是平均时间复杂度)
    空间复杂度: 运行完一个程序所需要的内存的大小
排序算法分类:
    比较排序: 快速排序,归并排序,冒泡排序,堆排序,选择排序等属于比较排序,在排序的最终结果里,元素之间的次序依赖他们之间的比较。
        每个数都必须和其他数进行比较,才能确定自己的位置. 普遍时间复杂度为O(n^2), 通过分治法可以削减为logN次,所以时间复杂度
        为O(nlogn), 并且比较排序算法时间复杂度也不能突破O(nlogn), 因此也成为非线性时间比较排序
    非比较排序:计数排序,基数排序,桶排序属于非比较排序. 非比较排序是通过确定每个元素之前, 应该有多少个元素来排序, 针对数组arr,
        计算arr[i]之前有多少个元素, 则唯一确定了arr[i]在排序后数组中的位置.
        非比较排序只要确定了每个元素之前的已有的元素个数就可以了,所以一次遍历就可进行排序,时间复杂度为O(n)

"""


# 冒泡排序: 内部排序, 稳定, 比较排序
def BubbleSort(alist: list)->list: 
    """
    冒泡排序的原理: 内部排序, 稳定, 比较排序
        重复的走访需要排序的数列, 一次比较两个元素，如果他们的顺序错误就把他们交换过来。
        走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
        1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个
        2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
        3. 针对所有的元素重复以上的步骤，除了最后一个。
        4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    助记码:
        i∈[0,N-1)               //循环N-1遍
            j∈[0,N-1-i)           //每遍循环要处理的无序部分
                swap(j,j+1)          //两两排序（升序/降序）
    时间复杂度分析:
        最佳情况: T(n) = O(n)
        最差情况: T(n) = O(n^2)
        平均情况: T(n) = O(n^2)
    """
    print("BubbleSort:")
    print("Source List: ", alist)
    for i in range(1, len(alist)):           # 第一层循环决定需要进行多少次比较
        for j in range(len(alist)-i):        # 第二层循环遍历进行比较
    # 循环有多种写法
    #for i in range(len(alist)-1):           # 第一层循环决定需要进行多少次比较
    #    for j in range(len(alist)-1-i):        # 第二层循环遍历进行比较
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
        print("第{}次进行比较".format(i), alist)
    print('BubbleSort: ', alist)
    return alist


# 选择排序: 内部排序, 不稳定, 比较排序
def SelectSort(alist: list) -> list:
    """ 
    选择排序的原理: 内部排序, 不稳定, 比较排序
        选择排序是一种简单直观的排序, 无论放什么数据都是O(n^2)的时间复杂度, 使用的时候数据规模越小越好。
        1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
        2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
        3. 重复第二步，直到所有元素均排序完毕
    时间复杂度:
        最佳情况: T(n) = O(n^2)
        最差情况: T(n) = O(n^2)
        平均情况: T(n) = O(n^2)
    """
    print("SelectSort: ")
    print("Source List: ", alist)
    for i in range(len(alist) - 1):
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        if i != min_index:
            alist[i], alist[min_index] = alist[min_index], alist[i]
        print("第{}次进行选择".format(i), alist)
    print('BubbleSort: ', alist)
    return alist


# 插入排序: 内部排序, 稳定, 比较排序
def InsertSort(alist: list) -> list:
    """ 
    插入排序的原理: 内部排序, 稳定, 比较排序
        插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，对于未排序数据，
        在已排序序列中从后向前扫描，找到相应位置并插入。插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。
    步骤:
        将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
        从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置
        如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。
    """
    print("InsertSort: ")
    print("Source List: ", alist)
    for i in range(len(alist)):
        pre_index = i - 1
        current = alist[i]
        while pre_index >= 0 and alist[pre_index] > current:
            alist[pre_index + 1] = alist[pre_index]
            pre_index -= 1
        alist[pre_index + 1] = current
        print("第{}次进行插入".format(i), alist)
    print('InsertSort: ', alist)
    return alist


# 希尔排序: 内部排序, 不稳定, 比较排序
def ShellSort(alist: list) -> list:
    """ 
    希尔排序原理: 内部排序, 不稳定, 比较排序
        希尔排序也是一种插入排序, 简单插入排序经过改进后的高效的版本, 也称为缩小增量排序。
        与插入排序的不同之处在于, 会优先比较距离较远的元素。
    步骤:
        选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
        按增量序列个数 k，对序列进行 k 趟排序；
        每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，
        分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
    """
    step = len(alist) // 2
    while step > 0:
        for i in range(step, len(alist)):
            while i >= step and alist[i] < alist[i-step]:
                alist[i], alist[i-step] = alist[i-step], alist[i]
                i -= step
        step //= 2
    return alist

# 归并排序: 外部排序, 稳定, 比较排序
# 合并两个有序数组
def MergeSort(alist: list) -> list:
    """ 
    归并排序原理: 外部排序, 稳定, 比较排序
        归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。
        该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
        作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：
            自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
            自下而上的迭代；
    步骤:
        申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
        设定两个指针，最初位置分别为两个已经排序序列的起始位置；
        比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
        重复步骤 3 直到某一指针达到序列尾；
        将另一序列剩下的所有元素直接复制到合并序列尾。
    """
    if len(alist) <= 1:
        return alist
    num = int(len(alist) / 2)
    left = MergeSort(alist[:num])
    right = MergeSort(alist[num:])
    return Merge(left, right)

def Merge(left, right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result

# 快速排序: 内部排序, 不稳定, 比较排序
def quickSort(alist: list) -> list:
    """ 
    快速排序原理: 内部排序, 不稳定, 比较排序
        快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists）。
        快速排序又是一种分而治之思想在排序算法上的典型应用。本质上来看，快速排序应该算是在冒泡排序基础上的递归分治法。
        快速排序的名字起的是简单粗暴，因为一听到这个名字你就知道它存在的意义，就是快，而且效率高！
        它是处理大数据最快的排序算法之一了
    步骤:
        从数列中挑出一个元素，称为 "基准"（pivot）;
        重新排序数列，所有元素比基准值小的摆放在基准前面，
        所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，
        该基准就处于数列的中间位置。这个称为分区（partition）操作；
        递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；
    """
    if len(alist) >= 2:  # 递归入口及出口        
        mid = alist[len(alist)//2]  # 选取基准值，也可以选取第一个或最后一个元素        
        left, right = [], []  # 定义基准值左右两侧的列表        
        alist.remove(mid)  # 从原始数组中移除基准值        
        for num in alist:            
            if num >= mid:                
                right.append(num)            
            else:                
                left.append(num)        
        return quickSort(left) + [mid] + quickSort(right) 
    else:        
        return alist
 








def TestSort() -> None:
    alist = [3, 1, 9, 24, 12, 34, 56, 97, 25]
    print(quickSort(alist))
    print(alist)




if __name__ == '__main__':
    TestSort()
