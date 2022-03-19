/**
 * ---------------------------------------------------------------------------------------
 *
 * Title:       Median of Two Sorted Arrays
 *
 * Link:        https://leetcode.com/problems/median-of-two-sorted-arrays/
 *
 * Difficulty:  Hard
 *
 * Language:    Java
 *
 * ---------------------------------------------------------------------------------------
 */

class Solution {

    public static void main(String[] args) {
        (new Solution()).go();
    }

    public void go() {
        int[] nums1 = new int[] { 1,4,7,8,10,14 };
        int[] nums2 = new int[] { 3,6,8,55 };
        System.out.println(findMedianSortedArrays(nums1,nums2));
    }

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] x = new int[nums1.length+nums2.length];
        int i=0, j=0, k=0;

        while(true) {
            boolean done = false;
            if( i < nums1.length && ( j >= nums2.length || nums1[i] <= nums2[j] ) ) {
                x[k] = nums1[i];
                i++;
                k++;
                done = true;
            }

            if ( !done && j < nums2.length && ( i >= nums1.length || nums2[j] <= nums1[i] ) ) {
                x[k] = nums2[j];
                j++;
                k++;
                done = true;
            }
            if( !done )
                break;
        }

        double rv;
        i = x.length / 2;

        if( x.length % 2 == 0 )
            rv = (double)( x[i] + x[i-1] ) / 2.0;
        else
            rv = (double) x[i];

        return rv;
    }

}
