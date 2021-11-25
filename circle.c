#include<stdio.h>
#include<conio.h>
#include<graphics.h>
void plot(int xc, int yc, int x, int y)
{
	putpixel((xc+x)+320,240-(yc+y),WHITE);
	putpixel(xc-x)+320,240-(yc+y,WHITE);
	putpixel(xc+x)+320,240-(yc-y,WHITE);
	putpixel(xc-x)+320,240-(,yc-y,WHITE);
	putpixel(xc+y)+320,240-(,yc+x,WHITE);
	putpixel(xc-y)+320,240-(,yc+x,WHITE);
	putpixel(xc+y)+320,240-(,yc-x,WHITE);
	putpixel(xc-y)+320,240-(,yc-x,WHITE);
}
void midpt(int xc,int yc, int r)
{
	int x,y,p;
	x=0;
	y=r;
	p=1-r;
	plot(xc,yc,x,y);
	while(x<y)
	{
		x++;
		if(p<0)
		{
			p=p+(2*x)+1;
		}
		else
		{
			y--;
			p=p+(2*(x-y))+1;
		}
		plot(xc,yc,x,y);
	}
}
void main()
{
	int gd=DETECT,gm,i,r,xc,yc;
	initgraph(&gd,&gm,"\\BGI");
	line(320,0,320,480);
	line(0,240,640,240);
	printf("Enter co-ordinates of center of circle:\n");
	scanf("%d%d",&xc,&yc);
	printf("Enterradius of circle:\n");
	scanf("%d",&r);
	midpt(xc,yc,r);
	getch();
}
