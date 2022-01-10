"""
对于二叉树这种数据结构，通常使用递归的方式去处理

这样我们需要注意的那三个问题的回答自然就有了（做递归问题，心中要想着怎么回答这三个问题）：

在我们的任务中，终止条件是什么？
[给我们的字符用完，也就不需要再创建节点了]
在我们的任务中，本次递归要干嘛？
[本次递归要创建三个节点，一个根节点，一个左节点，一个右节点]
在我们的任务中，本次递归要返回给上一次递归的是啥？
[当然是返回一个本层构造好的树的根节点]
"""
from abc import abstractmethod, ABCMeta


# Definition for singly-linked list.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeBase(metaclass=ABCMeta):
    """
    The test case base class
    User should implement the below 3 methods:
        setup: for test setup
        test: The main test body
        cleanup: Clean the test
    """
    def __init__(self):
        self.root = None

    @abstractmethod
    def initTree(self, data):
        """
        init create tree, input a list
        """
        pass

    @staticmethod
    def printTree_preorder(head):
        def printNode(node):
            if node is None:
                return

            node_left_val = 'None'
            node_right_val = 'None'
            if node.left is not None:
                node_left_val = node.left.val
            if node.right is not None:
                node_right_val = node.right.val
            print("%s: %s, %s" % (node.val, node_left_val, node_right_val))
            printNode(node.left)
            printNode(node.right)

        if head is None:
            return
        else:
            printNode(head)

    @staticmethod
    def printTree_inorder(head):
        def printNode(node):
            if node is None:
                return

            printNode(node.left)
            print("%s: %s, %s" % (node.val, node.left, node.right))
            printNode(node.right)

        if head is None:
            return
        else:
            printNode(head)

    @staticmethod
    def printTree_postorder(head):
        def printNode(node):
            if node is None:
                return

            printNode(node.left)
            printNode(node.right)
            print("%s: %s, %s" % (node.val, node.left, node.right))

        if head is None:
            return
        else:
            printNode(head)


"""
二叉树分类：
1、满二叉树
所有叶结点同处于最底层（非底层结点均是内部结点），一个深度为k(>=-1)且有2^(k+1) - 1个结点。如图（图来源于veil的博客）：

2、完全二叉树
叶结点只能出现在最底层的两层，且最底层叶结点均处于次底层叶结点的左侧。

3、平衡二叉树
它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
"""


# 除了叶子节点之外都有2个子树的二叉树
class BinaryTreeForTwoChild(BinaryTreeBase):
    def __init__(self):
        super().__init__()

    # test: inputList = [3, 9, 20, None, None, 15, 7]
    def initTree(self, data):
        def level(index):
            if index >= len(data) or data[index] is None:
                return None

            root = TreeNode(data[index])
            if index == 0:
                # 给self.root赋值，保存根节点
                self.root = root
            root.left = level(2 * index + 1)
            root.right = level(2 * index + 2)
            return root

        return level(0)


# 除叶子节点之外，含有1个子树的二叉树
class BinaryTreeForOneChild(BinaryTreeBase):
    def __init__(self):
        super().__init__()

    # test: inputList = [1, None, 2, 3, 4]
    def initTree(self, data):
        def level(root, tmp_data):
            # 创建头结点
            if len(tmp_data) == 0:  # 终止条件：val用完了
                return root
            if tmp_data[0] is not None:  # 本层需要干的就是构建Root、Root.lchild、Root.rchild三个节点。
                root = TreeNode(tmp_data[0])
                # print("%d," % root.val)
                tmp_data.pop(0)
                root.left = level(root.left, tmp_data)
                root.right = level(root.right, tmp_data)
                return root  # 本次递归要返回给上一次的本层构造好的树的根节点
            else:
                root = None
                # print("None,")
                tmp_data.pop(0)
                return root

        self.root = level(self.root, data)
