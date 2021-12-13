#!/usr/bin/python3
"""Calculates number of times lines intersect"""


def plot_row(plots, x1, y1, y2):
    coord = (x1, y1)
    if y2 > y1:
        for i in range(y1, y2 + 1):
            coord = (x1, i)
            if plots and coord in plots:
                plots[coord] += 1
            else:
                plots[coord] = 1
    else:
        for i in range(y2, y1 + 1):
            coord = (x1, i)
            if plots and coord in plots:
                plots[coord] += 1
            else:
                plots[coord] = 1

    return plots


def plot_column(plots, x1, y1, x2):
    coord = (x1, y1)
    if x2 > x1:
        for i in range(x1, x2 + 1):
            coord = (i, y1)
            if plots and coord in plots:
                plots[coord] += 1
            else:
                plots[coord] = 1
    else:
        for i in range(x2, x1 + 1):
            coord = (i, y1)
            if plots and coord in plots:
                plots[coord] += 1
            else:
                plots[coord] = 1
    return plots


def hydrothermal():
    """Takes input from text file, plots lines given and
    prints number of times lines intersect"""

    # import text files
    with open("input.txt") as f:
        lines = []
        # save sets of coordinates
        for line in f:
            plots = line.split(" -> ")
            lines.append(plots)

    plots = {
        (0, 0): 0
    }
    for line in lines:
        plot_a = line[0].split(',')
        plot_b = line[1].split(',')
        x1 = int(plot_a[0])
        y1 = int(plot_a[1])
        x2 = int(plot_b[0])
        y2 = int(plot_b[1])

        # if x1 = x2 plot line at x
        if x1 == x2:
            print("{0} is row".format(line))
            plots = plot_row(plots, x1, y1, y2)
        # if y1 = y2 plot line of y
        elif y1 == y2:
            print("{0} is column".format(line))
            plots = plot_column(plots, x1, y1, x2)
        else:
            print(print("Skipping {0}".format(line)))

    count = 0
    for v in plots.values():
        if v > 1:
            count += 1
    print(plots)
    print(count)

    # this version uses a matrix. Would it be easier with a dict?

if __name__ == "__main__":
    hydrothermal()