#!/usr/bin/python3
"""Defines a Node and a SinglyLinkedList."""


class Node:
    """A class defining a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node instance.

        Args:
            data (int): The data value of the node.
            next_node (Node, optional): The next node in the linked list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data attribute.

        Args:
            value (int): The new value for the data attribute.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next_node attribute.

        Args:
            value (Node): The new value for the next_node attribute.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """A class defining a singly linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList instance with an empty list."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value to be inserted into the list.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the entire list."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
