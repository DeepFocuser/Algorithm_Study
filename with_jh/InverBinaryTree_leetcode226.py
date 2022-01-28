from strtotree import str_to_tree, TreeNode
from typing import Optional
from collections import deque

# # 1. 재귀 방법1
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
#         def invert(root) -> Optional[TreeNode]:
            
#             if root == None:
#                 return
            
#             root.left, root.right = root.right, root.left
            
#             invert(root.left)
#             invert(root.right)
        
#         invert(root)

#         return root

# # 2. 재귀 방법2
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
#         if root:
#             root.left, root.right = root.right, root.left
#             self.invertTree(root.left)
#             self.invertTree(root.right)
        
#         return root

# 3. for문 사용 - bfs, dfs 로 풀어보기
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        tree=deque([root])
        
        while tree:

            #node=tree.pop() # bfs
            node=tree.popleft() # dfs
            if node:
                node.left, node.right = node.right, node.left

                tree.append(node.left)
                tree.append(node.right)

        return root

if __name__ == "__main__":
    root, p, q=str_to_tree(string = "[4,2,7,1,3,6,9]")
    print(Solution().invertTree(root = root)) # [4,7,2,9,6,3,1]
    root, p, q=str_to_tree(string = "[2,1,3]")
    print(Solution().invertTree(root = root)) # [2,3,1]
    root, p, q=str_to_tree(string = "[]")
    print(Solution().invertTree(root = root)) # None