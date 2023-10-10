#include "lists.h"

/**
 *is_palindrome -  checks if a singly linked list is a palindrome
 *
 *@head: linked list
 *
 *Return: check_palind or 1
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_palind(head, *head));
}

/**
 *check_palind - checks a palindrome
 *
 *@head: head of linked list
 *@end: end of linked list
 *
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int check_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (check_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
