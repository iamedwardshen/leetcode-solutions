/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class ConvertSortedArraytoBinarySearchTree {
    public TreeNode sortedArrayToBST(int[] num) {
        if (num == null) {
            return null;
        }

        return sorted(num, 0, num.length - 1);
    }

    private TreeNode sorted(int[] num, int low, int high) {
        if (low > high) {
            return null;
        }

        int mid = low + (high - low) / 2;
        TreeNode node = new TreeNode(num[mid]);
        node.left = sorted(num, low, mid - 1);
        node.right = sorted(num, mid + 1, high);

        return node;
    }

}
