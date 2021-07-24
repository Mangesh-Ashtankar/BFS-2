# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val in (x,y): return False # early termination
        
        q = collections.deque()
        q.append(root)
        
        xFound = False
        yFound = False
        
        while q:
            length = len(q)

            while length>0:
                
                ele = q.popleft()
                
                if ele.val == x:
                    xFound = True
                
                if ele.val == y:
                    yFound = True
                
                if ele.left != None and ele.right != None:
                    val1 = ele.left.val
                    val2 = ele.right.val
                    
                    if (x == val1 and y ==val2) or (x == val2 and y ==val1):
                        return False
                    
                if ele.left != None:
                    q.append(ele.left)
                
                if ele.right != None:
                    q.append(ele.right)
                
                length -= 1
                    
            
            
            if xFound and yFound:
                return True
                
            if xFound or yFound:
                return False
            
        return False
