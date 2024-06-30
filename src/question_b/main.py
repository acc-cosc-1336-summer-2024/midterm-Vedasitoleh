#add import

from question_b import get_assessment_value
from question_b import get_tax_value
def main():
    input_string = ''
    while 1:
        input_string = input("\n What is the value of your property?")
        if input_string == "quit":
            break
        get_assessment_value(input_string)
        get_tax_value(input_string)

main()       