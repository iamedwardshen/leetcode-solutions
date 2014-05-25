class ListNode {
    int val;
    ListNode next;

    public ListNode(int x) {
        val = x;
        next = null;
    }
}

public class RemoveDuplicatedSortedList {
    /**
     * Solution: Iterates down the linked list and
     * compare the current node with next node
     * Time Complexity: O(N), where N means the elements in the list.
     * Space Complexity: O(1), no additional space is required.
     */
    public static ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode current = head;
        while (current.next != null) {
            if (current.val == current.next.val) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }

        return head;
    }
}