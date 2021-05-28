# -*- coding: utf-8 -*-
# @Time : 2021/5/27 10:28 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : IPRAL_02_Reverse_a_linklist.py

"""
story:
    Given the head of a Singly LinkedList, reverse the LinkedList.
    Write a function to return the new head of the reversed LinkedList.

analysis:
    1、用模式-一个previous， 一个current，我感觉跟尼玛双指针法一样

Instance:
    input: Nodes of original LinkedList are: 2 4 6 8 10
    output: Nodes of reversed LinkedList are: 10 8 6 4 2

"""

from grokkingTheCoding.DataStructure.link_list import Link_list


def reverse_link_list(linklist: Link_list)-> Link_list:
    previous, current, _next = None, linklist, None  # init variable
    while current is not None:
        # step1 : 先把current 的正序的next存储起来
        _next = current.next
        # step2 : 既然是反转，就把current 的 next指向以前的previous
        current.next = previous
        # step3 : 既然是反转，那本来的previous应该指向当前的current
        previous = current
        # step4 : 最后移动到下一个链表的元素上,这里就是步骤1存在的意义
        current = _next
    # return linklist  # 这个是错的，你知道为啥吗，因为经过反转后，结合你定义的数据结构，previous才是最后保存所有的人
    return previous


def main():
    test = Link_list(2)
    test.next = Link_list(4)
    test.next.next = Link_list(6)
    test.next.next.next = Link_list(8)
    test.next.next.next.next = None
    test.print_link_list()

    reverse_link_list(test).print_link_list()


if __name__ == "__main__":
    main()
