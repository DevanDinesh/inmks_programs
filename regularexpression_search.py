import re
pattern="python"
if re.search(pattern,"hello am python"):
    print("matched")
else:
    print("not matched")