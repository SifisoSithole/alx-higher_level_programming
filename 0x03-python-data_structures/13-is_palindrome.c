#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"

/**
 * is_palindrome - Checks if linked list is palindrome
 * @head: head of linked list
 *
 * Return: 1 if palindrome otherwise return 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *h = *head;
	int nodes = 0;
	int i = 0, index, *arr;

	if (!head || !*head)
		return (1);
	while (h)
	{
		nodes++;
		h = h->next;
	}
	arr = malloc(sizeof(int) * nodes);
	h = *head;
	while (h)
	{
		arr[i] = h->n;
		h = h->next;
		i++;
	}
	index = nodes - 1;
	for (i = 0; i <= index; i++)
	{
		if (arr[i] != arr[index])
			return (0);
		index--;
	}
	free(arr);
	return (1);
}
