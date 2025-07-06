# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#### clean beats 70%
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr =dummy
        heap=[]
        count=0
        for head in lists:
            if head:
                heapq.heappush(heap,(head.val,count,head))
                count+=1
        while heap:
            _,_,node =heapq.heappop(heap)
            curr.next=node #curr points to the smallest node
            curr =curr.next # we will edit this node's next pointer in the next round 
            #currently curr points to the smallest number's list's next item
            if curr.next:
                #push the next node
                heapq.heappush(heap,(curr.next.val,count,curr.next))
                count+=1
        return dummy.next    


#### cheating - brute force (beats 96%) !!!!!!!!!!!!!!!!!!!!!
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        values=[]
        for head in lists:
            while head:
                values.append(head.val)
                curr.next = head
                curr = curr.next
                head = head.next
        node=dummy
        values.sort()
        
        if values:
            head = ListNode(values[0])
            current = head
        else:
            return dummy.next
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next  # move the "pointer"
        return head
