#calculator for the 3 signs
import keyboard
#multiplication
def mult():
    m = int(input("Input the first value: "))
    m2= int(input("Multiply by?: "))
    ans = m * m2
    print("your answer is: ",ans)
def plus():
    m = int(input("Input the first value: "))
    m2= int(input("Adding with?: "))
    ans = m + m2
    print("your answer is: ",ans)

def sub():
    m = int(input("Input the first value: "))
    m2= int(input("Subtracting ?: "))
    ans = m - m2
    print("your answer is: ",ans)
def div():
    m = int(input("Input the first value: "))
    m2= int(input("Divided by?: "))
    ans = m / m2
    print("your answer is: ",ans)
    
print("\nChoose Your arithmetic Expression\n----------------------------\n\t You can choose from the following\n ")
print("'a':- for addition\n'b':- for division\n'm':- for multiplication\n's':- for substraction")

while True:

    me = input("Which arithmetic expression will you like to use?: ")
    if me == 'a':
        plus()
    elif me == 'm':
        mult()
    elif me == 'd':
        div()
    elif me == 's':
        sub()
        
    else:
        break
    ending = input("Will you like to continue?y/n: ")
    if ending=='y':
        continue
    else:
        break
