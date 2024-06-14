# Approach I
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Check if the list is empty
        if head is None:
            return head
        
        # Check if the head node needs to be removed
        while head and head.val == val:
            head = head.next
            if not head:
                return head
        
        # Start from the second node
        prev = head
        curr = head.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
                
        return head
# Approach II
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        dummyNode=ListNode(-1)
        tail=dummyNode
        currNode=head
        while currNode:
            if currNode.val!=val:
                tail.next=currNode
                tail=tail.next
            currNode=currNode.next
            tail.next=None
        return dummyNode.next

