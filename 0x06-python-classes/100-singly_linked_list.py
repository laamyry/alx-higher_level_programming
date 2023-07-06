#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:

    def __init__(self, da_ta, n_node=None):

        self.da_ta = da_ta
        self.n_node = n_node

    @property
    def da_ta(self):

        return (self.__data)

    @da_ta.setter
    def da_ta(self, value):
        if not isinstance(value, int):
            raise TypeError("da_ta must be an integer")
        self.__data = value

    @property
    def n_node(self):

        return (self.__next_node)

    @n_node.setter
    def n_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("n_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    def __init__(self):

        self.__head = None

    def sorted_insert(self, value):

        new_node = Node(value)
        if self.__head is None:
            new_node.n_node = None
            self.__head = new_node
        elif self.__head.da_ta > value:
            new_node.n_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.n_node is not None and
                    temp.n_node.da_ta < value):
                temp = temp.n_node
            new_node.n_node = temp.n_node
            temp.n_node = new_node

    def __str__(self):

        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.da_ta))
            temp = temp.n_node
        return ('\n'.join(values))
