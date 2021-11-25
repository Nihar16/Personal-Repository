#include<stdio.h>

int main()
{
	int data[100],i,n,steps,temp;
	printf("Enter no. of elements to be sorted \n \t");
	scanf("%d \t",&n);
	
	for(i=0;i<n;i++)
	{
		printf("%d enter element \t",i+1);
		scanf("%d \t",&data[i]);
	}

	for(steps=0;steps<n;++steps)
	{
		for(i=steps+1;i<n;++i)
		{
			if(data[steps]>data[i])
			{ 
				temp=data[steps];
				data[steps]=data[i];
				data[i]=temp;
			}
		}
	}
	printf("In ascending order:\n \t");	
	{
		for(i=0;i<n;++i)
		{	
			printf("%d \n \t",data[i]);
		}
	return 0;
	}
}
