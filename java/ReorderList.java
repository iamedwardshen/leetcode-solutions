/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
    
    private ListNode findMiddle(ListNode head) {
        ListNode fast = head.next;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
    
    private void merge(ListNode l1, ListNode l2) {
        ListNode current = new ListNode(-1);
        int index = 0;
        while (l1 != null && l2 != null) {
            if (index % 2 == 0) {
                current.next = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                l2 = l2.next;
            }
            current = current.next;
            index++;
        }
        if (l1 != null) current.next = l1;
        else if (l2 != null) current.next = l2;

    }

    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        ListNode mid = findMiddle(head);
        ListNode tail = reverse(mid.next);
        mid.next = null;
        
        merge(head, tail);
    }
}
