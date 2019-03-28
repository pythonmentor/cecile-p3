# -tc- Transférer le code ci-dessous dans une classe

#class laby:
#    pass

laby = []
row = 15
col = 15
value = 0

for line in range(row):
    laby.append([])
    for column in range(col):
        value += 1
        laby[line].append(value)

for element in laby:
    print (element)

input()
