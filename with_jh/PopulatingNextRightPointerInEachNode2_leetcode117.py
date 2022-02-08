from collections import deque
from collections import defaultdict

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        return f"TreeNode{'{'}val: {self.val}, left: {self.left}, right: {self.right}, next: {self.next}{'}'}"

def str_to_tree(string = None, p=None, q=None):

    string = string.strip("'[]' ") # 양쪽에서 [],',공백문자 제거
    string = string.replace(" ", "") # 공백 제거
    string = string.split(",") # , 기준으로 자르기
    
    # 1. 각 노드 만들기
    deq=deque()
    for s in string:
        deq.append(TreeNode(s))

    if len(deq) <= 1:
        # raise ValueError
        return None, None, None

    # 2개일 때는 간단 
    if len(deq) == 2:
        deq[0].left = deq[1]
        if p != None and q!= None:
             if deq[0].val == str(p):
                 p = deq[0]

             if deq[0].val == str(q):
                 q = deq[0]

             if deq[1].val == str(p):
                 p = deq[1]

             if deq[1].val == str(q):
                 q = deq[1]

        return deq[0], p, q

    elif len(deq) >= 3:
        # 2. 깊이 별 분리하기
        # deq 길이가 3이상인 경우만 적용
        tree = {}
        tree_number = {}
        depth = 0

        popleft_number = 2
        while deq: 
            if depth == 0:
                temp = deq.popleft()
                tree[depth] = deque([temp]) # deque 그냥 쓴거임
                tree_number[depth] = deque([temp.val])
            else:
                for _ in range(popleft_number):
                    if depth not in tree:
                        tree[depth] = deque()
                        tree_number[depth] = deque()
                    temp = deq.popleft()
                    tree[depth].append(temp)
                    tree_number[depth].append(temp.val)
                popleft_number=(len(tree_number[depth])-tree_number[depth].count("null"))*2
                # 끝부분 처리
                if len(deq) < popleft_number:
                     popleft_number = len(deq)
            depth+=1

        # 3. 부모 자식 관계 설정
        for i in range(len(tree)-1, 0, -1):
            z = 0
            for node in tree[i-1]:
                if node.val != "null":
                    left_value =tree[i][z]
                    z+=1
                    right_value = tree[i][z]
                    if left_value.val != "null":
                        node.left = left_value
                    if right_value.val != "null":
                        node.right = right_value
                    z+=1

                    # 끝부분 처리
                    if z >= len(tree[i]):
                        break

        if p != None and q!= None:
            for _, value in tree.items():
                for v in value:
                    if v.val == str(p):
                        p = v
                        # continue # p, q가 같을수도!!!
                    if v.val == str(q):
                        q = v
                        # continue # p, q가 같을수도!!!
                        
        return tree[0].pop(), p, q

# 1. 직관적인 방법
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root:
            tree_val = defaultdict(list)
            tree_val[0] =[root]

            def get_depth(root, i=1):
                if root:
                    tree_val[i].append(root)
                    get_depth(root.left, i+1)
                    get_depth(root.right, i+1)

            get_depth(root.left)
            get_depth(root.right)

            for _, v in tree_val.items():
                for c in range(len(v)-1):
                    v[c].next = v[c+1]
        
        return root

# 1. 직관적인 방법
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root:
            tree_val = defaultdict(list)
            tree_val[0] =[root]

            def get_depth(root, i=1):
                if root:
                    tree_val[i].append(root)
                    get_depth(root.left, i+1)
                    get_depth(root.right, i+1)

            get_depth(root.left)
            get_depth(root.right)

            for _, v in tree_val.items():
                for c in range(len(v)-1):
                    v[c].next = v[c+1]
        
        return root

'''
Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
'''
# 2.  implicit stack space does not count as extra space for this problem! using bfs
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root:
            deq = deque([root])
            while deq:
                
                depth=[]

                for _ in range(len(deq)):
                    node=deq.popleft() # 너비 우선 탐색
                    depth.append(node)

                    # 왼쪽부터 차례대로 넣기
                    if node.left:
                        deq.append(node.left)
                    if node.right:
                        deq.append(node.right)

                for i in range(len(depth)-1):
                    depth[i].next = depth[i+1] 

        return root

if __name__ == "__main__":
    root, p, q=str_to_tree(string = "[1,2,3,4,5,null,7]")
    print(Solution().connect(root = root)) # [1,#,2,3,#,4,5,7,#]
    root, p, q=str_to_tree(string = "[]")
    print(Solution().connect(root = root)) # []