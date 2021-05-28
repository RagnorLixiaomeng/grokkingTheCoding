# -*- coding: utf-8 -*-
# @Time : 2021/5/28 4:59 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : DFS_01_algorithm.py

"""
name: DFS

scene:
    1、树的深度遍历的问题，譬如求root到leaf的所有的路径

algorithm:
    using recursion (or we can also use a stack for the iterative approach)
    to keep track of all the previous (parent) nodes while traversing

solution:
    1、recursion


Instance Solution:
    1、Start DFS with the root of the tree.
    2、If the current node is not a leaf node, do two things:
        2.1、Subtract the value of the current node from the given number to get a new sum => S = S - node.value
        2.2、Make two recursive calls for both the children of the current node with the new number calculated in the previous step.
    3、At every step, see if the current node being visited is a leaf node and if its value is equal to the given number ‘S’. If both these conditions are true, we have found the required root-to-leaf path, therefore return true.
    4、If the current node is a leaf but its value is not equal to the given number ‘S’, return false.


    1、深度优先搜索先以tree的root节点开始
    2、如果当前的节点不是一个leaf节点（这里是需要遍历到最底部），做两件事
        第一件事：用目标值减去当前节点的值获取一个新的目标值，这个目的是为了带着这个目标值向下遍历
        第二件事：写两个递归去分别递归目标节点的left node 跟 right node
    3、如果节点是leaf就比较leaf跟最后减剩下的目标值，一样就是true，不一样就是false

"""