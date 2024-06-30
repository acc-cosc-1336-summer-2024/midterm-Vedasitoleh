#add import
# import reverse_string

from question_a import reverse_string

def main():
    input_string = ''
    while 1:
        input_string = input("\n Give a string to reverse: ")
        if input_string == "quit":
            break
        reverse_string(input_string)

main()       