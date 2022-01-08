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

    # inputList = [3, 9, 20, None, None, 15, 7]
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


    @staticmethod
    def printTree_preorder(head):
        def printNode(node):
            if node is None:
                return

            print("%s, %s, %s" % (node.val, node.left, node.right))
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
            print("%s, %s, %s" % (node.val, node.left, node.right))
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
            print("%s, %s, %s" % (node.val, node.left, node.right))

        if head is None:
            return
        else:
            printNode(head)

