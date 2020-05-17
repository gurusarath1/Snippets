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
public class Learning_New {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        System.out.println("Basics 1 -------- ");
        
        /*
        
        No line-continuation escape sequence
        Number of keywords = 50; Keyworkds const and goto are reserved but not used.
        Variables are created when their scope is entered and destroyed when their scope is left.
        Unlike C - You cannot declare a variable to have the same name as one in an outer scope.
        
        ===================
        Number of bytes:
        ===================
        int - 32
        long - 32
        short - 16
        byte - 8
        
        double - 64
        float - 32
        
        char - 2
        ===================
        
        
        int - 
        -2,147,483,648 to 2,147,483,647
        Java does not support unsigned, positive-only integers
        octal - 0
        Hex - 0x or 0X
        long - l
        binary - 0b
        
        floating point - 
        IEEE-754
        single precision is usually faster.
        Double precision is actually faster than single precision in some of the modern processors.
        
        char - 
        Unicode
        char is referred to as integral type
        ASCII occupies first 127 values        
        */
        
        int a,b;
        a = 10;
        b = 10;
        System.out.println(a+b);
        
        // ------------------------------------------------------------------------------------------------
        
        System.out.println("Arrays 1 -------- ");
        
        int firstArray[]; // Declare an array
        firstArray = new int[12]; // assign the array
        
        int SecondArray[] = {1,2,3,4,5};
        for (int i : SecondArray)
        {
            System.out.println(i);
        }
        
        int TwoD_array_1[][] = new int[3][3];
        
        int TwoD_array_2[][] = new int[3][];
        TwoD_array_2[0] = new int[5];
        TwoD_array_2[1] = new int[2];
        TwoD_array_2[2] = new int[10];
        
        int TwoD_array_3[][] = { {1,2}, {3,4} };
        
        // ------------------------------------------------------------------------------------------------
        
        System.out.println("Arrays 2 -------- ");
        
        System.out.println(firstArray.length); //12
        System.out.println(TwoD_array_1.length); //3
        System.out.println(TwoD_array_2.length); //3
        System.out.println(TwoD_array_2[2].length); //10
        System.out.println(firstArray.getClass());
        
        
        
        // ------------------------------------------------------------------------------------------------
        
        System.out.println("Classes 1 -------- ");
        
        Box box_0;
        Box box_1 = new Box(); // New dynamically allocates memory for the object and returns the reference to it
        Box box_2 = new Box(5);
        Box box_3 = new Box(5,1,2);
        
        System.out.println(box_1.getVolume()); //0
        System.out.println(box_2.getVolume()); //125
        System.out.println(box_3.getVolume()); //10
        
    }
    
}
