"""
A program for binary tree DFS traversal

preorder : root <-> left <-> right
inorder : left <-> root <-> right
posrorder : left <-> right <-> root
"""

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

    def preorder(self,root):
        if root:
            # print the data
            print(" {}".format(root.data))

            # recur left subtree
            self.preorder(root.left)

            # recur right subtree
            self.preorder(root.right)


    def inorder(self,root):
        if root:
            # recur left subtree
            self.inorder(root.left)

            # print the data
            print(" {}".format(root.data))

            # recur right subtree
            self.inorder(root.right)

    def postorder(self,root):
        if root:
            # recur left subtree
            self.postorder(root.left)

            # recur right subtree
            self.postorder(root.right)

            # print the data
            print (" {}".format(root.data))


if __name__ == "__main__":
    # Driver module
    #                 1
    #                / \
    #               2   3
    #              /   / \
    #             4   5   6
    #                      \
    #                      7
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.right.right = Node(7)

    print("preorder :-")
    root.preorder(root)

    print("inorder :- ")
    root.inorder(root)

    print("postorder :-")
    root.postorder(root)
