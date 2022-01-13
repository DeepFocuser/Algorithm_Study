from strtotree import str_to_tree, TreeNode
from collections import deque

# 1. 정말 오래 걸렸다.... 12시간 트리를 잘 몰랐다. 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        tree = {root:None} # key : 현재노드 / value : 부모 
        
        def assignment(root : 'TreeNode'):
            
            if root.left != None:
                tree[root.left] = root
                assignment(root.left)
            
            if root.right != None:
                tree[root.right] = root
                assignment(root.right)
            
             
        # 전략 : key가 노드, value 가 부모인 사전을 정의한다. - 이러면 p,q에서 root까지 경로 구할 수 있을 것 같다.   
        assignment(root)
        
        # 1. p값에서 root까지 경로를 뽑아낸다
        p_path = []
        while p != None: 
            p_path.append(p)
            p=tree[p]
        
        # 2. q값에서 root까지 경로를 뽑아낸다.
        q_path = []
        while q != None:  
            q_path.append(q)
            q=tree[q]
        
        # 3. 부모 찾기
        lca = [] 
        while p_path:
            p = p_path.pop()
            q = q_path.pop()   
            if p == q:
                lca.append(p)
                
            if not p_path or not q_path:
                break
        
        return lca.pop()

# # 2. 이렇게 말고 재귀형을 이용해서 풀어보자
class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        deq = deque()
        path = deque()

        def find_path(root: TreeNode, target: TreeNode):
            
            if root == None:
                return
            
            deq.append(root)
            if root == target:
                path.append(deq.copy()) # deq.copy() 하는 이유는? 안하면 아래에서 deq.pop()할때 같이 없어짐. mutable 자료형이라.

            find_path(root.left, target)
            find_path(root.right, target)
            deq.pop()

        # 1. root에서 p까지의 경로 찾기
        find_path(root, p)
        p_path = path.pop()
        # 2. root에서 q까지의 경로 찾기
        find_path(root, q)
        q_path = path.pop()

        # 3. 부모 찾기
        lca = [] 
        while p_path:
            p = p_path.popleft()
            q = q_path.popleft()
            if p == q:
                lca.append(p)
                
            if not p_path or not q_path:
                break
        
        return lca.pop()

if __name__ == "__main__":

    # 입력 형태가 TreeNode 구성이 되어야 하며, 아래의 입력으로는 실행 안된다. - leetcode 플랫폼에서 하길
    root, p, q=str_to_tree(string = "[3,5,1,6,2,0,8,null,null,7,4]", p=5, q=4)
    #root, p, q=str_to_tree(string = "[37,-34,-48,null,-100,-101,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]", p=-100, q=8)
    print(Solution().lowestCommonAncestor(root = root, p=p, q=q))