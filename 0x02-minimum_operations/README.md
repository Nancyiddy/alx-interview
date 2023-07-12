# 0x03-minimum_operations
For this interview practice algorithm, there is a text file with a single character.  The text editor can only execute two operations: Copy All and Paste.

[0. Minimum Operations](/0x03-minimum_operations/0-minoperations.py)
* Given a number `n`, write a method that calculates the fewest number of operation needed to result in exactly `n` characters in the file.
  * Example: `n` = 9
    * C => Copy All => Paste => CC => Paste => CCC => Copy All => Paste => CCCCCC => Paste => CCCCCCCCC
    * Number of operations = 6
  * `n` is the number of times the character should be repeated.
  * returns the fewest number of operations needed or 0 if n is impossible

### test_files
The test_files/ directory contains files used to test the output of the algorithm locally.
