#include "lists.h"
/**
 * check_cycle - check lists contains a cycle.
 * 
 * @list: linked list.
 * Return:0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	if (!list)
	{
		return (0);
	}
	for (; slw && fst && fst->next; slw = slw->next, fst = fst->next->next)
	{
	if (slw == fst)
	{
		return (1);
	}
	}

	return (0);
}
