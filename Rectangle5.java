class rectangle
{
	int length,width;
	rectangle(int l,int w)
	{
		length=l;
		width=w;
	}
	rectangle()
	{
		length=0;
		width=0;
	}
	rectangle(int l)
	{
		length=width=l;
	}
	int area()
	{
		return (length*width);
	}
}

class Rectangle5 // constructor overloading
{
	public static void main(String args[])
	{
		rectangle r1=new rectangle(20,4);
		System.out.println(r1.area());
		rectangle r2=new rectangle();
		System.out.println(r2.area());
		rectangle r3=new rectangle(10);
		System.out.println(r3.area());
	}
}
