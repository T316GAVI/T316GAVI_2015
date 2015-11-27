
def message():
    print("This is a message")
    print("in a simple function")

def sum(a,b):
    result = a + b
    return result


print('hi!')
message()

x = int(input("First number: "))
y = int(input("Second number: "))

z = sum(x,y)
print(z)

x = input("First text: ")
y = input("Second text: ")

z = sum(x,y)
print(z)