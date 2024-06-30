#write functions here, don't add input('') statements here!
def test_config():
    return True

def reverse_string(string1):
    #counter to end function (counter set to the beginning of the string)
    letter_count=1
    #incremental that goes down by one in order to pull the next letter from the index in reverse (index on the string)
    str_count=-1
    #supposed to be a blank variable that will hold the output to print it
    str_result=''
    #loops until letter_count reaches the end of the string
    while letter_count <= len(string1):
        # increment letter_count
        letter_count+=1
        #adds the letters from the string to string_result backwards
        str_result += string1[str_count] 
        #decrements the index
        str_count-=1
    print (str_result)
    return str_result
    
#reverse_string('hello world')

