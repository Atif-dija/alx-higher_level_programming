#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list
 *
 * @head: head of linked list
 * @number: number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *l = *head, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!l || new->n < l->n)
	{
		new->next = l;
		return (*head = new);
	}
	while (l)
	{
		if (!l->next || next->n < l->next->n)
		{
			new->next = l->next;
			l->next = new;
			return (l);
		}
		l = l->next;
	}
	return (NULL);
}

