# ---------------------------------------------------------------------------------------
#
#  Title:       Median of Two Sorted Arrays
#
#  Link:        https://leetcode.com/problems/median-of-two-sorted-arrays/
#
#  Difficulty:  Hard
#
#  Language:    Python
#
# ---------------------------------------------------------------------------------------

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        x = []
        while(True):
            done = False
            if i < len(nums1) and ( j >= len(nums2) or nums1[i] <= nums2[j] ):
                x.append(nums1[i])
                i += 1
                done = True
            if not done and j < len(nums2) and ( i >= len(nums1) or nums2[j] <= nums1[i] ):
                x.append(nums2[j])
                j += 1
                done = True
            if not done:
                break

        lenx = len(x)
        midx = lenx >> 1
        rv = 0.0
        if lenx % 2 == 0:
            rv = (x[midx] + x[midx-1]) / 2.0
        else:
            rv = x[midx]
        return rv

if __name__ == "__main__":
    z = Solution()
    print(z.findMedianSortedArrays([1,8],[3,4,7,9]))
