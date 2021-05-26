# -*- coding: utf-8 -*-
# @Time : 2021/5/22 4:22 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : sw03_smallest_subarray_with_targetNum.py

"""
story:Given an array of positive numbers and a positive number ‘S’,
    find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
    Return 0, if no such subarray exists.

analysis:
    input: array, target_length
    output: smallest subarray: single num OR array

instance:
    Input:[2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

    Input: [2, 1, 5, 2, 8], S=7
    Output: 1
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

    Input: [3, 4, 1, 1, 6], S=8
    Output: 3
    Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

"""

# 两步解决：
#   1、实现sliding window的算法
#   2、对sw中的k进行循环判断，取最小的k就行


# def smallest_subarray_with_targetNum(array: list, targetNum:int):
#     for window_lengh in range(1, len(array)):  # 窗户的长度：1-》len(array)
#         windowSum_collection = sw_algorithm(array, window_lengh)
#         for subarray_index in range(len(windowSum_collection)):  # 有没有 >= targetNum的数
#             if windowSum_collection[subarray_index] >= targetNum:
#                 print((window_lengh, windowSum_collection[subarray_index], array[subarray_index:subarray_index + window_lengh]))
#
#
# def sw_algorithm(array: list, k: int)-> list:
#     windowSum: float = 0.0
#     result: list = []
#     windowStart: int = 0
#     for windowEnd in range(len(array)):
#         windowSum += array[windowEnd]
#
#         if windowEnd >= k - 1:
#             result.append(windowSum)
#             windowSum -= array[windowStart]
#             windowStart += 1
#     return result
#
#
# def main():
#     array_1 = [3, 4, 1, 1, 6]
#     k = 8
#     smallest_subarray_with_targetNum(array_1, k)
#
#
# if __name__ == "__main__":
#     main()


""" 
提供的解法会更优雅：
    1、用window_start右移控制和减少
    2、用window_end 右移动控制和增加
    3、用窗体的长度表示需要几个数
    4、用window_start 与 window_end都向右侧移动来表示所有的组合
"""


def smallest_subarray_with_targetNum(array: list, targetNum:int)->list:
    window_start: int = 0
    current_sum: float = 0.0
    smallest_subarrays: array = []

    for window_end in range(len(array)):
        current_sum += array[window_end]
        while current_sum >= targetNum:
            # print(current_sum, window_end, window_start)
            smallest_subarrays.append(array[window_start:window_end + 1])
            current_sum -= array[window_start]
            window_start += 1
    return smallest_subarrays


def main():
    array_1 = [3, 4, 1, 1, 6]
    k = 8
    print(smallest_subarray_with_targetNum(array_1, k))


if __name__ == "__main__":
    main()
