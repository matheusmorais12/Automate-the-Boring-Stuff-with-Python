#Return Values and return statements

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Is is certain'
    elif answerNumber == 2:
        return 'It is decidedly'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook hot so good'
    elif answerNumber == 9:
        return 'Very doubtful'

print(getAnswer(random.randint(1,9)))
