from typing import List


class Node:
    def __init__(self, key):
        self.left_node = None
        self.right_node = None
        self.key = key


def traversal_inorder_asc(node: Node, asc_values: List[int] = None) -> List[int]:
    if asc_values is None:
        print('initialized')
        asc_values = []

    if node.left_node:
        traversal_inorder_desc(node.left_node, asc_values)

    print(node.key)
    asc_values.append(node.key)

    if node.right_node:
        traversal_inorder_desc(node.right_node, asc_values)

    return asc_values

def traversal_inorder_desc(node: Node, desc_values: List[int] = None) -> List[int]:
    if desc_values is None:
        print('initialized')
        desc_values = []

    if node.right_node:
        traversal_inorder_desc(node.right_node, desc_values)

    desc_values.append(node.key)

    if node.left_node:
        traversal_inorder_desc(node.left_node, desc_values)

    return desc_values

# # A function to do inorder tree traversal
# def printInorder(root):
#     if root:
#         # First recur on left child
#         printInorder(root.left)
#
#         # then print the data of node
#         print(root.val),
#
#         # now recur on right child
#         printInorder(root.right)
#
#
# # A function to do postorder tree traversal
# def printPostorder(root):
#     if root:
#         # First recur on left child
#         printPostorder(root.left)
#
#         # the recur on right child
#         printPostorder(root.right)
#
#         # now print the data of node
#         print(root.val),
#
#
# # A function to do preorder tree traversal
# def printPreorder(root):
#     if root:
#         # First print the data of node
#         print(root.val),
#
#         # Then recur on left child
#         printPreorder(root.left)
#
#         # Finally recur on right child
#         printPreorder(root.right)


# Driver code
root = Node(3)
root.left_node = Node(2)
root.right_node = Node(4)
root.left_node.left_node = Node(1)
root.right_node.right_node = Node(5)


# print
# "Preorder traversal of binary tree is"
# printPreorder(root)

# print
# "\nInorder traversal of binary tree is"
# printInorder(root)
print(traversal_inorder_desc(root))
print(traversal_inorder_asc(root))

# print
# "\nPostorder traversal of binary tree is"
# printPostorder(root)