"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        l3 = ListNode()
        cur3 = l3
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur3.val = cur1.val
                cur1 = cur1.next
            else:
                cur3.val = cur2.val
                cur2 = cur2.next
            cur3.next = ListNode()
            cur3 =cur3.next

        if cur1:
            while cur1:
                cur3.val = cur1.val
                cur1 = cur1.next
                if cur1:
                    cur3.next = ListNode()
                    cur3 = cur3.next
        elif cur2:
            while cur2:
                cur3.val = cur2.val
                cur2 = cur2.next
                if cur2:
                    cur3.next = ListNode()
                    cur3 = cur3.next
        else:
            l3 =l1
        return l3
