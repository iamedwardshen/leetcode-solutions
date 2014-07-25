public class ReverseLinkedListII {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null) return null;

        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode prev = dummy;

        for (int i = 0; i < m - 1; i++) {
            prev = prev.next;
        }
        ListNode newHead = prev;

        prev = newHead.next;
        ListNode current = prev.next;
        for (int i = 0; i < n - m; i++) {
            prev.next = current.next;
            current.next = newHead.next;
            newHead.next = current;
            current = prev.next;
        }

        return dummy.next;
    }
}
