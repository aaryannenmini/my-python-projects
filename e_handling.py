def divide(a,b):
    try:
        result=a/b
        print(f"result = {result}")
    except ZeroDivisionError:
        print("Error: No NO NO !! WHat are you dividing")


divide(0,9)

print("_____________________________________________________________________________________")

def get_integer():
    while True:
        try:
            num=int(input("Enter number"))
            return num
        except  ValueError:
            print("Boo You")

value=get_integer()
print(f"you entered a {value}")


print("_----_____------------------------------------___----__---___--___---___---___---___---____--______----___----__---____--_____--____--")
def check_age():
    try:
        age=int(input("ENter your age"))
        if(age<0):
            raise ValueError("Age cannot be negetive")
    except ValueError as e:
        print(f"Error: {e}")

check_age()

print("____________-----___----___---____----____---__________----___----____--____----____---____--____---_____---____---____---___----____---____---____---____---____---____----___----____---____---___---____---____----____--____---____")

try:
    answer=int(input("What is 9^3: "))
    if answer == 729:
        print("Answer is correct")
    else:
        print("You are a failure")
except ValueError:
    print("You failed for life")
 

print('__----------_______-------_____------_____----_______------__------------___________________----______-----______-----______-----_____-----_____------_____----------____------_____------____--------____------')



def divide(a,b):
    try:
        result=a/b
        print(f"result = {result}")
    except ZeroDivisionError:
        print("Error: No NO NO !! WHat are you dividing")
    finally:
        print("You and complete are together")


divide(0,9)

divide(0,0)

divide(7,369000000)