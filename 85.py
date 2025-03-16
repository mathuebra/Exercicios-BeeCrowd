import sys
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = ''
        list2 = ''
        
        # 2 -> 4 -> 3
        # Transforma as listas em strings e posteriormente inteiros
        while True:
            list1 = str(l1.val) + list1
            holder = l1
            if holder.next == None:
                break
            l1 = l1.next
            
        while True:
            list2 = str(l2.val) + list2
            holder = l2
            if holder.next == None:
                break
            l2 = l2.next
        result = str(int(list1) + int(list2)) # Soma as listas
        
        dummy_head = ListNode(0) # Início da lista
        current = dummy_head
        
        for char in result[::-1]:
            current.next = ListNode(int(char))
            current = current.next
        
        return dummy_head.next # Primeiro elemento da lista encadeada