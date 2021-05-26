# -*- coding: utf-8 -*-
# @Time : 2021/5/24 4:08 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : TP_02_remove_duplicates.py


"""
story:
    Given an array of sorted numbers, remove all duplicates from it.
    You should not use any extra space;
    after removing the duplicates in-place return the new length of the array.

analysis:
    1、有序数组
    2、子集

instance：
    Input: [2, 3, 3, 3, 6, 9, 9]
    Output: 4
    Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

"""

# method1: 利用集合去重


# def remove_duplicates(array: list)->set:
#     un_duplicates_array = set(array)
#     return un_duplicates_array
#
#
# def main():
#     arr_1 = [2, 3, 3, 3, 6, 9, 9]
#     print(remove_duplicates(arr_1))
#
#
# if __name__ == "__main__":
#     main()


# method2： 双指针法
# 一个指针负责遍历，另一个指针负责记录动了多少次，这个是什么概念呢。就是只有遇到重复的element才会动，

def remove_duplicates(array:list):
    pointer_unduplicates: int = 0
    pointer_iterable: int = 1
    unduplicates_element_length: int = 1
    while pointer_iterable <= len(array) - 1:
        if array[pointer_iterable] - array[pointer_unduplicates] != 0:
            unduplicates_element_length += 1
            pointer_unduplicates = pointer_iterable

        pointer_iterable += 1
    return pointer_unduplicates, unduplicates_element_length


def main():
    arr_1 = [2, 3, 3, 3, 6, 9, 9]
    print(remove_duplicates(arr_1))


if __name__ == "__main__":
    main()
