# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        
        q = collections.deque()
        q.append(root)
        
        while q:
            length = len(q)
            while length>0:
                if length == 1:
                    res.append(q[0].val)
                ele = q.popleft()
                
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                    
                length -= 1
        
        return res
