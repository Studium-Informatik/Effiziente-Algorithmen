def trace_fibonacci_program(input_val):
    # Initialize registers based on the x_{ip+n} notation
    x1 = 0  # x_{ip+1}
    x2 = input_val  # x_{ip+2} -> This acts as the loop counter / input
    x3 = 0  # x_{ip+3}
    x4 = 0  # x_{ip+4}
    
    pc = 1  # Program Counter (starts at instruction M1)
    step = 1

    print(f"--- Tracing Fibonacci Program for Input x_{{ip+2}} = {input_val} ---")
    print(f"{'Step':<6} | {'Instr':<5} | {'x_1':<5} | {'x_2':<5} | {'x_3':<5} | {'x_4':<5} | Action")
    print("-" * 65)

    while True:
        # Log current state before executing the instruction
        state_log = f"{step:<6} | M{pc:<4} | {x1:<5} | {x2:<5} | {x3:<5} | {x4:<5} | "
        
        if pc == 1:
            x1 = 1  # suc(0)
            print(state_log + "x_1 := suc(0)")
            pc = 2
            
        elif pc == 2:
            x3 = 1  # suc(0)
            print(state_log + "x_3 := suc(0)")
            pc = 3
            
        elif pc == 3:
            x2 = max(0, x2 - 2)  # pred(pred(x2))
            print(state_log + "x_2 := pred(pred(x2))")
            pc = 4
            
        elif pc == 4:
            # if x_{ip+2} goto M5 (jump if strictly greater than 0)
            if x2 > 0:
                print(state_log + f"if x_2 ({x2}) > 0 goto M5 -> JUMP")
                pc = 6
            else:
                print(state_log + f"if x_2 ({x2}) > 0 goto M5 -> FALLTHROUGH")
                pc = 5
                
        elif pc == 5:
            print(state_log + "halt")
            break  # End of program
            
        elif pc == 6:
            x4 = x1
            print(state_log + "x_4 := x_1")
            pc = 7
            
        elif pc == 7:
            x1 = x1 + x3
            print(state_log + "x_1 := x_1 + x_3")
            pc = 8
            
        elif pc == 8:
            x3 = x4
            print(state_log + "x_3 := x_4")
            pc = 9
            
        elif pc == 9:
            # pred(x) is the monus operation: x - 1 if x > 0 else 0
            x2 = max(0, x2 - 1)
            print(state_log + "x_2 := pred(x_2)")
            pc = 10
            
        elif pc == 10:
            # if x_{ip+1} goto M3
            if x1 > 0:
                print(state_log + f"if x_1 ({x1}) > 0 goto M3 -> JUMP")
                pc = 4
            else:
                print(state_log + f"if x_1 ({x1}) > 0 goto M3 -> FALLTHROUGH")
                pc = 11 # Should theoretically never happen since x1 >= 1
                
        else:
            print(f"Error: Unknown instruction M{pc}")
            break
            
        step += 1

    print("-" * 65)
    print(f"Final Output State: x_1 = {x1}, x_2 = {x2}, x_3 = {x3}, x_4 = {x4}")
    return x1

# --- Run the trace for an example input ---
if __name__ == "__main__":
    trace_fibonacci_program(10)