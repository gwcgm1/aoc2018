file = open('adv2.txt')
lines = file.read().splitlines()
i=1
for line in lines:
    i=lines.index(line)+1
    while i < len(lines):
        count=0
        q = lines[i]
        s = lines[i]
        j=0
        while j < len(line):
            if line[j]!=q[j]:
                count+=1
                s = s[:j] + s[j+1:]
            j+=1
        if count==1:
            print(line)
            print(q)
            print(s)
        i+=1