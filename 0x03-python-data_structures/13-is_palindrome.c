#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *mid, *second_half;
	int palindrome = 1;

	slow = *head;
	fast = *head;
	mid = NULL;

	while (fast != NULL && fast->next != NULL)
			{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
			}

	if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }

    second_half = slow;
    prev_slow->next = NULL;
    reverse_list(&second_half);

    palindrome = compare_lists(*head, second_half);

    reverse_list(&second_half);

    if (mid != NULL)
    {
        prev_slow->next = mid;
        mid->next = second_half;
    }
    else
	{
		prev_slow->next = second_half;
	}

	return palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev, *current, *next;

	prev = NULL;
	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 * Return: 1 if lists are equal, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->n != head2->n)
		return 0;

		head1 = head1->next;
		head2 = head2->next;
	}

	return (head1 == NULL && head2 == NULL);
}
