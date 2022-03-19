# ---------------------------------------------------------------------------------------
#
#  Title:       Permutations
#
#  Link:        https://leetcode.com/problems/permutations/
#
#  Difficulty:  Medium
#
#  Language:    Python
#
# ---------------------------------------------------------------------------------------

class Permutations:
    def permute(self, nums):
        return self.phelper(nums, [], [])

    def phelper(self, nums, x, y):
        for i in nums:
            if i not in x:
                x.append(i)
                if len(x) == len(nums):
                    y.append(x.copy())
                else:
                    y = self.phelper(nums,x,y)
                del x[len(x)-1]
        return y

if __name__ == "__main__":
  p = [1,2,3]
  z = Permutations()
  print( z.permute(p) )

