# Assignments

A collection of solutions I made for interview assignments (i.e., problems I could do on my own time and not during the interview).


### Permutation Assignment

This assignment was given to me well over a decade ago.  I was interviewing for a healthcare company, but I can't recall now who it was.  The position was for a software engineer (developer).  While I still have the code for my solution, I no longer have the specific requirements for the assignment.  I vaguely recall it had to run in under 1-2 seconds (I'm thinking it was 1 second) and use no more than 1GB of memory.  It could be written in any programming language I wanted and there was no time line to complete it.  The assignment was to create a program that would take in a string of uppercase English letters (only A-Z) and determine how many permutations there are - with a twist (which I can't remember what the twist was).  The string could be of any size from 1 character to 25 characters and the characters could repeat.  The program would then output the string followed by "=" and then the number.  Here are some examples:

| Input      | Output             |
| ---------- | ------------------ |
| DCBA       | DCBA = 24          |
| QUESTION   | QUESTION = 24572   |
| BOOKKEEPER | BOOKKEEPER = 10743 |
| BAAA       | BAAA = 4           |

One thing I do remember is I had to reread the assignment a bunch of times, because I just couldn't understand exactly what it was wanting me to do.  But once it finally clicked I think I finished it rather quickly (certainly less than a day).  I also create a test case for it, which I managed to keep as well (and included here).  The test case was not part of the requirement, but I went ahead and submitted it along with the original program.  I think I got a call or email a few days after submitting it that they accepted it and wanted me to come in for some face-to-face interviews.  I ended up declining the interviews because I had gotten a really good offer at another company.  To this day I always feel this was one of the better programming challenges I had been given.  I'm not very partial to programming challenges where you have to figure out a solution (or as close to one as you can) while being interviewed.  It always makes me a little more nervous.

[HERE](https://github.com/stpride/challenges/blob/main/assignments/001/exercise.py) is the code for the original program, and [HERE](https://github.com/stpride/challenges/blob/main/assignments/001/test_exercise.py) is the test case code.
