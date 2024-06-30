#write functions here, don't add input('') statements here!

def get_assessment_value(value):
    assessment_value= round(eval(value)/100*60,2)
    print("Your assessment value is:${}".format(assessment_value))

def get_tax_value(value):
    get_tax_assessed= round(eval(value)/100*60/100*0.72,2)
    print("The property tax you must pay is:${}".format(get_tax_assessed))

