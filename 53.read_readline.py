with open('.\\text.txt') as f:
   
    while True:
        content = f.readline()
        if content:
            print(content)
        else:
            break
        