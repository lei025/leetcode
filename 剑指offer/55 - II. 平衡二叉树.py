# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        # 先序遍历 + 判断深度 （从顶至底） 时间复杂度高
        def depth(self, root):
            if not root: return 0
            return max(self.depth(root.left), self.depth(root.right)) + 1

        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)

        # 后序遍历 + 剪枝 （从底至顶）
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:
                return -1
            right = recur(root.right)
            if right == -1:
                return -1
            if abs(left - right) <= 1:
                return max(left, right) + 1
            else:
                return -1

        return recur(root) != -1
