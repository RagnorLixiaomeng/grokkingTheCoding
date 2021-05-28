# -*- coding: utf-8 -*-
# @Time : 2021/5/24 3:31 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : TP_01_algorithm.py

"""
name: two-pointer 双指针法

goal:
    当我们处理有序数组、或者链表的时候，经常会遇到一种问题：我们需要找到该有序数组或者链表中的满足某些约束的子集。

instance：
    给定一个有序数字数组和一个目标总和，请在该数组中找到一对总和等于给定目标的组合。

    SUM、给定输入数组已排序，一种有效的方法是从一个指针开始处开始，另一个指针结束处开始。在每一步中，我们都会看到两个指针所指向的数字是否加起来等于目标总和。
    如果他们不这样做，我们将做以下两件事之一：

    1、如果两个指针所指向的两个数字的和大于目标和，则意味着我们需要一个对和较小的对。因此，要尝试更多对，我们可以减少端点指针。
    2、如果两个指针所指向的两个数字的和小于目标和，则意味着我们需要一个具有更大和的对。因此，要尝试更多对，我们可以增加起始指针。

"""


def two_pointer_algorithm(array: list, targetNum: int)->tuple:
    pointer_start: int = 0
    pointer_end: int = len(array) - 1
    while pointer_end > pointer_start:
        current_value = array[pointer_start] + array[pointer_end]
        if current_value == targetNum:
            return array[pointer_start], array[pointer_end]
        elif current_value < targetNum:
            pointer_start += 1
        elif current_value > targetNum:
            pointer_end -= 1


def main():
    arr_1 = [1, 2, 3, 4, 6]
    target_sum = 6
    print(two_pointer_algorithm(arr_1, target_sum))


if __name__ == "__main__":
    main()
