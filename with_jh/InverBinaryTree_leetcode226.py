from strtotree import str_to_tree, TreeNode
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(root)

if __name__ == "__main__":
    print(Solution().invertTree(root = str_to_tree("[4,2,7,1,3,6,9]"))) # [4,7,2,9,6,3,1]
    #print(Solution().invertTree(root = str_to_tree("[2,1,3]"))) # [2,3,1]
    #print(Solution().invertTree(root = str_to_tree("[]"))) # [2,3,1]