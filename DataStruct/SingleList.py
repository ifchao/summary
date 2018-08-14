#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 单链表的Python语言实现
# 单链表的功能
'''
1.InitList: 初始化列表
2.is_empty: 判断是否为空
3.length: 返回链表的长度
4.travel: 遍历整个列表
5.add: 头部加入元素
6.append: 尾部添加元素
7.insert: 指定位置添加元素
8.remove: 删除元素
9.search: 查找节点
'''


class Node():
    '''节点类'''
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleList():
    '''单链表'''
    def __init__(self, node=None):
        '''初始化头节点为空'''
        self._head = node


    def is_empty(self):
        '''判断链表是否为空'''
        return self._head == None

    def length(self):
        '''判断链表长度'''
        # cur变量用来遍历链表
        cur = self._head
        # count 用来记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self._head
        while cur != None:
            print cur.elem,
            cur = cur.next

    def add(self, item):
        '''头部追加元素,头插法'''
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        '''尾部追加元素,尾插法'''
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置插入'''
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            '''首先使用变量pre遍历完pos-1的所有元素,并指向pos-1的节点'''
            pre = self._head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                # 头节点
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        '''查找节点是否存在'''
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleList()
    print ll.is_empty()
    print ll.length()
    ll.travel()
    ll.add(1)
    ll.travel()
    print '\n'
    ll.add(2)
    ll.append(3)
    ll.append(5)
    ll.append(7)

    ll.travel()
    print '\n'
    # 2,1,3,5,7
    ll.insert(2,4)
    ll.travel()
    # 2 1 4 3 5 7
    ll.remove(3)
    print "\n"
    ll.travel()
    ll.search(2)
