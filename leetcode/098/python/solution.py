# ---------------------------------------------------------------------------------------
#
#  Title:       Validate Binary Search Tree
#
#  Link:        https://leetcode.com/problems/validate-binary-search-tree/
#
#  Difficulty:  Medium
#
#  Language:    Python
#
# ---------------------------------------------------------------------------------------

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ValidateBST(object):
    def __init__(self):
        self.vals = []

    def bsearch(self, node):
        if node != None:
            node.left = self.bsearch(node.left)
            self.vals.append(node.val)
            node.right = self.bsearch(node.right)
        return node
    
    def isValidBST(self, node):
        self.bsearch(node)
        rv = True
        last = 0
        index = 0
        for i in self.vals:
            if index > 0 and i < last:
                rv = False
                break
            last = i
            index = index + 1
        return rv

if __name__ == "__main__":
    # 1(left) <- 2(root) -> 3(right)
    node = TreeNode(2, TreeNode(1), TreeNode(3))
    z = ValidateBST()
    print( z.isValidBST(node) )

    # 3(left) <- 2(root) -> 1(right)
    node = TreeNode(2, TreeNode(3), TreeNode(1))
    z = ValidateBST()
    print( z.isValidBST(node) )
