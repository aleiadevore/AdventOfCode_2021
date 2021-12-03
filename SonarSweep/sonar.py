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
old = 0
for i in range(0, len(lines) - 1):
    if int(lines[i]) > old:
        count += 1
    old = int(lines[i])

# print final answer
print(count)