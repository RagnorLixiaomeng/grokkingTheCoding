# -*- coding: utf-8 -*-
# @Time : 2021/5/28 2:35 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : BFS_01_algorithm.py

"""

scene:
    traverse a tree

algorithm:
    name: BFS:广度搜索优先

solution:
    We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:

    1、Start by pushing the root node to the queue.
    2、Keep iterating until the queue is empty.
    3、In each iteration, first count the elements in the queue (let’s call it levelSize). We will have these many nodes in the current level.
    4、Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
    5、After removing each node from the queue, insert both of its children into the queue.
    6、If the queue is not empty, repeat from step 3 for the next level.

    1、第一步先初始化一个队列数据类型：LILO，注意python的collection容器中提供的deque是一个双端队列
    2、将tree的root节点先push到队列中
    3、重复遍历，直到这个队列为空
    4、在每一次遍历中，首先统计队列中的元素的长度，这个长度就是levelSize，这个levelsize啥意思呢，就是树的该层Node节点有多少个
    5、然后移除到队列中的每一个node，但是把当前node的子node都给插入到队列中
    6、如果当前队列不为空，重复第三步
"""

