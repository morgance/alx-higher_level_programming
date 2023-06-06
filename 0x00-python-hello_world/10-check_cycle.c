#include "lists.h"

/**
 * check_cycle - checks if  singly linked list has
 * a cycle 
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *pro, *prim;
	

	pro = list;
	prim = list;
	while (list && pro && pro->next)
	{
		list = list->next;
		pro = pro->next->next;

		if (list == pro)
		{
			list = prim;
			prim =  pro;
			while (1)
			{
				pro = prim;
				while (pro->next != list && pro->next != prim)
				{
					pro = pro->next;
				}
				if (pro->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
