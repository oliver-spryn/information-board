#!/usr/bin/python

class LinkedList(object):
    """A doubly-linked list.

    This doubly-linked list works in conjunction with Node objects.
    This class has the ability to manipulate the list from both
    ends of the chain.

    Attributes:
        last: A pointer to the last Node in the list.
        list: A pointer to the first Node in the list.
        size: The number of Nodes in the list.
    """

    def __init__(self):
           self.last = None
           self.list = None
           self.size = 0

    def front(self):
        """Access the first element.

        Also obtainable via LinkedList.list.

        Returns:
            The first element in the list, which may be None, if no
            list has been established, yet.
        """

        return self.list

    def push_back(self, data):
        """Pushes a new Node on the back of the list.

        Args:
            data: A piece of data, which will be placed inside of a
                Node object, to add to the list.
        """

        n = Node(data)

        if self.list is None:
            self.list = n
            self.last = self.list
            self.size = 1
        else:
            self.last.set_next(n)
            self.last = self.last.next
            self.size += 1

    def push_front(self, data):
        """Pushes a new Node on the front of the list.

        Args:
            data: A piece of data, which will be placed inside of a
                Node object, to add to the list.
        """

        n = Node(data)

        if self.list is None:
            self.list = n
            self.last = self.list
            self.size = 1
        else:
            self.list.set_previous(n)
            self.list = self.list.previous
            self.size += 1