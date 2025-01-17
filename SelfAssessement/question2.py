#!/usr/bin/env python3

from collections import deque

# node class for tree structure
class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data  
        self.right = right  
        self.left = left  

# function to convert expression string to a list of items
def expr_to_items(expression: str) -> list:
    items = []
    number = ""  # temporary variable
    for char in expression:
        if char.isdigit():  
            number += char
        else:
            if number:  # if number is not empty, add it to item list
                items.append(number)
                number = ""
            if char in "+-*/":  # if the character is an operator, add it to items
                items.append(char)
    if number:  # append any remaining numberber at the end
        items.append(number)
    return items

# function to convert an expression string into a binary expression tree
def text_to_tree(expression: str) -> list:
    items = expr_to_items(expression) 

    # precedence map for operators
    precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2}

    # helper function to handle operators and build the tree
    def handle_operator(operators, vals):
        operator = operators.pop()  
        right_node = vals.pop() 
        left_node = vals.pop()  
        vals.append(Node(operator, right_node, left_node))  

    operators = []  # stack to store operators
    vals = []  # stack to store operand nodes

    # parse through items
    for item in items:
        if item.isdigit():  # if item is a numberber, create a node and push to vals
            vals.append(Node(item))
        elif item in precedence_map:  # if item is an operator
            while (operators and precedence_map[operators[-1]] >= precedence_map[item]):
                handle_operator(operators, vals)  
            operators.append(item)  # push the current operator onto the stack

    # handle any remaining operators
    while operators:
        handle_operator(operators, vals)

    root = vals[0]  

    node_queue = deque([root])  # queue for BFS traversal
    visited_nodes = set()  # set to track visited nodes
    result = []  # list to store the result edges

    while node_queue:
        current_node = node_queue.popleft()
        if current_node in visited_nodes:
            continue

        visited_nodes.add(current_node)

        data = current_node.data  # get the node data
        left_node = current_node.left  # left child
        right_node = current_node.right  # right child

        if left_node:  # if left child exists, create edge string and add to result
            edge = f'"{data}" -> "{left_node.data}" // left'
            result.append(edge)
            node_queue.append(left_node)
        if right_node:  # if right child exists, create edge string and add to result
            edge = f'"{data}" -> "{right_node.data}" // right'
            result.append(edge)
            node_queue.append(right_node)

    return result

# function to print output lines
def print_output(output: list) -> None:
    for line in output:
        print(line)

if __name__ == "__main__":
    expression1 = "2*7+3"  # Test 1: Example expression
    output1 = text_to_tree(expression1)  

    expression2 = "8/2*10"  # Test 2: Another example expression
    output2 = text_to_tree(expression2)  
    print_output(output1) 
    print('\n')  
    print_output(output2)  