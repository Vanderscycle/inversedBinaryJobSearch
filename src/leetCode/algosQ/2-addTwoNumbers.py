# Definition for singly-linked list.
class ListNode:
    """
    e.g. ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.
        
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
        """
        
        l3numbStr = str(self.linkedList2Num(l1) + self.linkedList2Num(l2))
        
        l3 = ListNode()
        flagFirst = True

        for i in l3numbStr:
            if flagFirst == True:
                l3 = ListNode(int(i))
                flagFirst = False

            else:
                l3 = ListNode(int(i), next=l3)
        
        return l3


def linkedList2Num(self,l: ListNode) -> int:
        """
        helper function to tranform the linked list object into a number.
        """
        strNumb = ''
        #navigate the list
        while l != None:
            strNumb += str(l.val)
            l = l.next

        return int(strNumb[::-1])

            


