# 链表实现

from typing import Optional

class TreeNode:
    def __init__(self, value: int = 0, 
                 left: Optional['TreeNode'] = None, 
                 right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right

def pre_traverse(node: TreeNode=None):
    """递归实现前序遍历"""
    if node == None:
        return
    
    print(node.value)
    pre_traverse(node.left)
    pre_traverse(node.right)

def pre_traverse_stack(root: TreeNode=None):
    """迭代实现前序访问"""
    stack = []

    node = root
    while node or stack:
        while node:
            print(node.value)
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        node = node.right

    return 

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    pre_traverse(root)
    print('')
    pre_traverse_stack(root)

    return

if __name__ == '__main__':
    main()


    

