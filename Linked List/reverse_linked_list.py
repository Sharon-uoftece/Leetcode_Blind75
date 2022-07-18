    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        newNode = None
        
        if head:
            prevNode = ListNode(head.val)
            head = head.next
        
        while(head):
            newNode = ListNode(head.val)
            newNode.next = prevNode
            prevNode = newNode
            
            head = head.next
        
        return newNode