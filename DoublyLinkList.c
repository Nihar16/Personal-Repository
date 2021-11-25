#include<stdio.h>

#include<stdlib.h>

typedef struct dnode
	{
		int data;
		struct dnode *next,*prev;
	};
dnode *create();
void print_forward(dnode*);
void print_reverse(dnode*);

void main()
{
	dnode*head;
	head=NULL;//initially node is empty
	head=create();
	printf("\n enter elements in forward direction :\n");
	print_forward(head);
	printf("\n enter elements in reverse direction :\n");
	print_reverse(head);
}

dnode *create()
{
	dnode *h,*p,*q;
	int i,n,x;
	printf("\n enter no. of elements \n");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		printf("\n enter next data \n");
		scanf("%d",&x);
		q=(dnode*)malloc(sizeof(dnode));
		q->data=x;
		q->prev=q->next=NULL;
		if(h==NULL)
			p=h=q;
		else
			p->next=q;
			q->prev=p;
			p=q;
	}
	return(h);
}

void print_forward(dnode*h);
{
	while(h!=NULL)
	{
		printf("<-%d->",h->data);
		h=h->next;
	}
}

void print_reverse(dnode*h);
{
	while(h->next!=NULL)
		h=h->next;	
			while(h!=NULL)
			{
				printf("<-%d->",h->data);
				h=h->prev;
			}
}
