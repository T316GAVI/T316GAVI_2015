
f = open('randomtext.txt','r')

t = f.readlines()


print(t)
print('--------')
print(type(t))
print(len(t))
print(len(t[0]))

f.close()