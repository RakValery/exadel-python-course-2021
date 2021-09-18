import re
texts = ["Hello, World!", "The world is mine", "Hello, how are you?"]
liststr = []
for istr in texts:
    istr = re.split(r'[:; ,*.!?\n]+',istr.lower())
    liststr.append(istr)
print("word\t\tcount\tfirst line\n----------------------------------")
i = 0 
for istr in liststr:
    j = 0
    for iword in istr:
        if iword == "":
            j += 1
            continue
        count = 1
        for a in range(i, len(liststr)):
            if (a == i):
                startb = j+1
            else:
                startb = 0
            for b in range(startb, len(liststr[a])):
                if liststr[a][b] == iword:
                    count += 1
                    liststr[a][b] = ""
        j += 1
        print(f"{iword}\t\t{count}\t{i}")
    i += 1