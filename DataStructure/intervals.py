# -*- coding: utf-8 -*-
# @Time : 2021/5/27 12:07 AM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : intervals.py


class Intervals():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]")


def main():
    Intervals(1, 4).print_interval()
    Intervals(2, 7).print_interval()


if __name__ == "__main__":
    main()
