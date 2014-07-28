class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) { val = x; }
}
public class BalancedBinaryTree {
    public boolean isBalanced(TreeNode root) {
        return checkHeight(root) >= 0;
    }

    private int checkHeight(TreeNode node) {
        if (node == null) return 0;

        int left = checkHeight(node.left);
        int right = checkHeight(node.right);
        if (left < 0 || right < 0 || Math.abs(left - right) < 0) {
            return -1;
        }

        return Math.max(left, right) + 1;
    }
}
