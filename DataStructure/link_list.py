# -*- coding: utf-8 -*-
# @Time : 2021/5/27 12:03 AM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : link_list.py


class Link_list(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_link_list(self):
        return self


def main():
    my_link_list = Link_list(1)
    my_link_list.next = Link_list(2)
    my_link_list.next.next = Link_list(3)

    print(str(my_link_list.print_link_list().value) + "->" +
          str(my_link_list.print_link_list().next.value) + "->" +
          str(my_link_list.print_link_list().next.next.value))


if __name__ == "__main__":
    main()
