def trace_factorial_program(input_val):
    # Initialize registers
    x1 = 0  # x_{ip+1} (Accumulator/Output)
    x2 = input_val  # x_{ip+2} (Input / Loop Counter)
    x3 = 0  # x_{ip+3}
    
    pc = 1  # Program Counter
    step = 1

    print(f"--- Tracing Factorial Program for Input x_{{ip+2}} = {input_val} ---")
    print(f"{'Step':<6} | {'Instr':<5} | {'x_1':<5} | {'x_2':<5} | {'x_3':<5} | Action")
    print("-" * 62)

    while True:
        state_log = f"{step:<6} | M{str(pc):<4} | {x1:<5} | {x2:<5} | {x3:<5} | "
        
        if pc == 1:
            x1 = 1  # suc(0)
            print(state_log + "x_1 := suc(0)")
            pc = 2
            
        elif pc == 2:
            # pred(pred(x)) subtracts 2, bottom-bounded at 0
            x3 = max(0, x2 - 2)
            print(state_log + "x_3 := pred(pred(x_2))")
            pc = 3
            
        elif pc == 3:
            # if x_{ip+3} goto M5
            if x3 > 0:
                print(state_log + f"if x_3 ({x3}) > 0 goto M5 -> JUMP")
                pc = 5
            else:
                print(state_log + f"if x_3 ({x3}) > 0 goto M4 -> FALLTHROUGH")
                pc = 4
                
        elif pc == 4:
            # if x_{ip+1} goto M_{end}
            if x1 > 0:
                print(state_log + f"if x_1 ({x1}) > 0 goto M10 -> JUMP TO END")
                pc = 10
            else:
                print(state_log + f"if x_1 ({x1}) > 0 goto M5 -> FALLTHROUGH")
                pc = 5
                
        elif pc == 5:
            # if x_{ip+2} goto M7
            if x2 > 0:
                print(state_log + f"if x_2 ({x2}) > 0 goto M7 -> JUMP")
                pc = 7
            else:
                print(state_log + f"if x_2 ({x2}) > 0 goto M7 -> FALLTHROUGH")
                pc = 6
                
        elif pc == 6:
            print(state_log + "halt")
            break  # End of program
            
        elif pc == 7:
            x1 = x1 * x2
            print(state_log + "x_1 := x_1 * x_2")
            pc = 8
            
        elif pc == 8:
            x2 = max(0, x2 - 1)
            print(state_log + "x_2 := pred(x_2)")
            pc = 9
            
        elif pc == 9:
            # if x_{ip+1} goto M5
            if x1 > 0:
                print(state_log + f"if x_1 ({x1}) > 0 goto M5 -> JUMP")
                pc = 5
            else:
                print(state_log + f"if x_1 ({x1}) > 0 goto M5 -> FALLTHROUGH")
                pc = 10
                
        elif pc == 10:
            # if x_{ip+1} goto M10
            if x1 > 0:
                print(state_log + f"if x_1 ({x1}) > 0 goto M10 -> JUMP")
                pc = 10
            else:
                print(state_log + f"if x_1 ({x1}) <= 0 goto M11 -> FALLTHROUGH")
                pc = 11
            break
                
        elif pc == 'end':
            print(state_log + "halt (reached M_end)")
            break
            
        else:
            print(f"Error: Unknown instruction M{pc}")
            break
            
        step += 1

    print("-" * 62)
    print(f"Final Output State: x_1 = {x1}, x_2 = {x2}, x_3 = {x3}")
    return x1

# --- Run the trace for an example input ---
if __name__ == "__main__":
    # Test with input 3
    trace_factorial_program(0)