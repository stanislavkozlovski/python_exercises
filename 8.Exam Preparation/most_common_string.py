from collections import Counter
import re


user_input = str(input())

most_common = Counter(re.sub("\s+", "", user_input)).most_common(1)

if most_common:
    print(most_common[0][0])
else:
    print("INVALID INPUT")