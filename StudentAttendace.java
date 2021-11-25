import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Frame;
import java.awt.GridLayout;
import java.awt.Label;
import java.awt.TextArea;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.util.HashMap;
import java.util.Set;
class Stud extends Attendance{
	String name,div,branch,roll;
	Stud(String n,String r,String d,String b,int am3,int ctn,int dsd,int edc,int oopj,int eic)
	{
		name=n;
		div=d;
		roll=r;
		branch=b;
		this.am3=am3;
		this.ctn=ctn;
		this.dsd=dsd;
		this.edc=edc;
		this.oopj=oopj;
		this.eic=eic;
	}
	String getName()
	{
		return name;
	}
	String getBranch()
	{
		return branch;
	}
	String getRoll()
	{
		return roll;
	}
	String getDiv()
	{
		return div;
	}
	public String toString()
	{
		return name+" "+roll+" "+div+" "+branch;
	}
}
class Attendance {
	int am3,ctn,dsd,edc,oopj,eic;
	double gettotal()
	{
		return((double)(am3+ctn+dsd+oopj+eic+edc)/300*100);
	}
	double getedc()
	{
		return ((double)edc/50*100);	
	}
	double getctn()
	{
		return ((double)ctn/50*100);
	}
	double getdsd()
	{
		return ((double)dsd/50*100);
	}
	double getoopj()
	{
		return ((double)oopj/50*100);
	}
	double geteic()
	{
		return ((double)eic/50*100);
	}
	double getam3()
	{
		return ((double)am3/50*100);
	}
}
public class StudentAttendace extends Frame implements WindowListener,ActionListener{
Label nameLabel,rollLabel,divLabel,branchLabel,am3Label,ctnLabel,dsdLabel,edcLabel,oopjLabel,eicLabel,totalLabel;
TextField nameText,rollText,branchText,divText,am3Text,ctnText,dsdText,edcText,oopjText,eicText,totalText;
Button addButton,searchButton,displayallButton,clearButton,deleteButton,totalButton;
HashMap<String,Stud>x;
StudentAttendace()
{
	x=new HashMap<>();
	nameLabel=new Label("Name");
	rollLabel=new Label("Roll Number");
	divLabel=new Label("Division");
	branchLabel=new Label("Branch");
	am3Label=new Label("AM3");
	ctnLabel=new Label("CTN");
	dsdLabel=new Label("DSD");
	edcLabel=new Label("EDC");
	oopjLabel=new Label("OOPJ");
	eicLabel=new Label("EIC");
	totalLabel=new Label("Total");
	nameText=new TextField(20);
	rollText=new TextField(20);
	branchText=new TextField(20);
	divText=new TextField(20);
	am3Text=new TextField(20);
	ctnText=new TextField(20);
	dsdText=new TextField(20);
	edcText=new TextField(20);
	oopjText=new TextField(20);
	eicText=new TextField(20);
	totalText=new TextField(20);
	addButton=new Button("Add");
	searchButton=new Button("Search");
	displayallButton=new Button("Display All");
	clearButton=new Button("Clear");
	deleteButton=new Button("Delete");
	totalButton=new Button("Calculate Attendance");
	setLayout(new GridLayout(14,2));
	add(nameLabel);
	add(nameText);
	add(rollLabel);
	add(rollText);
	add(divLabel);
	add(divText);
	add(branchLabel);
	add(branchText);
	add(am3Label);
	add(am3Text);
	add(ctnLabel);
	add(ctnText);
	add(dsdLabel);
	add(dsdText);
	add(oopjLabel);
	add(oopjText);
	add(edcLabel);
	add(edcText);
	add(eicLabel);
	add(eicText);
	add(totalLabel);
	add(totalText);
	add(addButton);
	add(searchButton);
	add(clearButton);
	add(deleteButton);
	add(displayallButton);
	add(totalButton);
	totalButton.addActionListener(this);
	addButton.addActionListener(this);
	searchButton.addActionListener(this);
	clearButton.addActionListener(this);
	displayallButton.addActionListener(this);
	deleteButton.addActionListener(this);
	addWindowListener(this);
	setSize(400,400);
	setVisible(true);
}
public static void main(String[] args) {
	StudentAttendace g=new StudentAttendace();
}
public void windowActivated(WindowEvent arg0) {}
public void windowClosed(WindowEvent arg0) {}
public void windowClosing(WindowEvent arg0) {
	System.exit(0);	
}
public void windowDeactivated(WindowEvent arg0) {}
public void windowDeiconified(WindowEvent arg0) {}
public void windowIconified(WindowEvent arg0) {}
public void windowOpened(WindowEvent arg0) {}
public void actionPerformed(ActionEvent e) {
	if(e.getSource().equals(totalButton))
	{
		String roll=rollText.getText();
		Stud temp=x.get(roll);
		if(temp==null)
			totalText.setText("Not Found");
		else
		{
			divText.setText(temp.getDiv()+"%");
			am3Text.setText(temp.getam3()+"%");
			ctnText.setText(temp.getctn()+"%");
			dsdText.setText(temp.getdsd()+"%");
			edcText.setText(temp.getedc()+"%");
			oopjText.setText(temp.getoopj()+"%");
			eicText.setText(temp.geteic()+"%");
			totalText.setText(temp.gettotal()+"%");;
		
		}}
else if(e.getSource().equals(deleteButton))
	{
		String roll=rollText.getText();
		Stud del=x.get(roll);
		if(del==null)
		{
			nameText.setText(" ");
			branchText.setText(" ");
			rollText.setText("Not Found");
			divText.setText(" ");
			am3Text.setText(" ");
			ctnText.setText(" ");
			dsdText.setText(" ");
			edcText.setText(" ");
			oopjText.setText(" ");
			eicText.setText(" ");
			totalText.setText(" ");
			nameText.setText("");
			branchText.setText("");
			divText.setText("");
			am3Text.setText("");
			ctnText.setText("");
			dsdText.setText("");
			edcText.setText("");
			oopjText.setText("");
			eicText.setText("");
			totalText.setText("");
		}
		else
		{
			x.remove(roll);
			rollText.setText(roll+" Deleted successfully");
			nameText.setText(" ");
			branchText.setText(" ");
			divText.setText(" ");
			am3Text.setText(" ");
			ctnText.setText(" ");
			dsdText.setText(" ");
			edcText.setText(" ");
			oopjText.setText(" ");
			eicText.setText(" ");
			totalText.setText(" ");
			nameText.setText("");
			branchText.setText("");
			divText.setText("");
			am3Text.setText("");
			ctnText.setText("");
			dsdText.setText("");
			edcText.setText("");
			oopjText.setText("");
			eicText.setText("");
			totalText.setText("");
		}
        }
else if(e.getSource().equals(displayallButton))
	{
		DisplayAll d=new DisplayAll(x);
		d.setVisible(true);
	}
else if(e.getSource().equals(addButton))
	{
	int am3=Integer.parseInt(am3Text.getText());
	int ctn=Integer.parseInt(ctnText.getText());
	int dsd=Integer.parseInt(dsdText.getText());
	int edc=Integer.parseInt(edcText.getText());
	int oopj=Integer.parseInt(oopjText.getText());
	int eic=Integer.parseInt(eicText.getText());
		String name=nameText.getText();
		String roll=rollText.getText();
		String branch=branchText.getText();
		String div=divText.getText();
		nameText.setText("");
		rollText.setText("");
		branchText.setText("");
		divText.setText("");
		am3Text.setText("");
		ctnText.setText("");
		dsdText.setText("");
		edcText.setText("");
		oopjText.setText("");
		eicText.setText("");
		totalText.setText(" ");
		totalText.setText("");
		x.put(roll, new Stud(name,roll,div,branch,am3,ctn,dsd,edc,oopj,eic));
	}
	else if(e.getSource().equals(clearButton))
	{
		nameText.setText(" ");
		branchText.setText(" ");
		rollText.setText(" ");
		divText.setText(" ");
		am3Text.setText(" ");
		ctnText.setText(" ");
		dsdText.setText(" ");
		edcText.setText(" ");
		oopjText.setText(" ");
		eicText.setText(" ");
		totalText.setText(" ");
		nameText.setText("");
		branchText.setText("");
		rollText.setText("");
		divText.setText("");
		am3Text.setText("");
		ctnText.setText("");
		dsdText.setText("");
		edcText.setText("");
		oopjText.setText("");
		eicText.setText("");
		totalText.setText("");
	}
	else {
		String roll=rollText.getText();
		Stud s=x.get(roll);
		if(s!=null)
		{
			nameText.setText(s.getName());
			branchText.setText(s.getBranch());
			divText.setText(s.getDiv());
			am3Text.setText(s.getam3()+"%");
			ctnText.setText(s.getctn()+"%");
			dsdText.setText(s.getdsd()+"%");
			edcText.setText(s.getedc()+"%");
			oopjText.setText(s.getoopj()+"%");
			eicText.setText(s.geteic()+"%");
			totalText.setText(s.gettotal()+"%");
		}
		else
			{
			if(roll.length()==0)
				rollText.setText("Please enter a Roll Number to search");
			else {
			nameText.setText(" ");
			rollText.setText("Not Found");
			divText.setText(" ");
			branchText.setText(" ");
			branchText.setText("");
			divText.setText("");
			am3Text.setText(" ");
			ctnText.setText(" ");
			dsdText.setText(" ");
			edcText.setText(" ");
			oopjText.setText(" ");
			eicText.setText(" ");
			totalText.setText(" ");
			am3Text.setText("");
			ctnText.setText("");
			dsdText.setText("");
			edcText.setText("");
			oopjText.setText("");
			eicText.setText("");
			totalText.setText("");
            }}
		}}}
