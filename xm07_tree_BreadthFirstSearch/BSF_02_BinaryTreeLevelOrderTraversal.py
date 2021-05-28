# -*- coding: utf-8 -*-
# @Time : 2021/5/28 2:43 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : BSF_02_BinaryTreeLevelOrderTraversal.py

"""
story:
    Given a binary tree, populate an array to represent its level-by-level traversal.
    You should populate the values of all nodes of each level from left to right in separate
    sub-arrays.

analysis
    1、首先这是一个树结构的广度优先遍历算法题：输入一个树，输出，每一层的Node元素值保存进列表
    2、利用python的collection模块下的deque 队列数据结构，实现先进先出

Instance:
    input: tree:        12
                    7         1
                  9         10  15

    output:Level order traversal: [[12], [7, 1], [9, 10, 5]]

"""
from collections import deque

from grokkingTheCoding.DataStructure.tree import TreeNode


def binary_tree_level_order_traverse(target_tree: TreeNode):
    """说明算法的本质：首先需求搞清楚==》怎么做搞清楚==》再写代码"""
    # step1：定义一个队列保存我们的Node
    queue = deque()
    queue.append(target_tree)
    # 存每一层遍历完的elements值
    result = []

    while queue:
        levelSize = len(queue)
        # 存当前层的node value
        temp_nodes = []

        for _ in range(levelSize):
            # 循环的开始当前Node出队列
            node_element = queue.popleft()  # 先进先出
            temp_nodes.append(node_element.val)

            # 循环的末尾子Node入队列
            if node_element.left:
                queue.append(node_element.left)
            if node_element.right:
                queue.append(node_element.right)

        result.append(temp_nodes)

    return result
# def traverse(root):
#     result = []
#     if root is None:
#         return result
#     quque = deque()
#     quque.append(root)
#     while quque:
#         leverSize = len(quque)
#         currentLevel = []
#         for _ in range(leverSize):
#             currentNode = quque.popleft()
#
#             currentLevel.append(currentNode.val)
#
#             if currentNode.left:
#                 quque.append(currentNode.left)
#             if currentNode.right:
#                 quque.append(currentNode.right)
#
#         result.append(currentLevel)
#
#     return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.rigth = TreeNode(5)

    print(binary_tree_level_order_traverse(root))  # yes yes


if __name__ == "__main__":
    main()
