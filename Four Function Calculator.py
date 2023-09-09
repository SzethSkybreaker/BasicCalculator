x=0
while x==0:
    y = int(input("Enter [1] to multiply, [2] to divide, [3] to add, and [4] to subtract, or [5] to exit"))
    if (y == 5):
        break
    elif (y == 1):
        a, b = input("Input two values multiply: ").split()
        print(int(a)*int(b))
    elif (y == 2):
        a, b = input("Input two values to divide: ").split()
        print(int(a)/int(b))
    elif (y == 3):
        a, b = input("Input two values to add: ").split()
        print(int(a) + int(b))
    elif (y == 4):
        a, b = input("Input two values to subtract: ").split()
        print(int(a) - int(b))
    else:
        print("Invalid input. Please enter 1, 2, 3, 4, or 5")