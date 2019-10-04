import java.util.*;

class PriorityQ
{
   private Path[] q;
 
   public PriorityQ()
   {
      q=new Path[200];
   }

   public int getLength()
   {
     int i=0;
 
     while(q[i]!=null)
       i++;

     return i;
    }    

   public void insert(Path p)
   {
      int i=0,j;

      if(getLength()==0)
        q[0]=p;
      else
      {
         while(i<=getLength()-1 && q[i].totalcost()<p.totalcost())
           i++;

         if(i==getLength())
           q[getLength()]=p;

         else{
        
         for(j=getLength()-1;j>=i;j--)
           q[j+1]=q[j];

         q[i]=p;
      }}
   }

   public Path removehead()
   {
      Path p=q[0];
      int i;
       
      if(getLength()==1)
        q[0]=null;
 
      else      
      {
 	     for(i=1;i<=getLength()-1;i++)
           q[i-1]=q[i];

         q[getLength()-1]=null;
      }		 
  
      return p;
   }

   public boolean empty()
   {
      if(getLength()==0)
        return true;
 
      else
        return false;
   }
}

class Path
{
   private int heuristic;
   private int pathcost;
   private int[] path=new int[100];

   public Path(int heuristic,int cost,int[] path,int node)
   {
      this.heuristic=heuristic;
      pathcost=cost;
      this.path=path;
	  this.path[getLength()]=node;
     
   }

   public Path(int heuristic,int cost,int startnode,int node)
   {
      int i;
      for(i=0;i<=99;i++)
        path[i]=-1;
      this.heuristic=heuristic;
      pathcost+=cost;
      path[0]=startnode;
      path[1]=node;
      
   }

   public int getLength()
   {
     int i=0;
    
     while(path[i]!=-1)
       i++;

     return i;
   }

   public int totalcost()
   {
      return heuristic+pathcost;
   }

   public int lastnode()
   {
      return path[getLength()-1];
   }

   public void display()
   {
      int i;
 
      for(i=0;i<=getLength()-1;i++)
        System.out.print(path[i] + " ");

      System.out.println();
   }
   
   public int getCost()
   {
	   return pathcost;
   }
   
   public int[] getPath()
   {
	   return path;
   }
   
   public int getHeuristic()
   {
	   return heuristic;
   }

}
         
   
class A
{
   private int[][] al;
   private int[] h;
   private int n;
   private Path result;
   private PriorityQ q;

   public A(int[][] al,int[] h,int n)
   {
      this.al=al;
      this.h=h;
      this.n=n;
      q=new PriorityQ();
   }

   public Path start(int s,int g)
   {
      int i;
      
      while(true)
	  {
         if(q.empty())
		 {
            for(i=0;i<=n-1;i++)
              if(al[s][i]!=0)
			  {
                 if(i==g)
                   result=new Path(h[i],al[s][i],s,i);
                 else
		           q.insert(new Path(h[i],al[s][i],s,i));
			  }
		 }
         
      
       else
       {
          
          Path p=q.removehead();
		  
		  int[] pat=p.getPath();
		  
		  int cost=p.getCost();
          int node=p.lastnode();
		  System.out.println(p.totalcost());
		  p.display();
		
		  
          for(i=0;i<=n-1;i++)
            if(al[node][i]!=0)
            { 
               int[] copy=new int[100];
		       int k;
		       for(k=0;k<=99;k++)
			     copy[k]=pat[k];		
               		
		       Path p1=new Path(h[i],cost+al[node][i],copy,i);
			  // p1.display();
			   if(i==g)
               { 
				  if(result==null || p1.totalcost()<result.totalcost())
				    result=p1;
               }
               else
			     q.insert(p1);
			 } 
        }

        if(q.empty())
          break;
      }
 
        return result;
   }
}    
               
       
class UseA
{
   public static void main(String args[])
   {
      Scanner sc=new Scanner(System.in);
      System.out.print("Enter no. of nodes : ");
      int n=sc.nextInt();
      int[][] al=new int[n][n];
      int[] h=new int[n];
      int i,j;
      System.out.println("Enter the weights of edges");
      for(i=0;i<=n-1;i++)
        for(j=0;j<=n-1;j++)
        {
           if(i!=j)
           {
              System.out.print("From node " + i + " to " + j + " : ");
              al[i][j]=sc.nextInt();
           }
        }
 
      for(i=0;i<=n-1;i++)
      {
         System.out.print("Enter heuristic value of node " + i + " : ");
         h[i]=sc.nextInt();
      }

      System.out.print("Enter the start node : ");
      int s=sc.nextInt();

      System.out.print("Enter the goal node : ");
      int g=sc.nextInt();

      // Start of the main program to find the path heuristically using Astar
      Path p=new A(al,h,n).start(s,g);
 
      System.out.println("Cost to reach the GOAL : " + p.totalcost());
      System.out.println("Corresponding route : ");
      p.display();
   }
}