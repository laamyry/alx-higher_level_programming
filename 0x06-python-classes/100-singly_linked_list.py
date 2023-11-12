#!/usr/bin/python3
"""defines a node of a singly linked list by:"""


class Node:
    '''Node class'''
    def __init__(self, data, next_node=None):
        '''init def'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''data def'''
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''Node SinglyLinkedList'''
    def __init__(self):

        self.__head = None

    def sorted_insert(self, value):

        n_node = Node(value)
        if self.__head is None:
            n_node.next_node = None
            self.__head = n_node
        elif self.__head.data > value:
            n_node.next_node = self.__head
            self.__head = n_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            n_node.next_node = temp.next_node
            temp.next_node = n_node

    def __str__(self):
        '''str def'''
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
