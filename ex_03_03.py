'''
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.
If the score is between 0.0 and 1.0, print a grade using the following table:

    Score   Grade
   >= 0.9     A
   >= 0.8     B
   >= 0.7     C
   >= 0.6     D
    < 0.6     F

   Enter score: 0.95
   A

   Enter score: perfect
   Bad score

   Enter score: 10.0
   Bad score

   Enter score: 0.75
   C

   Enter score: 0.5
   F
'''

score=input('Enter a score between 0.0 and 1.0: ')
try:
    fscore=float(score)
except:
    print('Error, enter number between 0.0 and 1.0')
    quit()

if fscore < 0.0 :
    print('Error, number is too small')
    quit()
elif fscore > 1.0 :
    print('Error, number is too big')
    quit()
else :
    if fscore >= 0.9 : print('Grade: A')
    elif fscore >= 0.8 : print('Grade: B')
    elif fscore >= 0.7 : print('Grade: C')
    elif fscore >= 0.6 : print('Grade: D')
    elif fscore < 0.6 : print('Grade: F')
