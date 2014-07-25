import java.util.Stack;

public class SameTree {
    public boolean isSampeTree(TreeNode p, TreeNode q) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(q);
        stack.push(p);
        while (!stack.empty()) {
            p = stack.pop();
            q = stack.pop();
            if (p == null && q == null) {
                continue;
            }
            if (p == null || q == null) {
                return false;
            }
            if (p.val != q.val) {
                return false;
            }
            stack.push(q.left);
            stack.push(p.left);
            stack.push(q.right);
            stack.push(p.right);
        }
        return true;
    }
}
