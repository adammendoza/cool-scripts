import random
runs = int(1000)
changed = 0
unchanged = 0
doorchoices = [0,1,2]
for x in range(runs):
    prize = random.choice(doorchoices)
    picked = random.choice(doorchoices)
    goats = set(doorchoices) - set([prize])
    remaining = set(doorchoices) - set([picked])
    opened = random.choice(list(goats.intersection(remaining)))
    if picked == prize:
        unchanged = unchanged + 1
    newchoice = (set(doorchoices) - set([picked]) - set([opened])).pop()
    if newchoice == prize:
        changed = changed + 1
print("{0} unchanged {1:.1f}% ".format(unchanged, unchanged / float(runs) * 100.0))
print("{0} changed {1:.1f}% ".format(changed, changed / float(runs) * 100.0))
