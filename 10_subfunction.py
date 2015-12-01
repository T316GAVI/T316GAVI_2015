
def fun1(x):
    def subfun1(a,b):
        return a**b

    def subfun2(sometext):
        for ch in sometext:
            print(ch)

    if x == 1:
        return subfun1
    else:
        return subfun2

a = fun1(1)
print(a(2,3))

a = fun1(0)
a('Testing')
