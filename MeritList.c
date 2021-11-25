#include <stdio.h>
void main()
{
	int temp,i,j,marks[100],n,n1,n2,smarks[100];
	int count1=0,count2=0;
	printf("\nenter the no. of students whos marks are to be entered in merit list 1.\n");
	scanf("%d",&n1);
	printf("\nenter the marks roll no. wise. \n");
	for(i=0;i<n1;i++)
	{
		scanf("%d",&marks[i]);
	}
	printf("\nmerit list 1:-\n");
	for(i=0;i<n1;i++)
	{
		printf("\n%d \n",marks[i]);
	}
	for(i=0;i<n1;i++)
	{
		smarks[i]=marks[i];
	}	
	//sorting array in the descending order
	for (i=0;i<n1;i++)
	{
		for(j=i+1;j<n1;j++)
		{
			if(smarks[i]<smarks[j])
			{
				temp=smarks[i];
				smarks[i]=smarks[j];
				smarks[j]=temp;
			}			
		}
	}
	printf("\nmarks in Descending order\n");
	for(i=0;i<n1;i++)
	{
		printf("\n%d \n",smarks[i]);
	}
	printf("\nHighest marks are %d.\n",smarks[0]);
	printf("\nLowest marks are %d.\n",smarks[n1-1]);
	// For Highest and Lowest Marks scorers' roll no.
	for (i=0;i<n1;i++)
	{
		if(smarks[0]==marks[i])
			printf("\nRoll no. %d has scored highest marks %d.\n",i+1,smarks[0]);
		if(smarks[n1-1]==marks[i])
			printf("\nRoll no. %d has scored lowest marks %d.\n",i+1,smarks[n1-1]);
		//For counting firstclass & secondclass students		
		if(smarks[i]>=65)
			count1++;
		if(smarks[i]<65 && smarks[i]>=45)
			count2++;
	}
	printf("\nNo. of students who passed with first class is %d\n",count1);
	printf("\nNo. of students who passed with second class is %d\n",count2);
	printf("\nEnter te no of students whose data u want to enter in second merit list 2\n");
	scanf("%d",&n2);	
	n=n1+n2;	
	int marks2[100],meritlist[100],smeritlist[100];
	printf("\nenter the marks roll no. wise. \n");	
	for(i=0;i<n2;i++)
	{
		scanf("%d",&marks2[i]);
	}
	printf("\nmerit list 2:-\n");
	for(i=0;i<n2;i++)
	{
		printf("\n%d \n",marks2[i]);
	}	
	printf("\nCombined merit list Roll no. wise :-\n");
	//Merging two merit lists	
	int k=0;
	for(i=0;i<n1;i++)
	{
		meritlist[k]=marks[i];
		k++;
	}
	for(i=0;i<n2;i++)
	{
		meritlist[k]=marks2[i];
		k++;
	}
	for(i=0;i<n;i++)
	{
		smeritlist[i]=meritlist[i];
		printf("\n%d \n",meritlist[i]);
	}
	printf("\nsorting combined merit list\n");	
	// sorting combined merit list	
	for(i=0;i<n;i++)
	{	
		for(j=i+1;j<n;j++)
		{
			if(meritlist[i]<meritlist[j])
			{
				temp=smeritlist[i];
				smeritlist[i]=smeritlist[j];
				smeritlist[j]=temp;
			}			
		}
		
	}
	printf("\nsorted combined merit list:-\n");
	for(i=0;i<n;i++)
	{
		printf("\n%d \n",smeritlist[i]);
	}
	// To search the roll no. of the given marks.
	int found,search;
	printf("\nEnter the Marks to get the roll no.s of the students who scored entered marks\n");
	scanf("%d",&search);
	printf("\nThe roll no.s who scored %d marks\n",search);
	for(i=0;i<n;i++)
	{
		if(meritlist[i]==search)
		{
			found=1;
			printf("%d ",i+1);		
		}
	}
	if(found==0)
	printf("not found\n");
	// To update the marks of the entered roll no.	
	int roll,nmarks,choice;
	printf("\nDo you want to edit marks? enter 1 for yes or 0 for no.\n");
	scanf("%d",&choice);
	if (choice==1)
	{
		printf("\nEnter the roll no. for which you want to edit marks\n");
		scanf("%d",&roll);
		printf("\nEnter new marks\n");
		printf("\nIf you want to delete marks for entered roll no.,then please add negative value.\n");
		scanf("%d",&nmarks);
		meritlist[roll-1]=nmarks;
	}
	printf("Final updated combined merit list:-");
	for(i=0;i<n;i++)
	{
		if(meritlist[i]>=0)
		{
			printf("\n%d \n",meritlist[i]);
		}
	}
}	
