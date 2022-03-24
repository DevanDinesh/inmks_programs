import re
pattern="python"


if re.match(pattern,"helloworld python how are you"):
    print("matched")
else:
    print("Not matched")