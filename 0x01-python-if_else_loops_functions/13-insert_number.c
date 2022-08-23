#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - This function inserts a node in a sorted linked list
 * @head: pointer to the node
 * @number: number to add
 *
 * Return: Pointer to the node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h, *new;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	h = *head;
	while (h->next && (*(h->next)).n < number)
		h = h->next;
	if (h == *head)
	{
		new->next = h;
		*head = new;
	}
	else
	{
		new->next = h->next;
		h->next = new;
	}
	return (new);
}
