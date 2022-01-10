# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def setHead(self, node):
        self.head = node

    @staticmethod
    def printList(head):
        if head is None:
            return
        node = head
        while node is not None:
            print(node.val, end=',')
            node = node.next
