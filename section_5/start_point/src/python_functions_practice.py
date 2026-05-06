def return_10():
    return 10

def add( number_1, number_2 ):
    return number_1 + number_2

def subtract( number_1, number_2):
    return number_1 - number_2

def multiply( number_1, number_2):
    return number_1 * number_2

def divide( number_1, number_2):
    return number_1 / number_2

def length_of_string( string ):
    return len(string)

def join_string( string_1, string_2):
    return string_1 + string_2

def add_string_as_number( string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name( number ):
    months = [ 
        {"number": 1, "name": "January"},
        {"number": 2, "name": "February"},
        {"number": 3, "name": "March"},
        {"number": 4, "name": "April"},
        {"number": 5, "name": "May"},
        {"number": 6, "name": "June"},
        {"number": 7, "name": "July"},
        {"number": 8, "name": "August"},
        {"number": 9, "name": "September"},
        {"number": 10, "name": "October"},
        {"number": 11, "name": "November"},
        {"number": 12, "name": "December"}
    ]

    for month in months:
        if month["number"] == number:
            return month["name"]

def number_to_short_month_name( number ):
    months = [ 
        {"number": 1, "name": "Jan"},
        {"number": 2, "name": "Feb"},
        {"number": 3, "name": "Mar"},
        {"number": 4, "name": "Apr"},
        {"number": 5, "name": "May"},
        {"number": 6, "name": "Jun"},
        {"number": 7, "name": "Jul"},
        {"number": 8, "name": "Aug"},
        {"number": 9, "name": "Sep"},
        {"number": 10, "name": "Oct"},
        {"number": 11, "name": "Nov"},
        {"number": 12, "name": "Dec"}
    ]

    for month in months:
        if month["number"] == number:
            return month["name"]
        
def get_volume_of_cube( side ):
    return side * side * side

def get_reversed_string( string ):
    return string[::-1]

def get_temperature_in_celsius( fahrenheit ):
    return (fahrenheit - fahrenheit) * 5/9