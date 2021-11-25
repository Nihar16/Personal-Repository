#include <stdio.h>
#define size 5
int array[size];
int top;
void main()
{
	int x=0,y=0,xx,yy,i;
	top=0;
	printf("pushing the element.")
	for(i=0;i<5;i++)	
	{
		// Checking the stack is full or not
		
		if(top<size)
		{
			x=1;
		}
		else
		{
			x=-1;
		}
		
		//pushing the element if stack is not full
		
		if(x==1)
		{
			printf("\nenter the element\n");
			scanf("%d",&array[top]);
			top++;
		}

	}	
	//Displaying matrix
	if(top>4)
	{
		top=4;
	}
	printf("\n Display stack\n");
	for(i=0;i<=top;i++)
	{
		printf("%d",array[i]);
	}
	printf("\npop elements:-\n");
	for(i=0;i<5;i++)
	{
		//checking whether stack is empty or not
	
		if(top>-1)
		{
			y=1;//not empty
		}
		else
		{
			y=-1;
		}
	
		//popping the element 
		
		if (y==1)
		{
			printf("%d ",array[top]);
			top--;
		}
	}
}

