file = open('adv2.txt')
lines = file.read().splitlines()
i=1
for line in lines:
    while i < len(lines):
        count=0
        q = lines[i]
        j=0
        print("new word")
        while j < len(line):
            print(line[j])
            print(q[j])
            if line[j]!=q[j]:
                count+=1
                line = line.replace(line[j],'',1)
                q = q.replace(q[j],'',1)
                j-=1
            j+=1
        if count==1:
            print(line)
            print(q)
        i+=1