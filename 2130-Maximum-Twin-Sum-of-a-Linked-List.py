# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
     #find middle
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow
    #reverse from middle for 1,2  3,4->1,2  4,3
        while curr:
            next_n=curr.next
            curr.next=prev
            prev=curr
            curr=next_n
    #find max_sum of two sum or n sum
        first=head
        second=prev
        ans=0
        while second:
            ans=max(ans,first.val+second.val)
            first=first.next
            second=second.next
        return ans
            