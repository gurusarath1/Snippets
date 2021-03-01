module counter(
    input COUNT_UP,
    input COUNT_DOWN,
    input RST,
    input sysclk,
    output [3:0] LEDS
    );
    

    reg [3:0] count_value; // current Counter value
    reg [27:0] sys_clk_count; // Number of ticks of the system clock
    reg divided_clk; // New clock signal produced by dividing the system clock
    
    assign LEDS[3:0] = count_value;
    
    /*
        Initialize the count values and divided clock signal
    */
    initial begin
        count_value <= 0;
        sys_clk_count <= 0;
        divided_clk <= 0;
    end
    
    /*
        Create a divided clock signal from the sysclk
    */
    always@(posedge sysclk) begin
    
        if(sys_clk_count == 62500000) begin
            sys_clk_count <= 0;
            divided_clk <= ~divided_clk; // Toggle the divided clock
        end
        else begin
            sys_clk_count = sys_clk_count + 1;
        end
    
    end
    
    /*
        Core functionality
    */
    always@(posedge divided_clk or posedge RST) begin
        
        if(RST == 1) begin // Reset the counter (Highest priority)
            count_value <= 0;
        end
        else if (COUNT_UP == 1) begin // Increment the counter by 1
            count_value <= count_value + 1;
        end
        else if (COUNT_DOWN == 1) begin // Decrement the counter by 1
            count_value <= count_value - 1;
        end
        
    end
    
endmodule
