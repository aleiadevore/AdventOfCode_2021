#!/usr/bin/python3
"""Marks off bingo boards and checks for completed row or column
Score of winning board calculated by finding sum of all unmarked
multiplied by the winning number"""


def checkBoard(board):
    """Checks board for win"""
    pass


def makeBoards(vals):
    """Takes list of strings representing boards, converts into
    list of matrices of ints"""
    boards = []

    for str in vals:
        lines = str.split('\n')
        board = []
        for line in lines:
            nums = line.split(' ')
            newNums = []
            for num in nums:
                try:
                    newNums.append(int(num))
                except:
                    continue
            print(len(newNums))
            board.append(newNums)
        boards.append(board)
    boards.pop(len(boards) - 1)

    return boards


def setUp():
    """Input format:
    First line is numbers to be called
    Next are 5x5 matrices split by blank lines"""

    with open("input.txt") as f:
        lines = f.read()
        numbers = lines[0]
        """Make list of matrices"""
        out = lines.split("\n\n")
        out.pop(0)
        boards = makeBoards(out)

    for board in boards:
        # checkBoard(board)
        print(board)

if __name__ == "__main__":
    setUp()
