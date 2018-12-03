file = open('adv1.txt')

freq = 0

for line in file:
    freq += int(line)

print(freq)