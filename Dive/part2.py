#!/usr/bin/python
"""Given input calculates horizontal and depth position, multiplies together
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X."""


def dive():
    # import input
    hor = 0
    depth = 0
    aim = 0

    with open("input.txt") as file_in:
        for line in file_in:
            # split by space
            words = line.split(" ")

            # if word[0] == forward, back, etc
            direction = words[0]
            n = int(words[1])

            if direction == "forward":
                hor += n
                depth += n * aim
            if direction == "down":
                aim += n
            if direction == "up":
                aim -= n
            print("Aim: {0}, hor: {1}, depth: {2}".format(aim, hor, depth))
    print(hor * depth)


if __name__ == "__main__":
    dive()
