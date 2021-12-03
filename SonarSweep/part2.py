#!/usr/bin/python3

# use dict to += Letter: value
# use letter instead of number so it can be incremented indefinitely
# don't use dict. Check list[i] + list[i + 1] + list[i + 2], make sure all exist
# comapare to prev

#!/usr/bin/python3

# declare count
from typing import Counter


count = 0

# import input
with open("input") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)

# parse through lines and increment count if l2 > l1
old = 999999
current = 0
for i in range(0, len(lines) - 1):
    if (i + 2 < len(lines)):
        current = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
    else:
        break
    if current > old:
        count += 1
    old = current

# print final answer
print(count)