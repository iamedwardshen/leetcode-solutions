import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) { val = x; }
}

public class SymmetricTree {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;

        Stack<TreeNode> stack = new Stack<>();
        stack.push(root.right);
        stack.push(root.left);
        while (!stack.emtpy()) {
            TreeNode left = stack.pop();
            TreeNode right = stack.pop();

            if (left == null && right == null) continue;
            if (left == null || right == null) return false;
            if (left.val != right.val) return false;

            stack.push(right.right);
            stack.push(left.left);
            stack.push(right.left);
            stack.push(left.right);
        }

        return true;
    }
}
