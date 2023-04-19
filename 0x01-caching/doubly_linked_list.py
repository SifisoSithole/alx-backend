#!/usr/bin/env python3
"""
`DoubleLinkedList` module
"""
from typing import Any

class Node:
    """
    Node of the linked list

    Attributes:
    ----------
    key : Any
        The key to keep track of it's frequency
    frequency : int
        keeps track of the number of times the key is accessed
    next : Node
        the next node in the list
    prev : Node
        the previous node in the list
    """

    def __init__(self, key: Any):
        """
        initialize a node

        Parameters:
        ----------
        key : Any
            The key to keep track of it's frequency
        """
        self.key = key
        self.frequency = 0
        self.next = None
        self.prev = None


class DoubleLinkedList:
    """
    Implemantation of a doubly linked list

    Attributes:
    ----------
    head : Node
        head of the node
    tail : Node
        tail of the node

    Methods:
    -------
    add_node(key: Any):
        adds a new node at the tail of the list
    """

    def __init__(self):
        """
        initialize linked list
        """
        self.head = None
        self.tail = None

    def add_node(self, key : Any):
        """
        adds a new node at the tail of the list

        Parameters:
        ----------
        key : Any
            key to add to the list
        """
        if key is None:
            return
        new_node = Node(key)
        if self.head is None:
            # if head is None
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail:
            # if the head and tail is the same node
            if self.tail.frequency == 0:
                # if the tail and new node have the same frequency
                # sort using the least recenty used
                new_node.next = self.tail
                self.tail.prev = new_node
                self.head = new_node
            else:
                # insert in the tail 
                self.head.next = new_node
                new_node.prev = self.head
                self.tail = new_node
        else:
            if self.tail.frequency == 0:
                # if the tail and new node have the same frequency
                # sort using the least recenty used
                new_node.next = self.tail
                self.tail.prev.next = new_node
                new_node.prev = self.tail.prev
                self.tail.prev = new_node
            else:
                # insert at the tail
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail


    def swap_nodes(self, Node1, Node2):
        """
        Swap two nodes
        Parameters:
        ----------
        Node1 : Node
            first node to swap
        Node2 : Node
            second node to swap
        """
        if self.head == None or self.head.next == None or Node1 == Node2:
            return
    
        if Node1 == self.head:
            self.head = Node2
        elif Node2 == self.head:
            self.head = Node1
        if Node1 == self.tail:
            self.tail = Node2
        elif Node2 == self.tail:
            self.tail = Node1
 
        # Swapping Node1 and Node2
        temp = None
        temp = Node1.next
        Node1.next = Node2.next
        Node2.next = temp
 
        if Node1.next != None:
            Node1.next.prev = Node1
        if Node2.next != None:
            Node2.next.prev = Node2
 
        temp = Node1.prev
        Node1.prev = Node2.prev
        Node2.prev = temp
 
        if Node1.prev != None:
            Node1.prev.next = Node1
        if Node2.prev != None:
            Node2.prev.next = Node2


    def delete_tail_node(self) -> Any:
        """
        deletes a node at the tail of the list

        Returns:
            the deleted key
        """
        if self.tail is None:
            print(self.tail)
            return
        key = self.tail.key
        prev_node = self.tail.prev
        prev_node.next = None
        self.tail = prev_node
        return key

    def update_node(self, key : Any):
        """
        updates the node and orders the linked, the most used at the
        head and the least used at the tail

        Parameters:
        ----------
        key : Any
            key to update
        """
        if key is None or self.head is None:
            return
        curr_node = self.head
        if curr_node.key == key:
            self.head.frequency += 1
            return
        
        while curr_node:
            if curr_node.key == key:
                curr_node.frequency += 1
                while curr_node.prev is not None and curr_node.frequency >= curr_node.prev.frequency:
                    self.swap_nodes(curr_node, curr_node.prev)
                #self.print_list()
                return
            curr_node = curr_node.next

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(f'key: {curr_node.key} frequency: {curr_node.frequency}')
            curr_node = curr_node.next
        

        
    
