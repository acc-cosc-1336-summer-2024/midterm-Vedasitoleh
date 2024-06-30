#add import
from question_c import is_prime

def main():
    input_string = ''
    while 1:
        input_string = input("\n Check if a number is Prime: ")
        if input_string == "quit":
            break
        is_prime(eval(input_string))

main()       
