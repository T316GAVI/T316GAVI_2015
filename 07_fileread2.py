
f = open('randomtext.txt','r')

t = f.readlines()


print(t)
print('--------')

for i in range(len(t)):
    t[i] = t[i].lstrip().rstrip('\n')

print(t)
print('----------')

thetext = ' '.join(t)

print(thetext)

words = thetext.split()

print(type(words))
print(len(words))
print(words)
print()
f.close()