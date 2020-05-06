"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.   
"""
#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        '''
        self.l1: ListNode
        self.L2: ListNode
        L3: returned ListNode
        '''
        self.l1 = l1
        self.l2 = l2

        str1 = ""
        str2 = ""

        while self.l1 != None:
            str1 = "%s%s" % (str(self.l1.val), str1)
            self.l1 = self.l1.next
        # print('str1:', str1)

        while self.l2 != None:
            str2 = "%s%s" %(str(self.l2.val), str2)
            self.l2 = self.l2.next
        # print('str2:', str2)

        str3 = str(int(str1)+int(str2))
        # print('str3:', str3[-3])

        l3 = ListNode(str3[-1])
        temp = l3
        for i in range(1, len(str3)):
            temp.next = ListNode(str3[-i-1])
            temp = temp.next
        return l3
