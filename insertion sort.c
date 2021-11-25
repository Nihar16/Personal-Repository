#include<stdio.h>

int main()
{
	int data[100],i,j,n,temp;
	printf("Enter no. of terms \n");
	scanf("%d",&n);
	
	printf("Enter elements \n");
	for(i=0;i<n;i++)
	{
		
		scanf("%d",&data[i]);
	}

	for(i=1;i<n;i++)
	{
		temp= data[i];
		j=i-1;
		
		while(temp<data[j] && j>=0)
		{
			data[j+1]=data[j];
			--j;
		}
		data[j+1]=temp;
	}
	printf("In ascending order:");	
	{
		for(i=0;i<n;++i)
		{	
			printf("%d",data[i]);
		}
	return 0;
	}
}