class DisplayAll extends Frame implements ActionListener{
	HashMap<String,Stud>x;
	TextArea all=new TextArea();
	Button b=new Button("Back");
	DisplayAll(HashMap<String,Stud>x)
	{
		add(all);
		add(b,BorderLayout.SOUTH);
		b.addActionListener(this);
		this.x=x;
		setSize(400,400);
		setVisible(true);
		Set<String> sets=x.keySet();
		all.append("Name"+"\t\t"+"Roll Number"+"\t"+"Division"+"\t"+"Branch"+"AM3"+"\t"+"CTN"+"\t"+"DSD"+"\t"+"EDC"+"\t"+"EIC"+"\t"+"OOPJ"+"\t"+"TOTAL"+"\n");
		for(String t:sets)
		{
			Stud v=x.get(t);
			all.append(v.getName()+"\t\t"+v.getRoll()+"\t"+v.getDiv()+"\t"+v.getBranch()+"\t"+v.getam3()+"\t"+v.getctn()+"\t"+v.getdsd()+"\t"+v.getedc()+"\t"+v.geteic()+"\t"+v.getoopj()+"\t"+v.gettotal()+"\n");
}}
	public void windowClosing(WindowEvent arg0) {
		this.dispose();
	}
	public void actionPerformed(ActionEvent arg0) {
		this.dispose();	
}}