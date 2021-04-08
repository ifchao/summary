#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 所有排序算法的原理以及Python实现

排序算法的说明:
    稳定: 如果a在b前面, a=b, 排序后a仍然会在b的前面
    不稳定: 如果a在b前面, a=b, 排序后a可能会在b的后面
    内排序: 所有排序操作都在内存中完成
    外排序: 由于数据太大, 因此把数据放在磁盘中, 而排序通过磁盘和内存的数据传输才能进行
    时间复杂度: 一个算法执行耗费的时间, (我们一般情况下说的都是平均时间复杂度)
    空间复杂度: 运行完一个程序所需要的内存的大小

"""


# 冒泡排序: 内部排序, 稳定,
def BubbleSort(alist: list) -> tuple: 
    """
    冒泡排序的原理:

    """
    return 1, 2

def test_sort() -> None:
    BubbleSort([1,3,2])


if __name__ == '__main__':
    test_sort()
