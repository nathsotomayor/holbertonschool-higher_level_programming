#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	current = list;
	check = list;

	if (list == NULL)
		return (0);

	while (current != NULL && check != NULL)
	{
		current = current->next;
		check = check->next->next;
		if (current == check)
			return (1);
	}
	return (0);
}
