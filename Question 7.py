'''
Draw Arrow Trail from Movement Deltas
A movement delta is the change from the current position to the next position.

Given a sequence of non-zero integers representing movement deltas, draw arrows representing each movement as described below.

Starting with current position as 0, for each number in the input:

Positive value v: draw a rightward arrow =====> of length v starting from the current position.
Negative value -v: draw a leftward arrow <==== of length v, ending at the current position.
Zero: draw a = at the current position.
Assume that the current position will be always greater than or equal to zero.

Arrows are made using:

'=' repeated v times
'>' for right arrow (ends with >)
'<' for left arrow (starts with <)
Each arrow should be drawn on a new line, aligned based on the cumulative position as described.

Note:

The starting position is index 0.
After printing each arrow, update the position by adding the delta value to it.
Sample Input

1 4 -2 5 0 -3 0 -3 1 4
Sample Output

=>
 ====>
   <==
   =====>
        =
     <===
     =
  <===
  =>
   ====>
'''
