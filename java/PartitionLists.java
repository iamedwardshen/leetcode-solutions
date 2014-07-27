public class PartitionLists {
    public ListNode partition(ListNode head, int x) {
        if (head == null) return null;

        ListNode lowDummy = new ListNode(-1);
        ListNode low = lowDummy;
        ListNode highDummy = new ListNode(-1);
        ListNode high = highDummy;

        ListNode current = head;
        while (current != null) {
            if (current.val < x) {
                low.next = current;
                low = current;
            } else {
                high.next = current;
                high = current;
            }
            current = current.next;
        }
        low.next = highDummy;
        high.next = null;

        return lowDummy.next;
    }
}
