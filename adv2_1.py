file = open('adv2.txt')

twocount = 0
threecount = 0
used = []

for line in file:
    twocountused=False
    threecountused=False
    for c in line:
        if c not in used:
            i = 0
            count = 0
            while i < len(line):
                if line[i]==c:
                    count+=1
                    i+=1
                else:
                    i+=1
            used.append(c)
            if count==2 and twocountused==False:
                twocount+=1
                twocountused=True
            elif count==3 and threecountused==False:
                threecount+=1
                threecountused=True
    used=[]
    
print(twocount * threecount)