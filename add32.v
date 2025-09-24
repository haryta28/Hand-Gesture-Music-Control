module add32(clk,a,b,sum);
input clk;
input [31:0]a;
input [31:0]b;
output [32:0]sum;
reg [32:0] sum;
always @(posedge clk)
begin
sum=a+b;
end
endmodule
