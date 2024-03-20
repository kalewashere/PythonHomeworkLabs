"""Write a quiz function that takes two arguments - one quiz question and the question's correct answer.

In your quiz function, you will print the question, and ask the user for the answer. If the user gets the answer
correct, print a success message. Else, print a message with the correct answer.   Your function does not need to
return anything.

Create a main function. From your main function, call your quiz function twice. So your program will ask the user one
question, verify the answer, ask the user another question, verify that answer. Here's some suggestions for questions
and their answers,

Q: Which planet is closest to the sun?  A: Mercury
Q: Who painted the Mona Lisa? A: Leonardo da Vinci"""


# answer_1 = input('What is the capital of Japan? ')

# if answer_1.upper() != 'TOKYO':
#    print('Incorrect. The capital of Japan is Tokyo. ')
# else:
#    print(f'Correct! Next question.')

# answer_2 = input('What is the capital of Minnesota? ')

# if answer_2.upper() != 'ST PAUL':
#    print('Incorrect. The capital of Minnesota is St. Paul')
# else:
#    print('Correct!')

# I realize after some feedback this is not what the assignment asked for. If and else statements may get program to
# run, but the assignment called for functions. Updates for quiz_function is as follows!

def main():  # Main function. defined all variables here for both questions and answers.
    question1 = 'What is the capital of Japan?'
    answer1 = 'Tokyo'
    quiz(question1, answer1)
    question2 = 'What is the capital of Hawaii?'
    answer2 = 'Honolulu'
    quiz2(question2, answer2)


def quiz(question1, correct_answer): # Def function for first question.
    user_answer = input(question1)
    if user_answer.lower() == correct_answer.lower(): # .lower() for mistypes in capitalization.
        print(f'Correct!')

    else:
        print(f'Incorrect. The correct answer is {correct_answer}.') # favortie f' strings for entering correct
        # answer if user answered incorrectly.


def quiz2(question2, answer2):  # function for second question. I initially tried to def in the other def function
    # but the program would not recognize one in the other. Unless i typed it incorrectly, it was easier/only able to
    # run by putting question2 on its own line/in its own sections
    user_answer2 = input(question2) # made some new variables
    if user_answer2.lower() == answer2.lower(): # .lower() for case sensitivity
        print('Correct!')
    else:
        print(f'That is incorrect. The correct answer is {answer2}')


main() # calling main function. will not run without this line. However, I was not able to get the quiz to stop if
# the first questrion was answered incorrectly.
