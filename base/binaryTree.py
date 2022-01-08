# Definition for singly-linked list.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
这样我们需要注意的那三个问题的回答自然就有了（做递归问题，心中要想着怎么回答这三个问题）：

在我们的任务中，终止条件是什么？
[给我们的字符用完，也就不需要再创建节点了]
在我们的任务中，本次递归要干嘛？
[本次递归要创建三个节点，一个根节点，一个左节点，一个右节点]
在我们的任务中，本次递归要返回给上一次递归的是啥？
[当然是返回一个本层构造好的树的根节点]
"""


class BinaryTree:
    def __init__(self):
        self.root = None

    def initTree(self, data):
        self.root = None
        self.root = self._createTree(self.root, data)

    def _createTree(self, root, data):
        # 创建头结点
        if len(data) == 0:  # 终止条件：val用完了
            return root
        if data[0] is not None:  # 本层需要干的就是构建Root、Root.lchild、Root.rchild三个节点。
            root = TreeNode(data[0])
            print("%d," % root.val)
            data.pop(0)
            root.left = self._createTree(root.left, data)
            root.right = self._createTree(root.right, data)
            return root  # 本次递归要返回给上一次的本层构造好的树的根节点
        else:
            root = None
            print("None,")
            data.pop(0)
            return root
