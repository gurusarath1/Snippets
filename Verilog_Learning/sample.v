// Code your design here
module example1 (
  output Z,
  output reg y1,
  output reg y2,
  output reg y3,
  input clk,
  input reset,
  input x1,
  input x2,
  input x3
);
  
  reg y1_temp,y2_temp,y3_temp;
  
  always@(posedge clk) begin
    
    if(reset == 1) begin
      y1 <= 0;
      y2 <= 0;
      y3 <= 0;
    end
    else begin
      y1 <= y1_temp;
      y2 <= y2_temp;
      y3 <= y3_temp;
    end

  end
  
  always @(*) begin
    y1_temp = (x1 & x2) | (~x3);
    y2_temp = ~(x2 & x3) | x1;
    y3_temp = x1 & x2 & (~x3);
  end
  
  assign Z = ~(x1 ^ x2) | x3; 
  
  
endmodule
