import re

file = open('adv3.txt')
claims = []
claim_area = []
claim_count = []

class Claim:
    def __init__(self,id,xin,yin,xlen,ylen):
        self.id=id
        self.xin=xin
        self.yin=yin
        self.xlen=xlen
        self.ylen=ylen

    def toString(self):
        print('Id: ' + self.id +', Xin: ' + str(self.xin) + ', Yin: ' + str(self.yin) + ', Xlen: ' + str(self.xlen) + ', Ylen: ' + str(self.ylen))

def create_claim_list(file):
    for line in file:
        id=re.search('#([0-9]{1,4})',line).group(1)
        xin=int(re.search('@\\ ([0-9]{1,4})',line).group(1))
        yin=int(re.search(',([0-9]{1,4})',line).group(1))
        xlen=int(re.search(':\\ ([0-9]{1,4})',line).group(1))
        ylen=int(re.search('x([0-9]{1,4})',line).group(1))
        claims.append(Claim(id,xin,yin,xlen,ylen))
        claim_area.append(0)
        claim_count.append(0)

def create_fabric():
    fabric=[['.' for i in range(1000)] for j in range(1000)]
    return fabric

def place_claim(claim, fabric):
    for x in range(claim.xin,claim.xin+claim.xlen):
        for y in range(claim.yin,claim.yin+claim.ylen):
            if fabric[y][x]=='.':
                fabric[y][x]=str(claim.id)
            else:
                fabric[y][x]='X'
    return fabric

create_claim_list(file)
fabric = create_fabric()
count=0
for claim in claims:
    claim_area[int(claim.id)-1]=claim.xlen*claim.ylen
    fabric = place_claim(claim, fabric)

for claim in claims:
    for i in range(1000):
        for j in range(1000):
            if fabric[j][i]==claim.id:
                claim_count[int(claim.id)-1]+=1

for i in range(len(claim_area)):
    if claim_count[i]==claim_area[i]:
        print(i+1)