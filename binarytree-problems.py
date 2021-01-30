# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                   # Display the plot

# import re
# texts = 'https://www.geeksforgeeks.org/'
# patterns = '(\w+)://'

# # print(re.findall(patterns, texts))
# print(re.findall(r"^(http[s]?:)+\/\/([^:\/\s]+)([^#?\s]+)\?([^#]*)?(#.*)?$",
#  "HTtpS://reGexr.com/more/less/path/foo.php?q=bar&same[12]=xxx&same[11]=#sldns13123nfdwdw", re.IGNORECASE)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_node(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)

        return res

    # Postorder traversal
    # Left ->Right -> Root
    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.data)
        return res

    # find val method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

    # bottom_up
    def max_depth_bottom_up(self, root):
        left_maxdepth = 0
        right_maxdepth = 0
        if root:
            if root.left:
                left_maxdepth = self.max_depth_bottom_up(root.left)
            if root.right:
                right_maxdepth = self.max_depth_bottom_up(root.right)
            return max(left_maxdepth, right_maxdepth) + 1
        else:
            return 0

    # top-down
    def max_depth_top_down2(self, root):
        return self.max_depth_top_down(root, 1)

    def max_depth_top_down(self, root, depth):
        # 1. return if root is null
        # 2. if root is a leaf node:
        # 3.      answer = max(answer, depth)         // update the answer if needed
        # 4. maximum_depth(root.left, depth + 1)      // call the function recursively for left child
        # 5. maximum_depth(root.right, depth + 1)     // call the function recursively for right chil
        left_maxdepth = 0
        right_maxdepth = 0
        if root.left is None and root.right is None:
            return depth

        if root.left:
            left_maxdepth = self.max_depth_top_down(root.left, depth+1)
        if root.right:
            right_maxdepth = self.max_depth_top_down(root.right, depth+1)

        return max(left_maxdepth, right_maxdepth)

    def size(self, root):
        if root:
            return 1 + self.size(root.left) + self.size(root.right)
        else:
            return 0

    def mirror(self, root):
        if root:
            rl = root.right
            root.right = self.mirror(root.left)
            root.left = self.mirror(rl)

        return root

    def get_leafs(self, root):
        leafs = []
        if root:
            if root.left is None and root.right is None:
                leafs.append(root.data)
            else:
                if root.left:
                    leafs = leafs + self.get_leafs(root.left)
                if root.right:
                    leafs = leafs + self.get_leafs(root.right)

        return leafs

    def count_leafs(self, root):
        leafs = 0
        if root:
            if root.left is None and root.right is None:
                leafs = leafs+1
            else:
                if root.left:
                    leafs = leafs + self.count_leafs(root.left)
                if root.right:
                    leafs = leafs + self.count_leafs(root.right)

        return leafs

    def get_root2leaf_paths(self, root):
        paths = []
        path = []
        if root:
            if root.left is None and root.right is None:
                path.append(root.data)
                paths.append(path)
                return paths
            else:
                if root.left:
                    for p in self.get_root2leaf_paths(root.left):
                        paths.append(p+[root.data])
                if root.right:
                    for p in self.get_root2leaf_paths(root.right):
                        paths.append(p + [root.data])
        return paths


root = Node(27)
root.insert_node(14)
root.insert_node(35)
root.insert_node(10)
root.insert_node(19)
root.insert_node(31)
root.insert_node(42)
root.insert_node(52)
root.insert_node(62)

# print(root.inorder_traversal(root))
# print(root.preorder_traversal(root))
# print(root.postorder_traversal(root))

# print(root.findval(7))
# print(root.findval(14))

# print(root.max_depth_bottom_up(root))
# print(root.max_depth_top_down2(root))
# print(root.size(root))

# print("original")
# root.print_tree()
# root.mirror(root)
# print("mirrored")
# root.print_tree()

# print(root.get_leafs(root))
# print(root.count_leafs(root))

print(root.get_root2leaf_paths(root))

# count the leafs
