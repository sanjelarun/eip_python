def RPN_evaluate(expression):
    delimt = ","
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: y - x,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: int(x / y)}
    current_stack = []
    cnt = 0
    operator = ""
    for token in expression.split(delimt):
        if cnt == 2 and token in operators:
            current_stack.append(operators[operator](int(current_stack.pop()), int(current_stack.pop())))
            cnt = 1
            operator = token
        elif token in operators:
            operator = token
        else:
            current_stack.append(token)
            cnt += 1
        print(current_stack)
    # LAST CHECK
    if cnt == 2:
        current_stack.append(operators[operator](int(current_stack.pop()), int(current_stack.pop())))

    return current_stack[0]

s = "/,3,1,*,7,+,12"
print(RPN_evaluate(s))