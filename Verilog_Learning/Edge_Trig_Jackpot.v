`timescale 1ns / 1ps

module switch(
    input [3:0] SWITCHES,
    input RST,
    input sysclk,
    output reg [3:0] LEDS
    );
    
    //reg [3:0] count_value; // current Counter value
    reg [27:0] sys_clk_count; // Number of ticks of the system clock
    reg divided_clk; // New clock signal produced by dividing the system clock
    integer win_flag;
    reg [3:0] PREV_SWITCH_STATE;
    
    /*
        Initialize the count values and divided clock signal
    */
    initial begin
        LEDS <= 4'b1000;
        sys_clk_count <= 0;
        divided_clk <= 0;
        win_flag <= 0;
        PREV_SWITCH_STATE <= 4'b0000;
    end
    
    /*
        Create a divided clock signal from the sysclk
    */
    always@(posedge sysclk) begin
        if(sys_clk_count == 12000000) begin
            sys_clk_count <= 0;
            divided_clk <= ~divided_clk; // Toggle the divided clock
        end
        else begin
            sys_clk_count <= sys_clk_count + 1;
        end
    end
    
    /*
        Core Logic
    */
    always@(posedge divided_clk) begin
    
        if (RST != 1)begin
            // Normal Operation
            // Check for switch transition and match
            if (SWITCHES[3:0] == LEDS[3:0] && PREV_SWITCH_STATE[0] == 0 && PREV_SWITCH_STATE[1] == 0 && PREV_SWITCH_STATE[2] == 0 && PREV_SWITCH_STATE[3] == 0) begin
                // Jackpot
                LEDS = 4'b1111;
            end
            else if (LEDS != 4'b1111) begin
                // Gnerate One Hot Sequence
                if(LEDS == 4'b0001) begin
                    LEDS = 4'b1000;
                end
                else begin
                    // Right shift
                    LEDS = LEDS >> 1;
                end
             end
         end
         else begin
            // RESET
            LEDS = 4'b1000;
         end
         
         PREV_SWITCH_STATE = SWITCHES[3:0];
    end

    
endmodule
