import re
texts = ["Hello, World!", "The world is mine", "Hello, how are you?"]
dictw = {}
for i, istr in enumerate(texts):
    for iword in re.split(r'[:; ,*.!?\n]+',istr.lower()):
        if iword == "":
            continue
        if iword not in dictw:
            dictw[iword] = [1, i]
        else:
            dictw[iword][0] += 1
print("word\t\tcount\tfirst line\n----------------------------------")
for iword, (count, line) in dictw.items():
    print(f"{iword}\t\t{count}\t{line}")