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
    while current.next is not None:
        # step1 : store the next node
        _next = current.next
        # step2 :
    return linklist


def main():
    test = Link_list(2)
    test.next = Link_list(4)
    test.next.next = Link_list(6)
    test.next.next.next = Link_list(8)
    test.next.next.next.next = None

    print(reverse_link_list(test))


if __name__ == "__main__":
    main()
