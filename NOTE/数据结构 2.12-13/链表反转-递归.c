ListNode* reversList(ListNode* head) {
	if (head == NULL || head->next = NULL) return head;
	ListNode* tail = head->next;
	ListNode* new_head = reversList(head->next);
	head->next = tail->next;
	tail->next = head;
	return new_head;
}
//或者建立新链表，然后遍历旧链表依次输入新链表即可 
