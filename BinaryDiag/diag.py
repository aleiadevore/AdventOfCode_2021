#!/usr/bin/python3
"""gamma bit = most common bit in corresponding position
epsilon bit == least common corresponding bit
output == gamma * epsilon"""


def diag():
    """Naive output with arrays. Go back and use bit manipulation"""
    gamma = []
    epsilon = []
    g = 0
    e = 0
    PlaceCheck = {
        0: 0,
        1: 0
    }

    with open("input.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)

    for i in range(0, 12):
        for j in range(0, len(lines) - 1):
            if int(lines[j][i]) == 0:
                PlaceCheck[0] += 1
            else:
                PlaceCheck[1] += 1
        if PlaceCheck[0] > PlaceCheck[1]:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)
        PlaceCheck[0] = 0
        PlaceCheck[1] = 0
    print("Gamma: {0}".format(gamma))
    print("E: {0}".format(epsilon))

    for bit in gamma:
        g = (g << 1) | bit
    for bit in epsilon:
        e = (e << 1) | bit

    print(g * e)

# power = gamma * epsilon

if __name__ == "__main__":
    diag()
