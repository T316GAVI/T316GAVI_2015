
f = open('randomnumbers.txt','r')

t = [0]*6

for x in f:   # x is a line in the file f
    value = int(x)

    t[value-1] += 1

f.close()

for i in range(6):
    print('The value {} appears {} times'.format(i+1, t[i]))