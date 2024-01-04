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
	listint_t *ptr = *head, *new, *temp;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	/*if (number < ptr->n)*/

	while (ptr != NULL)
	{
		if (number <= ptr->next->n)
		{
			ptr = ptr->next;
		}
		else
			break;
	}

	temp = ptr;
	ptr = ptr->next;
	temp->next = new;
	new->n = number;
	new->next = ptr->next;

	return (new);
}
