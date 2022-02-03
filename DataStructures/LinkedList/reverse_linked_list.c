/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};


struct ListNode* reverseList(struct ListNode* head){
    
    struct ListNode *temp = head;
    struct ListNode *prev = NULL;
    struct ListNode *next;
    
    while (temp != NULL){
        next = temp->next;
        temp->next = prev;
        prev = temp;
        temp = next;
        
    }
    return prev;

}
