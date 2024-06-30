#write functions here, don't add input('') statements here!

def get_assessment_value(value):
    assessment_value= round(int(value)/100*60,2)
    return int(assessment_value)

def get_tax_value(value):
    get_tax_assessed= round(value/100*0.72,2)
    return get_tax_assessed

