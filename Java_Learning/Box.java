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
public class Box {
    
    float l,b,h;
    
    /*
    CONSTRUCTOR -----------
    Same name as the class
    No return type (not even void)
    Returns class type (implicitly)
    Automatically initializes the object immediately upon creation.
    Default constructor initializes all the variables to zero.
    */
    Box()
    {
        this(1); // CONSTRUCTOR CHAINING
        System.out.println("Constructor 1 called 2");
        
    }
    
    Box(float d)// Constructor 1
    {
        System.out.println("This is constructor 2");
        this.l = d;
        this.b = d;
        this.h = d;
    }
    
    Box(float l, float b, float h)// Constructor 2
    {
        System.out.println("This is constructor 3");
        this.l = l;
        this.b = b;
        this.h = h;
    }
    
    double getVolume()
    {
        return l*b*h;
    }
    
    void setDimensions(float l, float b, float h)
    {
        this.l = l;
        this.b = b;
        this.h = h;
    }
    
    /*
    ARGUMENT PASSING -----------
    When primitive types are passed - Pass by value
    When objects are passed - Pass by reference (But the reference itself is passed by value)
    */
    boolean equals(Box b)
    {
        if(b.l == this.l && b.b == this.b && b.h == this.h)
        {
            return true;
        }
        return false;
    }
    
    /*
    METHOD OVERLOADING -----------
    dataType and number of arguments is used to guide which version to call.
    Return type do not play a role in overload resolution.
    */
    void setDimensions(float x)
    {
        this.l = x;
        this.b = x;
        this.h = x;
    }
    
    /*
    FINALIZE -----------
    Only called prior to garbage collection
    You cannot be sure when or even if finalize() will be executed.
    Therefore, your program should provide other means of releasing system resources.
    finalize is not a destructor (it only approximates a destructor)
    */
    protected void finalize()
    {
        System.out.println("Box finalize method was called !");
    }
}
