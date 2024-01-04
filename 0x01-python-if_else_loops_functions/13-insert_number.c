#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: head of the linked list
 * @number: number
 *
 * Return: the address of the new node, or NULL if it failed
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (ptr == NULL)
	{
		*head = new;
		return (new);
	}
	
	else if (number <= ptr->n)
	{
		new->next = ptr;
		ptr = new;
		return (new);
	}
	else
	{
		while (ptr->next != NULL)
		{
			if (number <= ptr->next->n)
			{
				new->next = ptr->next;
				ptr->next = new;
				return (new);
			}
			ptr = ptr->next;
		}
		new->next = NULL;
		ptr->next = new;
		return (new);
	}
	return (NULL);
}
