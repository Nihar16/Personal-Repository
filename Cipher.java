import java.util.*;
class Cipher
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the plain text");
		String pl=sc.nextLine();
		System.out.println("Enter the shift factor");
		int n=sc.nextInt();
		System.out.println("Cipher Text:");
		char a[]= pl.toCharArray();
		for(int i=0;i<a.length;i++)
		{
			a[i]=(char)(n+(int)a[i]);
		}
		for(int i=0;i<a.length;i++)
		{
			System.out.print(a[i]);
		}
		System.out.println();
	}
}
