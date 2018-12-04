import re

file = open('adv4.txt')

logs = []
unique_ids = []
guard_sleep_totals = []

class guard_log:
    def __init__(self,id,time,minutes,awake):
        self.id=id
        self.time=time
        self.minutes=int(minutes)
        self.awake=awake
    
    def toString(self):
        print('Id: ' + str(self.id) + ', Time: ' + str(self.time) + ', Minutes: ' + str(self.minutes) + ', Awake: ' + str(self.awake))

class guards_total:
    def __init__(self, id, time):
        self.id=id
        self.time=time

    def toString(self):
        print('Id: ' + str(self.id) + ', time: ' + str(self.time))

def isAwake(text):
    if 'asleep' in text:
        return False
    else:
        return True

def fetchId(text):
    if '#' in text:
        id = re.search('#(\\d{1,4})',text).group(1)
        if id not in unique_ids:
            unique_ids.append(id)
    elif not logs:
        id = 0
    else:
        id = logs[-1].id
    return id

def guard_logs(file):
    for line in file:
        id = fetchId(line)
        time = re.search('(\\d{4}-\\d{2}-\\d{2}\\ \\d{2}:\\d{2})',line).group(1)
        minutes = re.search(':(\\d{2})',line).group(1)
        awake = isAwake(line)
        logs.append(guard_log(id,time,minutes,awake))

def calculate_total_time_asleep_per_guard(id):
    time=0
    for row in logs:
        if row.id==id:
            if time==0:
                time=row.minutes
            if not row.awake:
                time+=row.minutes
            else:
                time-=row.minutes
    guard_sleep_totals.append(guards_total(id,abs(time)))

guard_logs(file)
logs.sort(key=lambda r: r.time)
for id in unique_ids:
    calculate_total_time_asleep_per_guard(id)

guard_sleep_totals.sort(key=lambda r: r.time)
for x in guard_sleep_totals:
    print(x.toString())