
name = input("Hi, what is your name? ")

year = int(input("What year is it? "))
pi = float(input("What is PI? "))

print("Hi {}, welcome to gagnavinnsla".format(name))
print("Year is {} and pi = {}".format(year,pi))

if year < 2015:
    print("{} is not correct")
    print("you are off by {}".format(2015-year))
    print("thank you!")
elif year > 2015:
    print("The future!")
else:
    print('ok')

