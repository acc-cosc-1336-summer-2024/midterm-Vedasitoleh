#add import
from question_d import get_random_number

user_answer = ''
while 1:
    #pick a random number and assign it to a variable
    current_answer = str(get_random_number())
    #take user input
    user_answer = input("Guess a number between 1-5: ")
    #if user input is 'quit', force exit
    if user_answer == 'quit':
        break
    #compare both values
    while user_answer!= current_answer:
        print('WRONG! TRY AGAIN')
        user_answer = input("Guess a number between 1-5: ")
    print('CONGRATS! LETS PLAY AGAIN!')

