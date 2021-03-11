stack = []

while True:

    string = input("Введите текст со скобками: ")
    if string:
        for i in string:        
            if i == "(" or i == "{" or i == "[" or i == "<":
                stack.append(i)

            if i == ")":
                stack.pop() if stack[len(stack) - 1] == '(' else print('ошибка')
        
            if i == "}":
                stack.pop() if stack[len(stack) - 1] == '{' else print('ошибка')
                    
            if i == "]":
                stack.pop() if stack[len(stack) - 1] == '[' else print('ошибка')
                    
            if i == ">":
                stack.pop() if stack[len(stack) - 1] == '<' else print('ошибка')
                    
        print("true" if len(stack) == 0 else "false")

    else: 
        break
