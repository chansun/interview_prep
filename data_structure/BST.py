class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def add(node, val):
    if node == None:
        node = Node(val)
    else:
        if val < node.val: # go to the left branch
            if node.left == None:
                node.left = Node(val)
            else:
                return add(node.left, val)
        else: # go to the right branch
            if node.right == None:
                node.right = Node(val)
            else:
                return add(node.right, val)

# Get the minimum value from the tree
def getMin(node):
    if node == None:
        return float("inf") # error value
    if node.left == None:
        return node
    else:
        return getMin(node.left)

# In-order traversal
def inOrder(node):
    if node != None:
        inOrder(node.left)
        print(node.val)
        inOrder(node.right)

# 1. Delete a leaf node
# 2. Delete a node with one child node
# 3. Delete a node with both child nodes
def delete(node, val):
    if node == None:
        return 0
    # Find the target value
    if val < node.val: # go to the left branch
        node.left = delete(node.left, val)
    elif val > node.val: # go to the right branch
        node.right = delete(node.right , val)
    else: # found the target value
        if node.left == None:
            temp = node.right
            node = None
            return temp
        elif node.right == None:
            temp = node.left
            node = None
            return temp
        else: # if the current node has both child nodes ...
            temp = getMin(node.right) # find the minimum node from the right branch of the current node
            node.val = temp.val # swap the values of the minimum node of the right branch and the current node
            node.right = delete(node.left, temp.val) # delete the original minimum node of the right branch from the tree
    return node

