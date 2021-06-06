# 3x3-Grid-Puzzle-Solver


Problem A
This is a logic puzzle in which you have a square grid of 33 cells. Each cell is initially either white or black. When you click on a square it flips, or toggles, the color of that square and the colors of its four immediate north, south, east and west neighbors that exist (they don’t exist if they would be outside the grid).

The problem is to find the minimum number of cell clicks to transform a grid of all white cells into the input grid (which is always possible). You cannot rotate the grid.

![Screenshot_67](https://user-images.githubusercontent.com/50110758/120938922-f5fe6100-c71d-11eb-8327-224bccc409a2.png)

Figure 1: The two sample problems
Input
The first value in the input file is an integer  on a line by itself giving the number of problems to solve.

For each of the  problems, 3 lines of 3 characters describe the input grid. The characters in the grid descriptions are ‘*’ (for black) and ‘.’ (for white).

Output
For each problem output a single integer giving the minimum number of clicks necessary to transform a grid of all white cells into the pattern given in the input.

Sample Input 1	Sample Output 1
2
*..
**.
*..
***
*..
..*
1
3
![Screenshot_68](https://user-images.githubusercontent.com/50110758/120938965-27772c80-c71e-11eb-827f-d2d64ab9e18f.png)



Author
Ivor Page
