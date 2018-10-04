basic="""+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +"""
print(basic)

def print_grid(n):
    def plus():
        print("+", end=" ")
        print("- "*(n//2), end="")
        print("+", end=" ")
        print("- "*(n//2), end="")
        print("+")
    def body():
        if n%2==0:
            for i in range(n//2):
                print ("|", end=" ")
                print (" "*(n), end="")
                print ("|", end=" ")
                print (" "*(n),end="")
                print ("|")
        else:
             for i in range(n//2):
                print ("|", end=" ")
                print (" "*(n-1), end="")
                print ("|", end=" ")
                print (" "*(n-1),end="")
                print ("|")
    plus()
    body()
    plus()
    body()
    plus()

def print_grid2(a,b):
    def plus():
        for i in range(a):
            print("+", end=" ")
            print("- "*(b), end="")
        print("+")
    def body():
        for x in range(b):
            for i in range(a):
                print ("|", end=" ")
                print (" "*(b*2), end="")
            print ("|")
    for i in range(a):
        plus()
        body()
    plus()
