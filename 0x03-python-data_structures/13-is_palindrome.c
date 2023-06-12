#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *palin = *head;
	int counter = 0;
	int x = 0, y = 0;

	if (!*head)
		return (1);

	while (current != NULL)
	{
		current = current->next;
		counter++;
	}
	current = *head;
	x = 1;
	while (x <= counter)
	{
		for (y = x; y <= counter - x; y++)
			palin = palin->next;
		if (current->n != palin->n)
			return (0);
		current = current->next;
		palin = current;
		x++;
	}
	return (1);
}
