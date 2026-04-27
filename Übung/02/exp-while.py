class State:
    def __init__(self, values):
        self.values = list(values)
        
    def __str__(self):
        return f"({', '.join(map(str, self.values))}, \\dots)"
        
    def copy(self):
        return State(self.values)

# Map abstract variable names to state array indices
VAR_MAP = {"x_{ip+1}": 0, "x_{ip+2}": 1, "x_{ip+3}": 2}

class Assign:
    def __init__(self, target, src):
        self.target = target
        self.src = src
        
    def __str__(self):
        return f"{self.target} := {self.src}"
        
    def eval(self, state):
        new_state = state.copy()
        new_state.values[VAR_MAP[self.target]] = state.values[VAR_MAP[self.src]]
        return new_state

class AssignConst:
    def __init__(self, target, val):
        self.target = target
        self.val = val
        
    def __str__(self):
        return f"{self.target} := {self.val}"
        
    def eval(self, state):
        new_state = state.copy()
        new_state.values[VAR_MAP[self.target]] = self.val
        return new_state

class Suc:
    def __init__(self, target):
        self.target = target
        
    def __str__(self):
        return f"{self.target} := \\text{{suc}}({self.target})"
        
    def eval(self, state):
        new_state = state.copy()
        new_state.values[VAR_MAP[self.target]] += 1
        return new_state

class AddMacro:
    def __init__(self, target, src1, src2):
        self.target = target
        self.src1 = src1
        self.src2 = src2
        
    def __str__(self):
        return f"{self.target} := {self.src1} + {self.src2}"
        
    def eval(self, state):
        new_state = state.copy()
        new_state.values[VAR_MAP[self.target]] = state.values[VAR_MAP[self.src1]] + state.values[VAR_MAP[self.src2]]
        return new_state

class MultMacro:
    def __init__(self, target, src1, src2):
        self.target = target
        self.src1 = src1
        self.src2 = src2
        
    def __str__(self):
        return f"{self.target} := {self.src1} \\cdot {self.src2}"
        
    def eval(self, state):
        new_state = state.copy()
        new_state.values[VAR_MAP[self.target]] = state.values[VAR_MAP[self.src1]] * state.values[VAR_MAP[self.src2]]
        return new_state

class Loop:
    def __init__(self, var, body):
        self.var = var
        self.body = body
        
    def __str__(self):
        body_str = "; ".join(str(s) for s in self.body)
        return f"\\textbf{{loop}} {self.var} \\textbf{{do}} {body_str} \\textbf{{end}}"
        
    def unfold(self, state):
        count = state.values[VAR_MAP[self.var]]
        unfolded = []
        for _ in range(count):
            unfolded.extend(self.body)
        return unfolded

def format_stmts(stmts):
    if not stmts:
        return "\\epsilon"
    return "; ".join(str(s) for s in stmts)

def evaluate(state, stmts, program_name):
    lines = []
    lines.append(f"\\delta({state}, \\text{{{program_name}}}) =")
    lines.append(f"\\delta({state}, {format_stmts(stmts)}) =")
    
    while len(stmts) > 0:
        if len(stmts) > 1:
            first = stmts[0]
            rest = stmts[1:]
            lines.append(f"\\delta(\\delta({state}, {first}), {format_stmts(rest)}) =")
            
            # Evaluate the first statement in the sequence
            state = first.eval(state)
            lines.append(f"\\delta({state}, {format_stmts(rest)}) =")
            stmts = rest
        else:
            first = stmts[0]
            if isinstance(first, Loop):
                unfolded = first.unfold(state)
                if not unfolded:
                    stmts = [] # Loop executes 0 times
                else:
                    lines.append(f"\\delta({state}, {format_stmts(unfolded)}) =")
                    stmts = unfolded
            else:
                state = first.eval(state)
                stmts = []
                
    lines.append(f"{state}")
    return lines

if __name__ == "__main__":
    # Define the programs based on the provided LaTeX input
    p_add = [
        Assign("x_{ip+1}", "x_{ip+2}"),
        Loop("x_{ip+3}", [Suc("x_{ip+1}")])
    ]
    
    p_mult = [
        AssignConst("x_{ip+1}", 0),
        Loop("x_{ip+3}", [AddMacro("x_{ip+1}", "x_{ip+1}", "x_{ip+2}")])
    ]
    
    p_exp = [
        AssignConst("x_{ip+1}", 0),
        Suc("x_{ip+1}"),
        Loop("x_{ip+3}", [MultMacro("x_{ip+1}", "x_{ip+1}", "x_{ip+2}")])
    ]
    
    # State mapping: [x_{ip+1}, x_{ip+2}, x_{ip+3}, ...]
    # We initialize input variables: x_{ip+2} = 3, x_{ip+3} = 2
    
    print("=== Evaluation trace for 'add' ===")
    print("$$\n\\begin{align*}")
    init_state_add = State([0, 3, 2, 0])
    for line in evaluate(init_state_add, p_add, "P add"):
        print(line, "\\\\")
    print("\\end{align*}\n$$")
        
        
    print("\n=== Evaluation trace for 'mult' ===")
    print("$$\n\\begin{align*}")
    init_state_mult = State([0, 3, 2, 0])
    for line in evaluate(init_state_mult, p_mult, "P mult"):
        print(line, "\\\\")
    print("\\end{align*}\n$$")

    print("\n=== Evaluation trace for 'exp' ===")
    print("$$\n\\begin{align*}")
    init_state_exp = State([0, 2, 3, 0])
    for line in evaluate(init_state_exp, p_exp, "P exp"):
        print(line, "\\\\")
    print("\\end{align*}\n$$")