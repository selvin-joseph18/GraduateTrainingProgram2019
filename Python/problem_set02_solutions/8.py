def eval_loop():
     result=''
     while (True):
        expr = input("enter a expression: ")
        if expr.lower()=='done':
            break
        else:
            result = eval(expr)
            print(result)

     print(result)

eval_loop()