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
	int begin = 0;
	int len = 0;
	int end = 0;
	size_t size = sizeof(char *) * 10;
	listint_t **address = NULL;
	listint_t **tempAddr = NULL;

	address = malloc(size);
	address[end] = list;
	list = list->next;
	while (list)
	{
		begin = 0;
		end = len;
		while (begin <= end)
		{
			if (address[begin] == list || address[end] == list)
			{
				free(address);
				return (1);
			}
			begin++;
			end--;
		}
		if (sizeof(char *) * len > size)
		{
			tempAddr = malloc(size * 2);
			size *= 2;
			for (begin = 0; begin < len; begin++)
				tempAddr[begin] = address[begin];
			free(address);
			address = tempAddr;
		}
		len++;
		address[len] = list;
		list = list->next;
	}
	free(address);
	return (0);
}
