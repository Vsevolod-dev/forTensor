stack = []

while True:
    string = input("Введите текст со скобками: ")
    if string:
        for i in string:     
            # Если в переборе попалась открывающая скобка
            # то добавляем её в стек. 
            if i == "(" or i == "{" or i == "[" or i == "<":
                stack.append(i)

            # Удаляем последнюю скобку из стека, 
            # если предыдущая скобка была открвающая и из той же коллекции. 
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
