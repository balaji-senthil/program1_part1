# BOGGLE
Python program that plays Boggle

# Overview of Boggle
Boggle is a board game played on a 5x5 board. Each square of the board contains a letter. Players have 5 minutes to write down
as many words as they can, where a word can be formed using adjacent (up, down, left, right, and diagonal) letters.
No letter can be used more than once.
A player scores points if they write down a word that no other player finds. Four letter words are worth 1 point,
five letter words 2 points, six letter words 3 points, seven letter words 5 points, and a word with eight
or more letters are worth 11 points.

# Overview of the Program
Given a 5x5 board, this Python program prints out all of the words (and their points) contained within the board.
Valid words are given in the `dictionary.txt` file, taken from
[BYU](http://dml.cs.byu.edu/~sburton/cs235/projects/boggle/dictionary.txt). Finally, the Python program prints out
the total number of points one can theoretically obtain, if they found all of the words (and no other player found any).

Sample input can be found in the `boards/` directory. Alternatively, you can input a 5x5 board via `stdin`.

# How to run:
```
# to input a board via stdin:
$ python boggle.py
<input your board here>
# alternatively, pipe an example board to stdin:
$ python boggle.py < boards/board1.txt
```

