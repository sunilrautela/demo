
def reverse(self, head):
        if head is None or head.next is None:
            return head
      
        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None
        
        return rest
