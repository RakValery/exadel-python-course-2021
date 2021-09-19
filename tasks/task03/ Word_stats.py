import re
texts = ["Hello, World!", "The world is mine", "Hello, how are you?"]
dictw = {}
i = 0
for istr in texts:
    for iword in re.split(r'[:; ,*.!?\n]+',istr.lower()):
        if iword == "":
            continue
        if dictw.get(iword, "e404") == "e404":
            dictw[iword] = [1, i]
        else:
            dictw[iword][0] += 1
    i += 1
print("word\t\tcount\tfirst line\n----------------------------------")
for iword in dictw.keys():
    print(f"{iword}\t\t{dictw.get(iword)[0]}\t{dictw.get(iword)[1]}")