import java.util.*;
class Myinput
{
	public static void main (String args[])
	{
		Scanner console = new Scanner(System.in);
		int roll;
		float marks;
		String name;
		String fullname;
		System.out.println("\n enter your fullname\n");
		fullname=console.nextLine();
		System.out.println("\n enter your roll number\n");
		roll=console.nextInt();
		System.out.println("\n enter your marks\n");
		marks=console.nextFloat();
		System.out.println("\n enter your name\n");
		name=console.next();
		System.out.println("\n fullname="+fullname);
		System.out.println("\nroll number="+roll);
		System.out.println("\n marks="+marks);
		System.out.println("\n name="+name);
	}
}
