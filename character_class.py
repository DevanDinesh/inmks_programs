import re
pattern="[a-z][0-9][a-z]"
if re.search(pattern,"pBu"):
    print("matched")
else:
    print("not matched")