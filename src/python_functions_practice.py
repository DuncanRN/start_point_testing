def return_10():
    return 10

def add (number_1, Number_2):
    return (number_1 + Number_2)

def subtract (number_1, Number_2):
    return (number_1 - Number_2)

def multiply (number_1, Number_2):
    return (number_1 * Number_2)

def divide (number_1, Number_2):
    return (number_1 / Number_2)
    
def length_of_string(text):
    num = ""
    for char in text:
        if char.isdigit():
            num = num + char
    return int(num)

def join_string(text1 , text2):
    return text1 + text2 

def add_string_as_number(num_as_str1, num_as_str2):
    return int(num_as_str1) + int(num_as_str2)    

def number_to_full_month_name (num):
    if num == 1: 
       return "January"
    elif num == 2:
        return "Febuary"
    elif num == 3:
        return "March"
    elif num == 4:
        return "April"
    elif num == 5:
        return "May"
    elif num == 6:
        return "June"
    elif num == 7:
        return "July"
    elif num == 8:
        return "August"
    elif num == 9:
        return "September"
    elif num == 10:
        return "October"
    elif num == 11:
        return "Novemeber"
    elif num == 12:
        return "December"


def number_to_short_month_name (num):
    if num == 1: 
       return "Jan"
    elif num == 2:
        return "Feb"
    elif num == 3:
        return "Mar"
    elif num == 4:
        return "Apr"
    elif num == 5:
        return "May"
    elif num == 6:
        return "Jun"
    elif num == 7:
        return "Jul"
    elif num == 8:
        return "Aug"
    elif num == 9:
        return "Sep"
    elif num == 10:
        return "Oct"
    elif num == 11:
        return "Nov"
    elif num == 12:
        return "Dec"

def calculate_vol_of_cube(length):
    return length ** 3

def reverse_string(string):
    return string[::-1]

def convert_temp_f_to_c(fah):
    return (fah - 32) * 5/9