'''Approach I-without reversing Function
class Solution(object):
    def reverseKGroup(self, head, k):
        if head == None or head.next == None:
            return head
        mainHead, tail = None, None 
        length = 0 
        curr = head 
        while curr:
            curr = curr.next 
            length += 1 
        
        if length < k:
            return head
        curr = head
        while length >= k and curr:
            temp = curr 
            prev = None
            for i in range(k):
                next = curr.next 
                curr.next = prev 
                prev = curr 
                curr = next 
            
            if mainHead == None:
                mainHead = prev 
                tail = temp 
            else:
                tail.next = prev 
                tail = temp 
            length -= k
        tail.next = curr 
        return mainHead
'''

'''Approch II-using reverse Function
class Solution(object):
    def reverseKGroup(self, head, k):
        length = 0 
        curr = head 
        while curr:
            curr = curr.next 
            length += 1 

        def doReverse(head):
            prev, curr = None, head 
            while curr:
                next = curr.next 
                curr.next = prev 
                prev = curr 
                curr = next 
            return prev

        mainHead, tail = None, None 
        curr = head 
        while length >= k:
            temp = curr 
            prev = None
            for i in range(k):
                prev = curr 
                curr = curr.next
            prev.next = None 
            revHead = doReverse(temp)
            if mainHead == None:
                mainHead = revHead 
                tail = temp
            else:
                tail.next = revHead
                tail = temp 
            length -= k 
        tail.next = curr
        return mainHead'''

