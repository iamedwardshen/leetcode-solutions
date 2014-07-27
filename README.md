Personal solutions of [LeetCode online judge](http://oj.leetcode.com/problems/)
--------------------------------------------

### 0. Tips
0.1 [Java Performance Tunning Tips](https://gist.github.com/rioshen/42294b25c09b89fa353f)

### 1. Arrays
1.1 [Remove Duplicates from Sorted Array](https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/)

Constraints:
+ the input array must be sorted
+ return 0 if the array is null or the length is 0

Ideas:
+ The occurrence times (2 in this problem) is the starting point.
+ Iterate through the array, compare the current element with the previous one.
+ If they are not equal, cover previous element by the current then update the index.
+ Time Complexity is *O(N)* as the worst case is no duplicates in the array.
+ Space Complexity is *O(1)*, no additional space is required.

[Code](https://github.com/rioshen/leetcode-solutions/blob/master/java/RemoveDuplicatesFromSortedArray.java)

1.2 []
