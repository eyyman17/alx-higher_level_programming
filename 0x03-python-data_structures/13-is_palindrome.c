#include "lists.h"

/**
 * add_nodeint - adds new node at the beginning
 *
 * @head: pointer to pointer to head of the list
 * @n: const integer
 *
 * Return: the address of the new element, or NULL if failed
 **/

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 **/

int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head, *head2;

	while (ptr != NULL)
	{
		add_nodeint(&head2, ptr->n);
		ptr = ptr->next;
	}

	while (ptr != NULL && head2 != NULL)
	{
		if (ptr->n != head2->n)
			return (0);
	}

	free_listint(head2)

	return (1);
}
