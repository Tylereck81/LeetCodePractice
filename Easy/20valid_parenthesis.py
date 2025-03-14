def isValid(s: str) -> bool: 
    stack = []
    for i in range(len(s)): 
        stack.append(s[i])
        if len(stack)-1 >= 0:
            top = stack[len(stack)-1]
        else: 
            top = 0
        if s[i] == ')'  and top== '(':
            stack.pop()
            stack.pop()
        elif s[i] == ']' and top== '[': 
            stack.pop()
            stack.pop()
        elif s[i] == '}' and top == '{': 
            stack.pop()
            stack.pop()
        
    return (len(stack) == 0)

print(isValid("([)"))