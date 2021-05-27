# -*- coding: utf-8 -*-
# @Time : 2021/5/26 11:58 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : mi_01_introduction.py

"""
algothm:
    1、Sort the intervals on the start time to ensure a.start <= b.start
    2、If ‘a’ overlaps ‘b’ (i.e. b.start <= a.end), we need to merge them into a new interval ‘c’ such that:
        c.start = a.start
        c.end = max(a.end, b.end)
    3、We will keep repeating the above two steps to merge ‘c’ with the next interval if it overlaps with ‘c’.

"""

