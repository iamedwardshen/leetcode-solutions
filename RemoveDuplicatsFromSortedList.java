class ListNode {
    int val;
    ListNode next;

    public ListNode(int x) {
        val = x;
        next = null;
    }
}

public class RemoveDuplicatedSortedList {
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