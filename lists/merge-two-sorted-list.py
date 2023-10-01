'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]'''

# solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # append items in list and then make a new LL out of it. Cons - extra space.
        # newLL = []
        # if list1 and list2 is None:
        #     return list1
        # while list1 is not None:
        #     newLL.append(list1.val)
        #     list1 = list1.next
        # while list2 is not None:
        #     newLL.append(list2.val)
        #     list2 = list2.next
        # newLL.sort() #sorted the list
        # result = ListNode(-1) #creating new LL for the result
        # temp = result
        # for i in range(len(newLL)):
        #     result.next = ListNode(newLL[i])
        #     result = result.next
        # return temp.next
        
        #append items in LL in real time by comparing the values in both the list
        dummy = ListNode()
        temp = dummy
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2
        return dummy.next

        # less faster approach

        # if not list1 or not list2:
        #     return list2 or list1
        # elif list1.val <= list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2