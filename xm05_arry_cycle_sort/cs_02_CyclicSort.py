# -*- coding: utf-8 -*-
# @Time : 2021/5/27 6:43 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : cs_02_CyclicSort.py

"""
story:
    We are given an array containing ‘n’ objects.
    Each object, when created, was assigned a unique number
    from 1 to ‘n’ based on their creation sequence.
    This means that the object with sequence number ‘3’ was created just
    before the object with sequence number ‘4’.

    Write a function to sort the objects in-place on their creation sequence number
    in O(n)O(n) and without any extra space. For simplicity,
    let’s assume we are passed an integer array containing only the
    sequence numbers, though each number is actually an object.

analysis:
    1、 就是利用下标，然后 0 对 1 这样，如果在正确的位置不用管，如果我们迭代的当前数字不在正确的索引处，那么我们将其与正确的索引处的数字交换
    2、有一点你需要清楚，start指针是不会动的，除非start指针指向的位置值是对的，swap操作是只要当前start指针指向的数字不正确，就swap
instance：
    Input: [3, 1, 5, 4, 2]
    Output: [1, 2, 3, 4, 5]
"""


def cycle_sort(array: list) -> list:
    start = 0
    while start < len(array):
        correct_location = array[start] - 1
        if array[start] != array[correct_location]:
            array[start], array[correct_location] = array[correct_location], array[start]  # swap
        else:
            start += 1  # move start next
    return array


def main():
    array_1 = [3, 1, 5, 4, 2]
    print(cycle_sort(array_1))


if __name__ == "__main__":
    main()
