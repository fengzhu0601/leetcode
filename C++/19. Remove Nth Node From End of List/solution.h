#include <cstddef>
#include <iostream>
using namespace std;
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL){}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        //　计算链表的长度
        int length = 0;
        ListNode* first = head;
        while(first != NULL)
        {
			length++;
			first = first->next;
        }

        length -= n;
        first = dummy;
        while(length > 0)
        {
            first = first->next;
        }
        first->next = first->next->next;
        return dummy->next;
    }
};
