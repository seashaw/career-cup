#!/usr/bin/env python3
"""
http://www.careercup.com/question?id=5160106813554688

N queen problem. 

In NXN chess board, you have to arrange N queens such that they do not
interfere each other. Following is how you define interference of queens:

1. Two queens cannot be on the same diagonal
2. Two queens cannot be in same horizontal or vertical line
3. Queen can jump like a knight. So, two queens cannot be at a position where
   they can jump two and half steps like a knight and reach the other queen.

You should return the possible ways to arrange N queens on a chess board.

This was a tech screen, but since I was local, they called me in their
office rather than phone interview. 

Hint: Don't try too hard, the best solution is n!

Return the number of solutions possible.

I should try to solve as a regular n queens problem, and then modify to find
solutions that incorporate knight movements.
"""

class nQueensBruteForce():
    """
    Brute force approach to finding number of solutions for n queens problems.
    """
    def __init__(self, N):
        self.N = N
        self.rows = []
        self.cols = []

    def checkPosition():
        """
        Takes given coordinates and checks.
        """
        is_valid = True
        for queen_one in range(0, self.N):
            for queen_two in range(queen_one+1, self.N):
                if self.rows:
                    # do this...
