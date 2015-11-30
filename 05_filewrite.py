import random

f = open('randomnumbers.txt','a')

for i in range(100):
    a = random.randint(1,6)
    f.write('{}\n'.format(a))


f.close()