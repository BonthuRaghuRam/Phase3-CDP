'''Approach I - Using Binary Search
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)-1
        def mergeTwoLists(list1,list2):
            if list1 == None:
                return list2
            elif list2 == None:
                return list1
            dummyNode=ListNode(-1)
            head=dummyNode
            tail=dummyNode
            while list1!=None and list2!=None:
                if list1.val<list2.val:
                    tail.next=list1
                    list1=list1.next
                else:
                    tail.next=list2
                    list2=list2.next
                tail=tail.next
            if list1:
                tail.next=list1
            else:
                tail.next=list2
            return head.next
        def mergeThem(lists, start, end):
            if start == end:
                return lists[start]
            mid = (start + end) // 2
            left = mergeThem(lists, start, mid)
            right = mergeThem(lists, mid + 1, end)
            return mergeTwoLists(left, right)

        if not lists:
            return None
        return mergeThem(lists, 0, len(lists) - 1)
        
        ''' 

'''Approach 2 - using Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)-1
        if n<0:
            return None
        def mergeTwoLists(list1,list2):
            if list1 == None:
                return list2
            elif list2 == None:
                return list1
            dummyNode=ListNode(-1)
            head=dummyNode
            tail=dummyNode
            while list1!=None and list2!=None:
                if list1.val<list2.val:
                    tail.next=list1
                    list1=list1.next
                else:
                    tail.next=list2
                    list2=list2.next
                tail=tail.next
            if list1:
                tail.next=list1
            else:
                tail.next=list2
            return head.next
        def mergeThem(i):
            if i == n:
                return lists[i]
            head2=mergeThem(i+1)
            head1=lists[i]
            return mergeTwoLists(head1,head2)
            
        return mergeThem(0)
        
        '''
