from curses import ALL_MOUSE_EVENTS


def numberMatchesMath(l, s):
    matches = (l)/s/5
    # check if float
    if matches % 1 != 0:
        matches = int(matches) + 1
    return matches

def numberMatchesNoMath(l, s):
    matches = 0
    distancetraveled = 0
    while distancetraveled < l:
        pass
    return matches


l = 250
s = 110
s = s/100
out = numberMatchesMath(l, s)
#out2 = numberMatchesNoMath(l, s)
print(out)
#print(out2)