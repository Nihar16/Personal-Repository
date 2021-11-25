import java.util.Scanner;
class CGPA
{
  public static void main(String args[])
  {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter number of subjects");
     int n=sc.nextInt();
     double[] marks=new double[n];
     for(int i=0;i<n;i++)
     {
    	 System.out.println("Enter marks of subject "+(i+1));
        marks[i]=sc.nextDouble();
     }
     double sum= cgpaCalculation(marks);
     double cgpa=sum/n;
     System.out.println("CGPA="+cgpa);
     System.out.println("Percantage from CGPA="+cgpa*9.5+"%");
  }
 static double  cgpaCalculation(double marks[])
 {
    double sum=0; 
    for(int i=0;i<marks.length;i++)
    {
    	sum+=(marks[i]/10) ;
    }
     return sum;
   }
}