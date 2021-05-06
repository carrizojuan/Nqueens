# Nqueens
https://www.reddit.com/r/dailyprogrammer/comments/ab9mn7/20181231_challenge_371_easy_n_queens_validator/

For the purpose of this challenge, the N queens problem consists of putting one queen on every column (labeled a, b, c, ...) of an NxN chessboard, such that no two queens are in the same row or diagonal. An example valid solution for N = 6 is:

6  . . Q . . .
5  . . . . . Q
4  . Q . . . .
3  . . . . Q .
2  Q . . . . .
1  . . . Q . .
   a b c d e f
In chess notation, the squares with queens in this solution are called a2, b4, c6, d1, e3, and f5. We'll represent solutions by listing the rows that each column's queen appears in from left to right, so this solution is represented as the array {2, 4, 6, 1, 3, 5}.

Solving the N queens problem was #25 (difficult) on r/dailyprogrammer, but you don't need to actually solve it for today's challenge.

Challenge
Given an array of 8 integers between 1 and 8, determine whether it represents a valid 8 queens solution.

qcheck({4, 2, 7, 3, 6, 8, 5, 1}) => true
qcheck({2, 5, 7, 4, 1, 8, 6, 3}) => true
qcheck({5, 3, 1, 4, 2, 8, 6, 3}) => false   (b3 and h3 are on the same row)
qcheck({5, 8, 2, 4, 7, 1, 3, 6}) => false   (b8 and g3 are on the same diagonal)
qcheck({4, 3, 1, 8, 1, 3, 5, 2}) => false   (multiple problems)
You may optionally handle solutions for any N, not just N = 8.
