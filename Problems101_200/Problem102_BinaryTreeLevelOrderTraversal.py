# short Solution idea
# 1. Put root in queue
# 2. While queue has nodes:
#       - Get number of nodes in this level
#       - Process that many nodes:
#            * record values
#            * push children in queue
#       - Save level list
# 3. Return result

# Simple Pseudocode
# FUNCTION levelOrder(root):

#     IF root is NULL:
#         RETURN empty list

#     create an empty queue
#     push root into queue

#     create result list

#     WHILE queue is not empty:

#         get size of queue → level_size
#         create empty list level_values

#         REPEAT level_size times:
#             remove front node from queue → current
#             add current.value to level_values

#             IF current.left exists:
#                 push current.left into queue

#             IF current.right exists:
#                 push current.right into queue

#         add level_values to result

#     RETURN result

# code
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        d = deque([root])

        level = 0
        result = []
    
        while d: 
            level_size = len(d)
            level =[]

            for i in range(level_size):
                curr_node = d.popleft()
                level.append(curr_node.val)

                if curr_node.left:
                    d.append(curr_node.left)
                if curr_node.right:
                    d.append(curr_node.right)

            result.append(level)
        return result
        #  we use approach of stack in depth first and queue where we have breath first 
    # why we have so many traversal in tree beacuse it is non linear data structure
    # DFS:(depth first search) go to depth first, go in depth in one side(left) come back and go to other side(right)
    # BFS: (breath first search) level order traversal