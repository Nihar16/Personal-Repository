#include<stdio.h>
#include<stdlib.h>
#define size 5

int front=0,rear=0,i,j;
int q[size];

int qisfull()
{
	if(rear==size)
	{
		return 1;
	}
	else 
		return 0;
}

int qisempty()
{
	if(rear==0)
		return 1;
	else
		return 0; 
}

void enque()
{
	if(!qisfull())
	{
		int n;
		printf("\nEnter Data: ");
		scanf("%d",&n);
		q[rear] = n;
		rear+=1;
	}
	else
	{
		printf("\nSorry..Queue is Full!");
	}
}  

void deque()
{
	if(!qisempty())
	{
		printf("\nElement DeQueued Successfully!");
		for(i=0;i<rear;i++)
		{
			q[i]=q[i+1];
		}
		rear-=1;
	}
	else
	{
		printf("\nQueue is Empty!");		
	}
}

void display()
{
	printf("\nQueue Status: ");
	for(i=0;i<rear;i++)
	{
		printf("%d ",q[i]);
	}
}

void peak()
{
	printf("\nPeak Element: %d",q[front]);
}

void search()
{
        int target,flag=0;
        printf("\nEnter Target Element: ");
        scanf("%d",&target);
        for(i=0;i<rear;i++)
        {
                if(q[i]==target)
                {
                        flag=1;
                        break;
                }
        }
        if(flag==1)
        {
                printf("\nElement Found!\nPosition = %d",i+1);
        }
        else
        {
                printf("\nElement Not Found..!!");
        }
}

void update()
{
        int pos,data;
        printf("\nEnter Position: ");
        scanf("%d",&pos);
        if(pos>rear)
        {
                printf("\nEnter A Valid Position!");
        }
        else
        {
                printf("\nEnter New Data: ");
                scanf("%d",&data);
                q[pos-1]=data;
                printf("\nUpdation Completed!");
        }
}

void sort()
{
        //My Sorting Technique
	int temp;
	for(i=rear-1;i>0;i--)
	{
		for(j=0;j<i;j++)
		{
			if(q[i]<q[j])
			{
				temp = q[i];
				q[i] = q[j];
				q[j] = temp;
			}
		}
	}//Sorting Completed     
	printf("\nSorting Completed!");           
}

int main()
{
	int choice;
	do
	{
		printf("\n----------------------------");
		printf("\n1. Enque\n2. Deque\n3. Display Queue\n4. Show Peak\n5. Search");
		printf("\n6. Update\n7. Sort\n8. Exit");
		printf("\n----------------------------");
		printf("\nEnter Your Choice: ");		
		scanf("%d",&choice);
		switch(choice)
		{
			case 1 : enque();break;
			case 2 : deque();break;
			case 3 : display();break;
			case 4 : peak();break;
			case 5 : search();break;
			case 6 : update();break;
			case 7 : sort();break;
			case 8 : printf("\nExiting...\n");break;
			default: printf("\nPlease Enter A Valid Choice!");

		}
	
	}while(choice!=8);
	return 0;	
}


