
f = open('randomtext.txt','r')

t = f.readlines()


print(t)
print('--------')

for i in range(len(t)):
    t[i] = t[i].strip()

print(t)

f.close()