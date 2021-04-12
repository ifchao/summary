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

# 希尔排序: 内部排序, 不稳定


def TestSort() -> None:
    alist = [3, 1, 9, 24, 12, 34, 56, 97, 25]
    BubbleSort(alist)
    alist = [3, 1, 9, 24, 12, 34, 56, 97, 25]
    SelectSort(alist)
    alist = [3, 1, 9, 24, 12, 34, 56, 97, 25]
    InsertSort(alist)



if __name__ == '__main__':
    TestSort()
