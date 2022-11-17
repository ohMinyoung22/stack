from stack import Stack
n = input("명령행 숫자")

stack = Stack(100000)
    
for i in range(0, int(n)):
    ops_list = input().split()
    
    operator = ""
    operand = -1
    
    if len(ops_list) == 1:
        operator = ops_list[0]
    elif len(ops_list) == 2:
        operator = ops_list[0]
        operand = ops_list[1]
        operand = int(ops_list[1])
    
    if operator == "push":
        stack.push(operand)
    elif operator == "top":
        print(stack.check())
    elif operator == "size":
        print(stack.count())
    elif operator == "empty":
        if stack.count() > 0:
            print("0")
        else:
            print("1")
    elif operator == "pop":
        print(stack.pop())