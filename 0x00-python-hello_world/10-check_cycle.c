#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - This function checks if singly linked list has a cycle in it
 * @list: Pointer to the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	int i = 0;

	listint_t *h = list;

	if (!list)
		return (0);
	while (list)
	{
		if (list == h)
			return (1);
		for (i = 0; i < 3; i++)
		{
			if (h-next == NULL)
				return(0);
			h->next;
		}
		list = list->next;
	}
	free(address);
	return (0);
}
