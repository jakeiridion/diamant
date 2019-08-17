print("Enter the size of the diamond!")
while True:
    ko = input("> ")
    if ko == "exit" or ko == "e" or ko == "quit" or ko == "stop":
        print("Bye Bye!")
        break
    scan = int(ko) / 2
    scan = scan + 0.5
    size = int(scan)
    test = 3
    letzter = int(size) * 2 - 1
    u = int(size) - 1
    x = int(letzter / 2 - 0.5)

    q = int(size) * 2 - 1
    w = 2
    t = q-w

    for i in range(u):
        print(" ", end="")
    print("*")

#obere Hälfte des Diamanten von "tannenbaum.py"
    for i in range(u):
        for i in range(u - 1):
            print(" ", end="")
            if i == u - 2:
                u = u - 1

        for i in range(test):
            print("*", end="")
            if i == test - 1:
                print("")

            if i == test - 1:
                test = test + 2

#Falls Der input gerade ist wird noch eine mitte eingefügt:
    if int(ko) % 2 == 0:
        print("*" * letzter,end="")
        print("")

#Untere hälfte des Diamanten:
    for i in range(size-1):
        print(" " * u,end="")
        for i in range(t):
            print("*",end="")
            if i == (t - 1):
                t = t - 2
        print("")
        u = u + 1
    print("")