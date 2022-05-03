class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        
        if not l1 or not l2:
            return l1 or l2
        
        
        if l1.val <= l2.val:
            return ListNode(l1.val, next = self.mergeTwoLists(l1.next, l2))
        else:
            return ListNode(l2.val, next = self.mergeTwoLists(l1,l2.next))