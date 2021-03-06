'''
Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
'''

def computegrade (score) :
    if score < 0.0 :
        print('Error, number is too small')
        quit()
    elif fscore > 1.0 :
        print('Error, number is too big')
        quit()
    elif score >= 0.9 : return 'Grade: A'
    elif score >= 0.8 : return 'Grade: B'
    elif score >= 0.7 : return 'Grade: C'
    elif score >= 0.6 : return 'Grade: D'
    elif score < 0.6 : return 'Grade: F'

iscore=input('Enter a score between 0.0 and 1.0: ')
try:
    fscore=float(iscore)
except:
    print('Error, enter number between 0.0 and 1.0')
    quit()

result = computegrade(fscore)
print(result)
