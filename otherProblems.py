class LinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLinkedLists(lists):
  n = 0
  lst = []
  for node in lists:
    while node != None:
      lst.append(n.val)
      n = node.next

# ----------------------------------------------------------------

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class LinkedListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def traverseTree(root, orderedList):
  if root:
    traverseTree(root.left)
    orderedList.append(root)
    traverseTree(root.right)

def convert_tree_to_list(root):
  orderedList = []
  traverseTree(root, orderedList)
  for i in range(len(orderedList)):
    if i == 0:
      orderedList[i].left = None
    else :
      orderedList[i].left = orderedList[i - 1]
    if i == len(orderedList) - 1:
      orderedList[i].right == None
    else :
      orderedList[i].right = orderedList[i + 1]
    

#Let’s say a binary tree is "super balanced" if the difference between the depths 
# of any two leaf nodes is at most one. Write a function to check if a binary tree is 
# "super balanced".
def find_depth(root, current_depth, depth_list):
    if root.left:
        find_depth(root.left, current_depth + 1, depth_list)
    if root.right:
        find_depth(root.right, current_depth + 1, depth_list)
    if not root.left and not root.right:
        depth_list.append(current_depth)

def is_super_balanced(root):
    depth_list = []
    find_depth(root, 0, depth_list)
    return max(depth_list) - min(depth_list) <= 1