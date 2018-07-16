#!/usr/bin/env python
# @TIME     : 2018/7/16 14:22
# @AUTHOR   : GongTengPangYi
# @FILE     : KDTree.py
import numpy as np


class KDTree:
    # 根节点
    root = 0

    # 构建KD树
    def create(self, lists):
        if len(lists) > 0:
            list_x = []
            list_y = []
            for item in lists:
                # print(item)
                # print(item[1])
                list_x.append(item[0])
                list_y.append(item[1])
            self.root = KDTree.create_child(list_x, list_y)

    def __str__(self, *args, **kwargs):
        return "%s" % self.root

    @staticmethod
    def create_child(list_x, list_y):
        x_length = len(list_x)
        y_length = len(list_y)
        if x_length == 0 or y_length == 0 or x_length != y_length:
            return 0
        p_index = 0
        m_x = m_y = 0
        if np.std(list_x) > np.std(list_y):
            m_x = np.median(list_x)
            for index in range(len(list_x)):
                if list_x[index] == m_x:
                    p_index = index
            m_y = list_y[p_index]
        else:
            m_y = np.median(list_y)
            for index in range(len(list_y)):
                if list_y[index] == m_y:
                    p_index = index
            m_x = list_x[p_index]

        parent = KDNode(m_x, m_y)
        parent.set_left(KDTree.create_child(list_x[0 : p_index], list_y[0 : p_index]))
        parent.set_right(KDTree.create_child(list_x[p_index + 1 : len(list_x)], list_y[p_index + 1 : len(list_y)]))
        return parent

# KD算法的元素
class KDNode:
    # 元素的具体值
    x = 0
    y = 0
    # 子节点
    left_node = 0
    right_node = 0

    # 初始化
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 设置左节点
    def set_left(self, node):
        self.left_node = node

    # 设置右节点
    def set_right(self, node):
        self.right_node = node

    def __str__(self, *args, **kwargs):
        return "this is (%s, %s) " \
               "and the left is %s " \
               "and the right is %s"%(self.x, self.y, self.left_node, self.right_node)


# test
kdTree = KDTree()
kdTree.create([
    [1,2],
    [2,4],
    [1,7],
    [5,6],
    [7,10],
    [11,12],
    [3,9]
])
print(kdTree)