class Rational
{
	int numerator,denominator;
	Rational(int n,int d)
	{
		numerator=n;
		denominator=d;
	}
	Rational()
	{
		numerator=0;
		denominator=0;
	}
	Rational sum(Rational n2)
	{
		Rational r=new Rational();
		int temp=0;
		temp+=numerator*n2.denominator;
		temp+=n2.numerator*denominator;
		r.numerator=temp;
		r.denominator=denominator*n2.denominator;		
		return r;
	}
	void display()
	{
		System.out.println(numerator+"/"+denominator);
	}
}
class RationalDemo2
{
	public static void main(String args[])
	{
		Rational r1=new Rational(7,5);
		Rational r2=new Rational(3,5);
		Rational r3=new Rational();
		r3=r1.sum(r2);
		r1.display();
		System.out.println("+");
		r2.display();
		System.out.println("=");
		r3.display();
	}
}

