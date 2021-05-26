# -*- coding: utf-8 -*-
# @Time : 2021/5/21 10:02 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : sw02_maximum_sum_subarray_of_size_k.py

"""
story: Given an array of positive numbers and a positive number ‘k’,
        find the maximum sum of any contiguous subarray of size ‘k’.

analysis:
    input: array, k
    output:array

instance:
    [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3]

"""

# time: o(n) space: o(n + 1) ==>o(n)


def maximum_sum_of_subarray(array: list, k: int)-> tuple:
    window_sum: float = 0.0
    result: list = []
    window_start = 0

    for windowEnd in range(len(array)):
        window_sum += array[windowEnd]
        if windowEnd >= k - 1:
            result.append(window_sum)
            window_sum -= array[window_start]
            window_start += 1
    return result, array[find_maximun_subarray(array): find_maximun_subarray(array) + 3]  # 列表切片


def find_maximun_subarray(array: list)-> int:
    # 问题在于如果有相同的就不行了，只取第一个
    return array.index(max(array))


def main():
    array_1 = [2, 1, 5, 1, 3, 2]
    k = 3
    print(maximum_sum_of_subarray(array_1, k))


if __name__ == "__main__":
    main()

