#calculator for the 3 signs

#multiplication
def mult():
    m = int(input("Input the first value: "))
    m2= int(input("Multiply by?: "))
    ans = m * m2
    print("your answer is: {ans}")
def plus():
    m = int(input("Input the first value: "))
    m2= int(input("Adding with?: "))
    ans = m + m2
    print("your answer is: {ans}")

def sub():
    m = int(input("Input the first value: "))
    m2= int(input("Subtracting ?: "))
    ans = m - m2
    print("your answer is: {ans}")
def div():
    m = int(input("Input the first value: "))
    m2= int(input("Divided by?: "))
    ans = m / m2
    print("your answer is: {ans}")


mult()
sub()
plus()
div()
