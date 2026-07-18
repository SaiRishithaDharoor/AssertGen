module fsm(
    input logic clk,
    input logic rst,
    output logic done
);

always_ff @(posedge clk)
begin
    if(rst)
        done <= 0;
    else
        done <= 1;
end

endmodule