"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
from Food import Food
# Constants


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while len(source) > 0:
        stack.push(source.pop())

    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0, stack.pop())

    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()

    try:
        s.pop()
    except AssertionError:
        print("Pop on empty stack correctly raised an exception.")

    try:
        s.peek()
    except AssertionError:
        print("Peek on empty stack correctly raised an exception.")

    for item in source:
        s.push(item)
        print(f"Pushed {item} onto the stack. Top of stack is now: {s.peek()}")

    print("Test is_empty after pushing:", s.is_empty())

    while not s.is_empty():
        item = s.pop()
        print(f"Popped {item} from the stack.")

    print("Test is_empty after popping all items:", s.is_empty())

    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    source_len = len(source)
    for i in range(source_len):
        queue.insert(source.pop(0))

    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())

    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    q = Queue()

    print("The queue is empty: ", q.is_empty())
    print("The length should be 0:", len(q))
    q.insert(a[0])
    print("Is empty should now be false: ", q.is_empty())
    print("The length should now be 1: ", len(q))
    p = q.peek()
    print("The value added and peeked is:")
    print(p)
    r = q.remove()
    print("remove the value: ", r)
    print("Empty again: ", q.is_empty())

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    length = len(source)
    while i < length:
        pq.insert(source.pop(0))
        i += 1
    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    print("The p queue is empty: ", pq.is_empty())
    pq.insert(a[0])
    print("Is empty should now be false: ", pq.is_empty())
    p = pq.peek()
    print("The value added and peeked is:", p)
    pq.insert(a[1])
    p = pq.peek()
    print("The value added is:")
    print(a[1])
    print("and the value next up is:")
    print(p)
    r = pq.remove()
    print("remove the value: ", r)
    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        llist.append(source.pop(0))
    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(llist) > 0:
        target.append(llist.pop(0))


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    print(f"New list created. Is empty: {lst.is_empty()} (Expected: True)")

    # Append each item in the source to the list and print the updated list
    for item in source:
        lst.append(item)
        print(f"Appended {item} to list. New list: {lst}")

    # Assuming list_to_array and array_to_list functions are implemented elsewhere
    target_array = []
    list_to_array(lst, target_array)
    array_to_list(lst, target_array)

    # Remove the first item in the source from the list and print the updated list
    if source:
        value_to_remove = source[0]
        removed_value = lst.remove(value_to_remove)
        print(
            f"Removed {value_to_remove} from list. Removed: {removed_value} (Expected: {value_to_remove})")
        for l in lst:
            print(l)

    # Test max value of the list
    if lst.is_empty():
        print("List is empty, max should raise an assertion error.")
    else:
        max_value = lst.max()
        print(f"Max value of list: {max_value} (Expected: {max(source)})")

    # Test min value of the list
    if lst.is_empty():
        print("List is empty, min should raise an assertion error.")
    else:
        min_value = lst.min()
        print(f"Min value of list: {min_value} (Expected: {min(source)})")

    # Test finding a specific value in the list
    find_value = source[0] if source else None
    found_value = lst.find(find_value)
    print(f"Find {find_value} in list: Found {found_value} (Expected: {find_value if find_value in source else None})")

    # Test finding the index of a specific value in the list
    if source:
        index_value = source[0]
        found_index = lst.index(index_value)
        print(
            f"Index of {index_value} in list: {found_index} (Expected: {source.index(index_value) if index_value in source else -1})")

    # Test counting occurrences of a specific value in the list
    if source:
        count_value = source[0]
        count_result = lst.count(count_value)
        print(
            f"Count of {count_value} in list: {count_result} (Expected: {source.count(count_value)})")

    # Insert a new value at index 0 in the list and print the updated list
    insert_value = "test"
    lst.insert(0, insert_value)
    print(
        f"Insert {insert_value} at index 0: {lst} (Expected: [{insert_value}, ...rest of list...])")

    return
