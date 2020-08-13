def evalRPN(tokens):
        stack = []
        
        operators = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "/": lambda a,b: int(a/b),
            "*": lambda a,b: a*b
        }
        
        for t in tokens:
            if t in operators:
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(operators[t](num_1, num_2))
            else:
                stack.append(int(t))
                
        return stack[0]
        
