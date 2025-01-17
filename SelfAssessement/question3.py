#!/usr/bin/env python3

# function to convert a tree structure to text

#recursion to solve :)
def tree_to_text(tree, root_node):
    # base case: if the current node has no children
    if not tree[root_node]:
        return root_node.split('_')[1]

    # recursively process left and right
    left = tree[root_node][0]
    right = tree[root_node][1]

    # get the expressions for the left and right subtrees
    left_expr = tree_to_text(tree, left)
    right_expr = tree_to_text(tree, right)

    # get operator
    operator = root_node.split('_')[1]

    # return the string
    return f"{left_expr}{operator}{right_expr}"

if __name__ == "__main__":
    # test case 1
    tree =  {"n1_+": ["n2_*","n3_3"], "n2_*":["n4_2","n5_7"], "n4_2":[],"n5_7":[],"n3_3":[]}
    root_node = "n1_+"  
    print(tree_to_text(tree, root_node)) 

    # test case 2
    tree ={'n1_+': ['n2_3', 'n3_*'], 'n3_*': ['n4_/', "n5_2"], 'n4_/': ["n6_10", "n7_5"], "n6_10": [], "n7_5": [], "n5_2": [], 'n2_3': []}
    root_node = "n1_+" 
    print(tree_to_text(tree, root_node)) 