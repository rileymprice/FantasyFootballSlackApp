import re
import os

ALAN_MENTION_REGEX = "[^a-zA-Z](alan)[^a-zA-Z]|^(alan)[^a-zA-Z]|[^a-zA-Z](alan)"
# ALAN_MENTION_REGEX = "[^a-zA-Z](alan)"

sentence_text = "fuck you alan."
starter = "alan fuck"
mid_alan = "fuck alan cuckold"
non_alan = "dkjf avalanche dskfjdf"
cap_alan = "ALAN kdjf"
camel_alan = "dsfdf Alan dkjfdf"
weird_alan = "aLaN ksjdfkdf"

result = re.search(ALAN_MENTION_REGEX, sentence_text, re.IGNORECASE)
result2 = re.search(ALAN_MENTION_REGEX, starter, re.IGNORECASE)
result3 = re.search(ALAN_MENTION_REGEX, mid_alan, re.IGNORECASE)
result4 = re.search(ALAN_MENTION_REGEX, non_alan, re.IGNORECASE)
result5 = re.search(ALAN_MENTION_REGEX, cap_alan, re.IGNORECASE)
result6 = re.search(ALAN_MENTION_REGEX, camel_alan, re.IGNORECASE)
result7 = re.search(ALAN_MENTION_REGEX, weird_alan, re.IGNORECASE)

assert result
assert result2
assert result3
assert not result4
assert result5
assert result6
assert result7


if result:
    print("yes")
else:
    print("no")
