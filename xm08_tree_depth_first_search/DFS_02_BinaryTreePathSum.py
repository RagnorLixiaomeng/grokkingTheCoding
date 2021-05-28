# -*- coding: utf-8 -*-
# @Time : 2021/5/28 5:10 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : DFS_02_BinaryTreePathSum.py

"""
story:
    Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such
    that the sum of all the node values of that path equals ‘S’.

analysis:
    1、这不就是树的深度优先遍历嘛

Instance：
            1
         2      3
        4 5    6 7

    S: 10
    Output: true
    Explaination: The path with sum '10' is highlighted
"""
from grokkingTheCoding.DataStructure.tree import TreeNode


def binary_tree_path_sum(root: TreeNode, target_sum):
    # base case : 是才能 进行recurision
    if root is None:
        return False

    if root.val == target_sum and root.left is None and root.right is None:
        return True

    # recurisive case
    return binary_tree_path_sum(root.left, target_sum - root.val) or binary_tree_path_sum(root.right, target_sum - root.val)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.rigth = TreeNode(7)

    print(binary_tree_path_sum(root, 10))


if __name__ == "__main__":
    main()
