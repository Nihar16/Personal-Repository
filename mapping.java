import java.util.*;
import java.lang.*;
class mapping
{
    public static void main(String args[])
    {
        int mm,cm,block,choice;
        mapping m=new mapping();
        System.out.println("Enter the size of the Main Memory in MB: ");
        Scanner sc=new Scanner(System.in);
        mm=sc.nextInt();
        System.out.println("Enter the size of the Cache Memory in KB: ");
        cm=sc.nextInt();
        System.out.println("Enter the size of the block in B: ");
        block=sc.nextInt();
        System.out.println("Main Menu\n1.Direct mapping\n2.Associative mapping\n3.Set Associative mapping\nEnter your choice");
        choice=sc.nextInt();
        do
        {
            switch(choice)
            {
                case 1:
                m.direct(mm,cm,block);
                break;
                case 2:
                m.assoc(mm,block);
                break;
                case 3:
                m.set_assoc(mm,cm,block);
                break;
                default:
                System.out.println("Invalid Input");
            }
        }while(choice<1||choice>3);
    }
    void direct(int mm,int cm,int b)
    {
        int lines,tag,msize,csize,bsize;
        double mlog2=Math.log(2);
        cm*=1024;
        msize=(int)(Math.log(mm*Math.pow(2,20))/mlog2);
        csize=(int)(Math.log(cm)/mlog2);
        bsize=(int)(Math.log(b)/mlog2);
        lines=csize-bsize;
        tag=msize-lines-bsize;
        System.out.println("Tag="+tag+"\tLines="+lines+"\tWords="+bsize);
    }
    void assoc(int mm,int b)
    {
        int tag,msize,bsize;
        double mlog2=Math.log(2);
        msize=(int)(Math.log(mm*Math.pow(2,20))/mlog2);
        bsize=(int)(Math.log(b)/mlog2);
        tag=msize-bsize;
        System.out.println("Tag="+tag+"\tWords="+bsize);
    }
    void set_assoc(int mm,int cm,int b)
    {
        Scanner sc=new Scanner(System.in);
        int tag,msize,csize,lines,bsize,n;
        cm*=1024;
        double mlog2=Math.log(2);
        msize=(int)(Math.log(mm*Math.pow(2,20))/mlog2);
        csize=(int)(Math.log(cm)/mlog2);
        bsize=(int)(Math.log(b)/mlog2);
        lines=csize-bsize;
        System.out.println("What n-way set associative do you want?:");
        n=sc.nextInt();
        int s=(int)(lines/Math.log(n)/mlog2);
        tag=msize-s-bsize;
        System.out.println("Tag="+tag+"\tSets="+s+"\tWords="+bsize);
    }
}
