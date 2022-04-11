#!/bin/python3

import math
import os
import random
import re
import sys
import collections

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    
    def printLinkedList(head):
        node = head
        ats = []
        while node != None:
            ats.append(str(node.data))
            node = node.next
        print("-->".join(ats))
    
    
    print("data", data)
    print("initial")
    printLinkedList(head)
    
    ht = collections.OrderedDict()
    node = head
    while node:
        ht[node] = node.data
        node = node.next
    
    def bs(l, n):
        
        def search(lft, rgt, lis, ele):
            mid = lft + (rgt - lft)//2
            if lft == mid:
                return lft
            if lis[mid] > ele:
                return search(lft, mid, lis, ele)
            else:
                return search(mid, rgt, lis, ele)
        
        return search(0, len(l),l, n)
    
    ind = bs(list(ht.values()), data)
    #print("halues ", ht.values())
    #print("ind", ind)
    
    val = list(ht.values())
    target = val[ind]
    
    if target < data:
        while ind < len(val)-1 and val[ind] == val[ind+1]:
            ind = ind+1
    
    #print("new ind", ind)

    newNode = DoublyLinkedListNode(data)
    #print("taaget", target)
    
    i = 0
    tn = None
    for k,v in ht.items():
        if i == ind:
            tn = k
            break
        i = i+1
        
    
    node = head
    temp = None
    while node:
        if node == tn:
            if target <= data:
                temp = node.next 
                node.next = newNode
                newNode.next = temp
                if temp:
                    temp.prev = newNode
                    
            else:
                temp = node.prev
                node.prev = newNode
                newNode.next = node
                if temp:
                    temp.next = newNode
                else:
                    head = newNode     
        
        node = node.next
    
    print("final")
    printLinkedList(head)
    return head
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
