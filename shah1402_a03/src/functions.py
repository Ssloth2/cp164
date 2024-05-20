"""
-------------------------------------------------------
functions
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports

from Stack_array import Stack
from utilities import array_to_stack, stack_to_array
# Constants


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()

    while not source1.is_empty() or not source2.is_empty():

        if not source1.is_empty():
            target.push(source1.pop())

        if not source2.is_empty():
            target.push(source2.pop())
    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    list = []
    stack_to_array(source, list)

    array_to_stack(source, list)

    return


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = False
    chars = ""
    for char in string:
        if char.isalpha():  # lower al letters and ignore what we dont want
            chars += char.lower()

    stack = Stack()
    for s in chars:
        stack.push(s)
    reversed_chars = ""
    while not stack.is_empty():
        reversed_chars += stack.pop()  # compare stacks togethers ex abc to cba
    if reversed_chars == chars:
        palindrome = True
    else:
        pass

    return palindrome


OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()

    elements = string.split()

    for element in elements:
        if element in OPERATORS:
            right_operand = stack.pop()
            left_operand = stack.pop()

            if element == '/' and right_operand == 0:
                stack.push("Eror")

            if element == '+':
                stack.push(left_operand + right_operand)
            elif element == '-':
                stack.push(left_operand - right_operand)
            elif element == '*':
                stack.push(left_operand * right_operand)
            elif element == '/':
                stack.push(left_operand / right_operand)

        else:
            stack.push(float(element))

    answer = stack.pop()
    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """

    try:
        current = "Start"
        choices = maze[current]
        path = []
        if "X" in choices:
            path.append("X")
        stack = Stack()
        while "X" not in choices:
            for c in choices:
                stack.push(c)
            current = stack.pop()
            if maze[current] != []:
                path.append(current)
            choices = maze[current]
            if "X" in choices:
                path.append("X")
    except:
        path = None
    finally:
        return path
