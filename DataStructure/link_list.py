# -*- coding: utf-8 -*-
# @Time : 2021/5/27 12:03 AM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : link_list.py


class Link_list(object):

    def __init__(self, head, next=None):
        self.head = head
        self.next = next

    def print_link_list(self):
        temp = self
        while temp is not None:
            print(temp.head, end=" -> ")
            temp = temp.next
        print()



def main():
    my_link_list = Link_list(1)
    my_link_list.next = Link_list(2)
    my_link_list.next.next = Link_list(3)

    # print(str(my_link_list.print_link_list().value) + "->" +
    #       str(my_link_list.print_link_list().next.value) + "->" +
    #       str(my_link_list.print_link_list().next.next.value))
    my_link_list.print_link_list()


if __name__ == "__main__":
    main()
