# -*- coding: utf-8 -*-
# @Time : 2021/5/27 10:14 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : IPRAL_01_introduction.py

"""
scenes:
    就死在很多情况下，需要我们解决对链表中某一些nodes进行反转，当然也可以是整个链表

algorithm:
    1、要反转LinkedList，我们需要一次反转一个节点。我们将从一个变量开始，该变量current最初指向LinkedList的头部，另一个变量previous指向我们已处理的上一个节点；最初previous将指向null。

    2、以逐步的方式，我们将current通过previous在继续下一个节点之前将其指向节点来反转该节点。另外，我们将更新，previous使其始终指向已处理的上一个节点。这是我们算法的直观表示：

"""

