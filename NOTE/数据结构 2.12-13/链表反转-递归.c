ListNode* reversList(ListNode* head) {
	if (head == NULL || head->next = NULL) return head;
	ListNode* tail = head->next;
	ListNode* new_head = reversList(head->next);
	head->next = tail->next;
	tail->next = head;
	return new_head;
}
//���߽���������Ȼ��������������������������� 
