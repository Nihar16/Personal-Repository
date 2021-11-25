import java.util.*;
class MemorySim 
{
    ArrayList <Integer> myMemoryHoles;
    private int value;
    private int Max;
    private int Min;
    public static void main(String[] args) 
    {
	    MemorySim memorySim = new MemorySim();
	    memorySim.setMemoryHoles( new ArrayList<Integer>());
	    ArrayList<Integer> myMemoryHoles2 = memorySim.getMemoryHoles();
	    Random intRandom = new Random();
	    for (int i = 0; i < 6; i++) 
	    {
	    	myMemoryHoles2.add(intRandom.nextInt(1000));
	    }
	    System.out.println("The random values of MB in the ArrayList are: ");
	    Iterator <Integer> it = memorySim.getMemoryHoles().iterator();
	    while (it.hasNext()) 
	    {
	    	System.out.println(it.next());
	    }
	    	System.out.println();
	    
	    Collections.sort(memorySim.getMemoryHoles());
	    System.out.println("The ordered values of MB in the ArrayList are: ");
	    Iterator <Integer>i = memorySim.getMemoryHoles().iterator();
	    while(i.hasNext())
	    {
	    	System.out.println(i.next());
	    }
	    
	    
	    System.out.println("The maximum value in the ArrayList is: ");
	    System.out.println( Collections.max( memorySim.getMemoryHoles()));
	    System.out.println();
	    System.out.println("The minimum value of MB in the ArrayList is: ");
	    System.out.println( Collections.min( memorySim.getMemoryHoles()));
	    
	    memorySim.setMin ( Integer.parseInt(Collections.min(memorySim.getMemoryHoles()).toString()) );
	    memorySim.setMax ( Integer.parseInt(Collections.max(memorySim.getMemoryHoles()).toString()) );
	    Scanner input = new Scanner(System.in);
	    System.out.print("Enter number of MB needing space: ");
	    memorySim.value = input.nextInt();
	    memorySim.firstFit();
	    memorySim.worstFit();
	    memorySim.bestFit();
   } 
	    private ArrayList<Integer> getMemoryHoles() 
	    {
	    	return myMemoryHoles;
	    }
	    private void setMemoryHoles(ArrayList<Integer> arrayList) 
	    {
	    	myMemoryHoles = arrayList;
	    }
	    public int getValue() 
	    {
	    	return value;
	    }
	    public void setValue(int value) 
	    {
	    	this.value = value;
	    }
	    public int getMax() 
	    {
	    	return Max;
	    }
	    public void setMax(int max) 
	    {
	    	Max = max;
	    }
	    public int getMin()
	    {
	    	return Min;
	    }
	    public void setMin(int min)
	    {
	    	Min = min;
	    }
	    public void firstFit()
	    {
	    	int index;
	    	for( int j = 0; j < myMemoryHoles.size(); j++)
	    	{
	    
	    		if( value <= myMemoryHoles.get(j) )
	    		{
	    			System.out.printf("First fit value: %d MB fits in %d MB hole", value, j);
	    			System.out.println();
	    			return;
	    		}
	    		else
	    		{
	    			System.out.printf("%d MB will have to wait for first fit.", value);
	    			System.out.println();
	    		return;
	    		}
	    	}
	    }
	    public void worstFit()
	    {
	    
	    	for (int index : myMemoryHoles)
	    	{
	    		if( value <= Max)
	    		{
	    			System.out.printf("Worst fit for %d MB is in %d MB hole", value, index);
	   	
	    			System.out.println();
	    			return;
	    		}
	    		else
	    		{
	    		
	    			System.out.printf("%d MB will have to wait for worst fit.", value);
	    			System.out.println();
	    			return;
	    		}
	    	}
	    }
	    public void bestFit()
	    {
	    	int m = 0;
	    	for (int l = 0; l < myMemoryHoles.size(); l++)
	    	{
	    		int n = myMemoryHoles.get(l) - value;
	    		if (n > 0)
	    		{	
	    			m = n;
	    			if (myMemoryHoles.get(l) - value > m)
	    			{
	    				m = myMemoryHoles.get(l);
	    				System.out.printf("Best fit for %d MB is in %d MB hole", value, myMemoryHoles.get(l));
	    				System.out.println();
	    				return;
	    			}
	    			else
	    			{
	    				System.out.printf("%d MB will have to wait for best fit.", value);
	    				System.out.println();
	    				return;
	    			}
	    		}
	    	}
    	}
}
