
f = open('randomtext.txt','r')

t = f.read()


print(t)
print('--------')
print(type(t))
print(len(t))

f.close()