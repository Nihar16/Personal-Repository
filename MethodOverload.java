class overload
{
	int volume(int x)
	{
		return (x*x*x);
	}

	double volume(double r,double h)
	{
		return (3.14*r*r*h);
	}
	
	long volume( long l, int b, int h)
	{
		return (l*b*h);
	}
}
class MethodOverload // method overloading
{
	public static void main ( String args[])
	{
		overload v= new overload();
		System.out.println("Volume of cube ="+v.volume(10));
		System.out.println("Volume of cylinder ="+v.volume(3.5,6.7));
		System.out.println("Volume of rectangle ="+v.volume(48l,25,3));
	}
}
