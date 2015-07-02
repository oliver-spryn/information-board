#!/usr/bin/python

class Node(object):
    """A Node for use within a doubly-linked list.

    This class is part of a doubly-linked list data structure,
    and contains all of the elements which are necessary to hold
    data, and point to the previous and next Node objects.

    Attributes:
        data: The data being held by this node.
        next: The next Node in the doubly-linked list. Defaults to
            None, if there isn't a next Node.
        previous: The previous Node in the doubly-linked list.
            Defaults to None, if there isn't a previous Node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def set_next(self, node):
        """Add or change the next Node.

        The "next" attribute will be modified to point to the given
        "node" parameter. If there is already an existing next Node,
        then the provided Node will be placed in between the current
        Node and the the existing next Node.

        Args:
            node: A Node object to insert into the list after the
                current Node.
        """
        if self.next is None:
            self.next = node
        else:
            old_next = self.next

            self.next = node
            node.previous = self
            node.next = old_next

            old_next.previous = node

    def set_previous(self, node):
        """Add or change the previous Node.

        The "previous" attribute will be modified to point to the given
        "node" parameter. If there is already an existing previous Node,
        then the provided Node will be placed in between the current
        Node and the the existing previous Node.

        Args:
            node: A Node object to insert into the list before the
                current Node.
        """
        if self.previous is None:
            self.previous = node
        else:
            old_previous = self.previous

            self.previous = node
            node.next = self
            node.previous = old_previous

            old_previous.next = node