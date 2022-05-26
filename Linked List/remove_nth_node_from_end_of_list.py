class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        lengthPtr = head
        
        while lengthPtr is not None:
            lengthPtr = lengthPtr.next
            length += 1
        
        if length == n:
            head = head.next
            return head
        
        curr = head
        
        for i in range(length - n - 1):
            curr = curr.next
            
        curr.next = curr.next.next
        
        return head
            