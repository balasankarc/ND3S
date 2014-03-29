import inflection
def sentencer(a):
    inpfile = open("text.txt", "r")
    txt = inpfile.read().split("\n")
    i = 0
    rootwordlist = list()
    for i in txt:
        roots = inflection.stem(i)
        rootwordlist[i] = roots
    return rootwordlist
