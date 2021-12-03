#!/usr/bin/python
"""Given input calculates horizontal and depth position, multiplies together"""


def dive():
    # import input
    x = 0
    y = 0

    with open("input.txt") as file_in:
        for line in file_in:
            # split by space
            words = line.split(" ")

            # if word[0] == forward, back, etc
            direction = words[0]
            n = int(words[1])

            if direction == "forward":
                x += n
            if direction == "down":
                y += n
            if direction == "up":
                y -= n
    print(x * y)


if __name__ == "__main__":
    dive()
