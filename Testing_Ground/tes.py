flag = True

for i in range(1, 6):
    if flag:
        print("Hello")
        flag = False
    if not flag:
        print("Bye")