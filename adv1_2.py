file = open('advent1.txt')
lines = file.read().splitlines()

freq = 0
sf = [0]
i = 0

while i < len(lines):
    freq+=int(lines[i])
    if freq in sf:
        print('Duplicate freq: ' + str(freq))
        break
    else:
        sf.append(freq)
    i+=1
    if i == len(lines):
        i = 0

    