# -*- coding: utf-8 -*-
# @Time : 2021/5/24 11:03 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : FS_02_linkedList_cycle.py

"""
story:
    Given the head of a Singly LinkedList,
    write a function to determine if the LinkedList has a cycle in it or not.

analysis:
    也是双指针，但是一个fast 一个slow这个意义是什么你知道吗，就是同时出发，如果遇到cycle 那个快的一定能够追赶上慢的

instance:
    1->2->3->4->5->6
          <-
    output:true
"""


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head: Node):
    pointer_slow, pointer_fast = head, head
    while pointer_fast is not None and pointer_fast.next is not None:
        pointer_slow = pointer_slow.next
        pointer_fast = pointer_fast.next.next
        if pointer_fast == pointer_slow:
            return True
    return False


def main():
    # python自定义数据类型link_list链表
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next

    print(has_cycle(head))


if __name__ == "__main__":
    main()













