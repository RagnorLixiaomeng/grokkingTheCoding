# -*- coding: utf-8 -*-
# @Time : 2021/5/21 12:42 AM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : sw01_algorithm.py

"""
story:Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

analysis:
    input: array, k
    output: array

instance:
    Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
    Output: [2.2, 2.8, 2.4, 3.6, 2.8]

"""

# TODO: step1: A brute-force algorithm
# A brute-force algorithm：计算每5个子序列的累加
# Time: o(n * k) n是数组的长度，k next ‘K’ elements  Space：o(k)
# def find_average_of_all_contuguous_subarrays(array: list, k: int) -> list:
#     result: list = []
#
#     for i in range(len(array) - k + 1):
#         temp: float = 0.0
#         for j in range(i, i+k):
#             temp += array[j]
#         result.append(temp/k)
#     return result
#
#
# def main():
#     array_1 = [1, 3, 2, 6, -1, 4, 1, 8, 2]
#     k = 5
#     print(find_average_of_all_contuguous_subarrays(array_1, k))
#
#
# if __name__ == "__main__":
#     main()

# TODO: step2: Analysis brute-force algorithm weakness
# 算法优化：上面那个算法的问题在于每次的temp跟下次都会有4个元素是重复加的
"""
i=0,j=0,1,2,3,4 ==> temp = arr[0] + arr[1] + arr[2] + arr[3] + arr[4] 
i=1,j=1,2,3,4,5 ==> temp =          arr[1] + arr[2] + arr[3] + arr[4] + arr[5]

==>common sum is arr[1] + arr[2] + arr[3] + arr[4] calculate twice

"""


# TODO: step3: A sliding-window algorithm partern
def find_average_of_all_contuguous_subarrays(array: list, k: int) -> list:
    # 这些变量是写下面逻辑代码发现需要后再添加的
    window_sum: float = 0.0
    result: list = []
    window_start: int = 0

    for windowEnd in range(len(array)):
        window_sum += array[windowEnd]  # add the next element
        # only when window is reach k length we sliding the window
        if windowEnd >= k - 1:
            result.append(window_sum / k)  # calculate the average
            window_sum -= array[window_start]  # subtract the element going out
            window_start += 1  # slid the window ahead
    return result


def main():
    array_1 = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    print(find_average_of_all_contuguous_subarrays(array_1, k))


if __name__ == "__main__":
    main()
