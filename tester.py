import re

ALAN_MENTION_REGEX = "[^a-zA-Z](alan)[^a-zA-Z]|^(alan)[^a-zA-Z]"

text = "fuck you alan"

result = re.search(ALAN_MENTION_REGEX, text, re.IGNORECASE)

if result:
    print("yes")
else:
    print("no")
