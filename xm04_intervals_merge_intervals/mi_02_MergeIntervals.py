# -*- coding: utf-8 -*-
# @Time : 2021/5/26 11:48 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : mi_02_MergeIntervals.py

"""
story:
    Given a list of intervals,
    merge all the overlapping intervals to produce a list
    that has only mutually exclusive intervals.

analysis:
    例如时间间隔的重叠，a间隔 跟 b间隔之间有6种关系，把这6中关系梳理清楚就可以
    1: ----
            ---- 这就是两者无重叠overlap
    2: ----
          ---- 这就是下 在 上 之后结束
    3: ----
        --   这就是下完全被上覆盖
    4： ----
      ----   这就是上 在 下之后结束
    5： ----
      ------- 这就是下完全覆盖上
    6：       ----
          --  这就是下离开上无重叠

    ==> 因为我们的算法是先排序，所以 a的start 一定是 <= b的start
    1：√
    2：√
    3：√
    4：×
    5：√
    6：×

    所以考虑的是1、2、3、5、注意5的情况是因为下完全覆盖上的话 可以出现a.start = b.start



instance：
    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
    one [1,5].

"""

"""
1、第一步先对这种intervals进行首段排序：1， 2， 7
2、第二步排序后的intervals中的两个进行比较
3、重复往后直到最后
"""
from grokkingTheCoding.DataStructure.intervals import Intervals


# step:1
def sort_intervals(intervals:list):
    # sort the Interval start
    # for i in range(len(intervals) - 1):
    #     if intervals[i].start > intervals[i+1].start:
    #         intervals[i], intervals[i+1] = intervals[i+1], intervals[i]

    """看看大神的sort"""
    intervals.sort(key=lambda x: x.start)
    return intervals


# step:2
def merge_two_intervals(k: Intervals, w: Intervals, sorted_intervals: list, recursion_depth, result):
    # 递归的出口
    recursion_depth += 1
    if recursion_depth == len(sorted_intervals) - 1:
        return

    # k = sorted_intervals[recursion_depth - 1]
    # w = sorted_intervals[recursion_depth]
    w_next = sorted_intervals[recursion_depth + 1]

    # result: list

    # default k.start <= w.start
    if w.start > k.end:
        merge_two_intervals(w, w_next, sorted_intervals, recursion_depth, result)
    else:
        end = max(w.end, k.end)
        result.append([k.start, end])
        merge_two_intervals(Intervals(k.start, end), w_next, sorted_intervals, recursion_depth, result)

    return result  # 这个result 是 merged的集合

    # 以上的算法，最后一个元素是不会比到的
    # 以上的算法，没办法获取到最终合并后的结果，只能获得merged操作后的集合，没有overlap关系的不管
    # 这两点需要处理，至少一点可以认可，你的递归思路是对的

# def merge_two_intervals(sorted_intervals: list, recurision=0):
#     # 递归的出口
#     recurision += 1
#     if recurision == len(sorted_intervals) - 1:
#         return
#
#     current_interval = sorted_intervals[recurision - 1]
#     next_interval = sorted_intervals[recurision]
#     next_next_interval = sorted_intervals[recurision + 1]
#
#     # default k.start <= w.start
#     if current_interval.end < next_interval.start:
#         # merge_two_intervals(next_interval, next_interval.next)
#         merge_two_intervals(next_interval, next_next_interval)
#     else:
#         end = max(next_interval.end, current_interval.end)
#         # merge_two_intervals(Intervals(current_interval.start, end), next_interval.next)
#         merge_two_intervals(Intervals(current_interval.start, end), next_next_interval)


def merge(intervals: list):
    """大神的解法"""
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(interval.end, end)
        else:
            mergedIntervals.append(Intervals(start, end))
            start = interval.start
            end = interval.end

    mergedIntervals.append(Intervals(start, end))
    return mergedIntervals


def main():
    intervals = sort_intervals([Intervals(2, 5), Intervals(1, 4),
                                Intervals(7, 9), Intervals(8, 15),
                                Intervals(18, 20)])
    # print(merge_two_intervals(intervals[0], intervals[1], intervals, 0, []))
    print(merge(intervals))


if __name__ == "__main__":
    main()



