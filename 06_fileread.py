
f = open('randomtolur.txt','r')

t = [0]*6

for x in f:   # x is a line in the file f
    print('-----------')
    type(x)
    print('"{}"'.format(x))


f.close()
