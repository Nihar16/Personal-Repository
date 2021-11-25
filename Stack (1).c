#include <stdio.h>
#define size 5
void niharPush();
void niharPop();
void niharPopAll();
int niharIsFull();
int niharIsEmpty();
void niharDisplay();
int array[size];
int top,x=0,y=0,i;
void main()
{
	int choice,exit=0;
	top=-1;
	do
	{
		printf("\nEnter Your Choice\n");
		printf("\n1 FOR PUSH\n");
		printf("\n2 FOR POP\n");
		printf("\n3 FOR DISPLAY THE STACK\n");
		printf("\n4 TO POP OUT ALL ELEMENTS\n");
		printf("\n5 TO EXIT\n");
		printf("\n Choice:- ");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
				niharPush();
				break;
			case 2:
				niharPop();
				break;
			case 3:
				niharDisplay();
				break;
			case 4:
			    niharPopAll();
			    break;
			case 5:
				printf("\nExiting...\n");
				exit=1;
				break;
		
		    default: 
		        printf("Invalid choice. Please enter Valid Choice");
		        break;
		    
		}
	}while(exit!=1);
}
	
	int niharIsFull()
	{
		// Checking the stack is full or not
		
		if(top<size-1)
		{
			x=1;
		}
		else
		{
			x=-1;
		}
		return x;
	}	
	void niharPush()
	{
		//pushing the element if stack is not full
		int xx= niharIsFull();
		if(xx==1)
		{
			++top;
			printf("\nPushing the element...\n");
			printf("\nEnter the element\n");
			scanf("%d",&array[top]);

		}
        else
            printf("\nStack is full.\n");
	}	
	void niharDisplay()
	{
		//Displaying matrix
		printf("\n Display stack\n");
		for(i=0;i<=top;i++)
		{
			printf("%d ",array[i]);
		}
        if (top<0)
        printf("\nStack Is Empty\n");
	}	
	
	int niharIsEmpty()
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
		return y;
	}
	void niharPop()
	{	
		//popping the element 
		printf("\nPopping....\n");
		printf("\nPopped element:- ");
		int yy = niharIsEmpty();
		if (yy==1)
		{
			printf("%d ",array[top]);
			top--;
		}
	
	    else
	        printf("\nStack Is Empty\n");
	}
	void niharPopAll()
	{
	    // Popping all elements.
	    printf("\nPopping All Elements ....\n");   
	    printf("\nAll Popped Elements :-\n");
	    for(i=top;i>=0;i--)
	    {
	       printf("%d ",array[top]); 
	       top--;
	    }
	    printf("\nNow Stack Is Empty\n");
	}
