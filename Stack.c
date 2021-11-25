#include<stdio.h>
#define size 5
int arr[size];
int top=0;
void stackPush();
void stackPop();
int stackIsEmpty();
int stackIsFull();
void stackDisplay();

//Pushing Element In Stack
void stackPush()
{
	int check = stackIsFull();
	if(check == 1)
	{
		printf("\nEnter Element: ");
		scanf("%d",&arr[top]);
		top++;
	}
}

//Pop Element From Stack
void stackPop()
{
	int check = stackIsEmpty();
	if(check == 1)
	{	
		top--;
		printf("\nPop Element %d",arr[top]);
		
	}
}

//Check If Stack Is Empty
int stackIsEmpty()
{
	int i=0;
	if(top>-1)
	{
		i=1; //not empty		
	}
	return i;
}

//Display Stack
void stackDisplay()
{
	int i;
	printf("\nCurrent Status Of Stack: ");
	for(i=0;i<top;i++)
	{
		printf("%d ",arr[i]);
	}
	printf("\n");
}

//Check If Stack Is Full
int stackIsFull()
{
	int i=0;
	if(top<=size-1)
	{
		i=1; //not full
	}
	return i;
}

void main()
{
	int choice;
	do
	{
		printf("\n1.Push\n2.Pop\n3.Display Stack\n4.Exit\n");
		printf("\nEnter Your Choice: \n");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1 :stackPush();break;
			case 2 :stackPop();break;
			case 3 :stackDisplay();break;
			case 4 :printf("\nExiting Stack...!!\n");break;
			default:printf("\nEnter Valid Choice!");
		}//closing switch
	}while(choice!=4);
	
}
