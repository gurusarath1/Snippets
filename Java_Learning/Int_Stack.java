/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package learning_new;

/**
 *
 * @author gsgur
 */
public class Int_Stack {
    
    
    private int stackX[] = new int[5];
    private int tos = 0;
    static int numberOfObjects = 0;
    
    /*
    ACCESS CONTROL ---------
    public -  Can be accessed by any code
    private - Only by other members of the class
    protected - Can be accessed only by the class and subclass (same pkg / different pkg)
    default - public within its own package (cannot be accessed outside its package)
    _________________________________________________________________
    |           │ Class │ Package │ Subclass │ Subclass │ World  |
    |           │       │         │(same pkg)│(diff pkg)│        |
    -----------------------------------------------------------------
    |public     │   +   │    +    │    +     │     +    │   +    | 
    |protected  │   +   │    +    │    +     │     +    │        | 
    |no modifier│   +   │    +    │    +     │          │        | 
    |private    │   +   │         │          │          │        |
    |___________|________|__________|__________|___________|________|
     + : accessible         blank : not accessible
    
    */
    
    /*
    STATIC METHODS ---------
    They can only directly call other static methods 
    They can access only other static data (Cannot access instance data)
    They cannot use super or this.
    */
    
    // Static block
    static {
        System.out.println("This is a static block !");
    }
    
    // Static Function
    public static int getNumberOfObjects()
    {
        return numberOfObjects; // Can only access static members
    }
    
    
    Int_Stack()
    {
        numberOfObjects += 1;
    }
    
    public void push(int val)
    {
        if(tos <= 4)
        {
            stackX[this.tos] = val;
            this.tos++;
        }
        else
        {
            System.out.println("Stack is full");
        }
    }
    
    public int pop()
    {
        if(tos >= 1)
        {
            this.tos--;
            return stackX[this.tos];
        }
        else
        {
            return -1;
        }
    }
    
}
