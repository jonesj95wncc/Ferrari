# Declare the variables
year = int

# Functions
def get_value(year):

    # Year with equivalent car value
    y1962_to_1964 = 1800
    y1965_to_1968 = 6000
    y1969_to_1971 = 12000
    y1972_to_1975 = 48000
    y1976_to_1980 = 200000
    y1981_to_1985 = 650000
    y1986_to_2012 = 35000000
    y2013_to_2014 = 52000000

    # If-else statement
    if ((year >= 1962) and (year <= 1964)):
        car_value = y1962_to_1964
    elif ((year >= 1965) and (year <= 1968)):
        car_value = y1965_to_1968
    elif ((year >= 1969) and (year <= 1971)):
        car_value = y1969_to_1971
    elif ((year >= 1972) and (year <= 1975)):
        car_value = y1972_to_1975
    elif ((year >= 1976) and (year <= 1980)):
        car_value = y1976_to_1980
    elif ((year >= 1981) and (year <= 1985)):
        car_value = y1981_to_1985
    elif ((year >= 1986) and (year <= 2012)):
        car_value = y1986_to_2012
    elif ((year >= 2013) and (year <= 2014)):
        car_value = y2013_to_2014
    else:
        print("No estimated value yet for year 2015 and above.")
        exit()
    return car_value

#The while loop will keep executing the code statements until the condition is no longer True
while year != 2015:
    year = int(input("Please enter year of Ferrari 250 GTO: " ))
    print("The estimated value of Ferrari 250 GTO year", year, "is: ", "${:,.2f}".format(get_value(year)))
