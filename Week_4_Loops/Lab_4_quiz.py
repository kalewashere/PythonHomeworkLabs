print('Quiz Program!')

answer = input('What is the capital of Wisconsin? ')
# going to use loop instead of if statement. jk may need an if statement but lets try without
# while answer.lower() == 'madison':
    # print('Correct!')    turned into a comment to see what i am changing
while answer.lower() != 'madison':
    print('Sorry, that is not correct. Please try again.')
    answer = input('What is the capital of Wisconsin? ')
if answer.lower() == 'madison':
    print('Correct!') # i am pretty sure I tried this with the code above and it didnt work - let me try again below


# while answer.lower() == 'madison':
    # print('Correct!')
    # if answer.lower() != 'madison':
    #    print('Sorry, that is incorrect.')
    #     answer = input('what is the capital of Wisconsin? ')
# yeeeeap, didn't work. I'll have to re-watch the video to figure out why. I must have missed it 
