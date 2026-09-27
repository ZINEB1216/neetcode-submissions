# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = []
        if head is not None:
            curr = head
            while curr not in l:
                l.append(curr)
                head = head.next
                curr = head
                if head is None and curr not in l:
                    return False
            return True
        else:
            return False
        