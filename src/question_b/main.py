#add import
#1) A county collects property taxes on the assessment value of property, 
# which is 60 percent of the property’s actual value. For example, if an acre of land is valued at $10,000, 
# its assessment value is $6,000. The property tax is then 72¢ for each $100 of the assessment value. 
# The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the actual
# value of a piece of property and displays the assessment value and property tax. 
#Functions:
#get_assessment_value with parameter value
#get_tax_assessed with parameter assessment value

from question_b import get_assessment_value
from question_b import get_tax_value
def main():
    input_string = ''
    while 1:
        input_string = input("\nWhat is the value of your property?: ")
        if input_string == "quit":
            break
        
        print("Your assessment value is:${}".format(get_assessment_value(input_string)))
        print("The property tax you must pay is:${}".format(get_tax_value(get_assessment_value(input_string))))
main()       