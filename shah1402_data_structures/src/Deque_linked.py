"""
-------------------------------------------------------
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-02-13"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Deques are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a deque (Deque)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        return

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._front is None:  # if it is empty
            new_node = _Deque_Node(value, None, None)
            self._rear = new_node
            self._front = new_node
        else:

            new_node = _Deque_Node(value, None, self._front)
            self._front = new_node

        self._count += 1

        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        new_node = _Deque_Node(value, self._rear, None)
        if self._front is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node

        self._count += 1
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"

        value = self._front
        self._front = self._front._next

        self._count -= 1
        if self._count == 0:
            self._rear = None
        else:
            self._front._prev = None

        return value._value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"
        value = self._rear
        self._rear = self._rear._prev

        self._count -= 1
        if self._count == 0:
            self._front = None
        else:
            self._rear._next = None
        return value._value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"

        value = deepcopy(self._front._value)
        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"

        value = deepcopy(self._rear._value)
        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"
        # ex [1,2,3] swap (0,1) (l,r)
        # If l and r are not the same node
        if l is not r:
            # Swap the _prev and _next pointers of l and r
            l._prev, r._prev, l._next, r._next = r._prev, l._prev, r._next, l._next

            # Check if l's previous node is l itself
            if l._prev is l:
                # If so, update l's previous node to be r
                l._prev = r

            # Check if l's next node is l itself
            elif l._next is l:
                # If so, update l's next node to be r
                l._next = r

            # Check if r's previous node is r itself
            if r._prev is r:
                # If so, update r's previous node to be l
                r._prev = l

            # Check if r's next node is r itself
            elif r._next is r:
                # If so, update r's next node to be l
                r._next = l

            # Update _front pointer if needed
            if l._prev is None:
                self._front = l
            else:
                # Update the next node of l's previous node to be l
                l._prev._next = l

            # Update _rear pointer if needed
            if l._next is None:
                self._rear = l
            else:
                # Update the previous node of l's next node to be l
                l._next._prev = l

            # Update _front pointer if needed
            if r._prev is None:
                self._front = r
            else:
                # Update the next node of r's previous node to be r
                r._prev._next = r

            # Update _rear pointer if needed
            if r._next is None:
                self._rear = r
            else:
                # Update the previous node of r's next node to be r
                r._next._prev = r
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
