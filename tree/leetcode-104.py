# Press the green button in the gutter to run the script.
from base.binaryTree import BinaryTree


class Solution(object):
    """
    问题：代码在leetcode中返回是正确结果3，但在pyCharm中执行，返回却是4。
    原因分析：binaryTree.initTree中，将list转换为tree的初始化流程不正确，导致结果不一致。
    """

    def maxDepth(self, root):
        if root is not None:
            return self.getDepth(0, root)
        else:
            return 0

    def getDepth(self, level, node):
        # 1. 递归终结者
        if node is None:
            return level

        # 本次递归的操作
        level = level + 1
        print('level:%d, node:%d' % (level, node.val))

        left_level = self.getDepth(level, node.left)
        right_level = self.getDepth(level, node.right)

        # 因为是求最长路径，将较大的返回给上一个递归
        # 如果是最短路径，将较小的返回个上一个递归
        return left_level if (left_level > right_level) else right_level


if __name__ == '__main__':
    instance = Solution()

    # 构建一棵树
    inputList = [3, 9, 20, None, None, 15, 7]
    tree_instance = BinaryTree()
    tree_instance.initTree(inputList)
    print('tree root:', tree_instance.root.val)
    BinaryTree.printTree_preorder(tree_instance.root)
    print('************************************')
    BinaryTree.printTree_inorder(tree_instance.root)
    print('************************************')
    BinaryTree.printTree_postorder(tree_instance.root)

    print('####################################')
    # 返回最长路径
    result = instance.maxDepth(tree_instance.root)
    print('result=%s' % result)
