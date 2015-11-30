
f = open('randomtext.txt','r')

t = f.readlines()


print(t)
print('--------')

for i in range(len(t)):
    t[i] = t[i].lstrip().rstrip('\n')

print(t)
print('----------')

print(' '.join(t))

print()
f.close()