#include <iostream>
 
class BinTreeNode(object):
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        # If the node is left of the root
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
        # If the node is right of the root

    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print(tree.value)
    if(tree.right!=None):
        in_order(tree.right)

# --------------------------------------------

def in_order_iterative(tree):
    stack = []
    permatree = tree
    Complete = False
    Counter = 0
    while Complete == False:
        
        while tree.left!=None:
            stack.append(tree.value)
            tree = tree.left
        stack.append(tree.value)
        print(stack)
        
        print("Left:",tree.value)
        stack.pop()

        while stack:
            while tree.right!=None:
                tree = tree.right
                print("Right:",tree.value)
            #print(stack)

            tree = permatree
            for x in range(Counter):
                tree = tree.right
            while tree.value != stack[-1]:
                tree = tree.left
            print("Left:",tree.value)
            stack.pop()
        Complete = True

        if Complete == True:
            tree = permatree
            for x in range(Counter):
                tree = tree.right
            if tree.right!=None:
                Complete = False
                tree = tree.right
                #print("Not complete, taking:",tree.value)
                Counter = Counter + 1
    # Nothing on the left, ouput value, check right...
    # This method doesn't cover all posilibites however is close.


def in_order_iterative_2(tree):
    stack = []
    # Every left element is added to the stack for right comparison
    Complete = False
    current = tree
    
    while Complete == False:
        # Current as a flexible variable, either None or a value
        # appending each left element to the stack, and checking if
        # there is a right value for each of these elements.
        if current is not None:
            stack.append(current)
            current = current.left
            # This allows all left elemements to be discovered
            # by setting False when the subtree is exhausted.
        else:
            if(len(stack)>0):
                current = stack[-1]
                # "Backtracks" to next element
                print(current.value)
                stack.pop()
                current = current.right 
            else:
                Complete = True
                # When stack is empty.
               
def tree_sort(array):
    for x in array:
        tree_insert(t, x)
    in_order(t)


#        6
#       /  \
#      5    10
#     /       \
#    3         15
#     \        /
#      4      12
#               \
#                14
#               /
#             13

# --------------------------------------------


 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  array = [10,5,15,3,4,12,14,13]
  tree_sort(array)
  print("----------")
  in_order_iterative_2(t)
