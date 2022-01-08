# Press the green button in the gutter to run the script.
from base.binaryTree import BinaryTree


class Solution(object):
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.func(root)
        return self.result

    def func(self, root):
        if root is None:
            return root
        self.result.append(root.val)
        self.func(root.left)
        self.func(root.right)


if __name__ == '__main__':
    instance = Solution()

    inputList = [1, None, 2, 3, 4]
    tree_instance = BinaryTree()
    tree_instance.initTree(inputList)
    print('tree root:', tree_instance.root.val)
    BinaryTree.printTree_preorder(tree_instance.root)

    result = instance.preorderTraversal(tree_instance.root)
    print('result=%s'%result)
