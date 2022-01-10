from base.linkedList import SingleLinkedList


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        last = None
        # 最终结果的头指向last，head最后指向None,因此要判断head是否为None
        while head:
            # print("head.val:", head.val)
            # 先备份head.next
            temp = head.next
            # 将head.next转向
            head.next = last
            # last，head一起向前移动
            last = head
            head = temp
            # print("last=%r, head=%r" %(last, head))

        # 返回last
        return last


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instance = Solution()

    # 初始化链表
    linkedList_instance = SingleLinkedList()
    linkedList_instance.initList([1, 2, 3, 4, 5])

    # 反转链表
    new_head = instance.reverseList(linkedList_instance.head)

    # 重新设置链表头节点，并打印整个链表
    linkedList_instance.setHead(new_head)
    SingleLinkedList.printList(linkedList_instance.head)
