
def message():
    print("This is a message")
    print("in a simple function")

def sum(a,b):
    result = a + b
    return result

def get_two_numbers():
    num1 = int(input("write a number: "))
    num2 = int(input("write another number: "))
    return num1,num2


print('hi!')
message()

#x = int(input("First number: "))
#y = int(input("Second number: "))
x,y = get_two_numbers()

z = sum(x,y)
print(z)

x = input("First text: ")
y = input("Second text: ")

z = sum(x,y)
print(z)