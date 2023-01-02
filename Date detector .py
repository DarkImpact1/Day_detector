# ----------------------------------------------------JAI SHREE RAM----------------------------------------

# CONCEPT - shortcut used to detect day on particular date of any year is -----[ date +  code of month + no_of_year (whose range is from 1 to 99 i.e. last two digit of year) + no_of_leapyear + year_code ] whatever the value comes divide it by 7 seven and then the remainder will give you the result

def leapyear(a):  # assigning special value to months based on year
    if a % 4 == 0:
        month_code = ["0", "0", "3", "4", "0",
                      "2", "5", "0", "3", "6", "1", "4", "6"]

    else:
        month_code = ["0", "1", "4", "4", "0",
                      "2", "5", "0", "3", "6", "1", "4", "6"]
    return (month_code)


def num_of_year(a):  # to count no of year from 1 to 99
    return int(str(a)[len(str(a))-2:])


# Assigning value to months of different days
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months_having_30days = [4, 6, 9, 11]
months_having_31days = [1, 3, 5, 7, 8, 10, 12]

# program to detect day on particular


def program():
    # calling function to get value of year
    no_of_year = num_of_year(year)
    # getting no of leap year
    no_of_leap_year = no_of_year // 4
    # assigning value to particular day
    day = ['Saturday', 'Sunday', 'Monday', 'Tuesday',
           'Wednesday', 'Thursday', 'Friday', ]
    # calling function to assign a month code to variable x according to the month
    x = int(leapyear(year)[month])

    # Checking condition if year lies within the range
    if year in range(1, 100) or year in range(400, 500) or year in range(800, 900) or year in range(1200, 1300) or year in range(1600, 1700) or year in range(2000, 2100) or year in range(2400, 2500) or year in range(2800, 2900):
        # assigining year code
        year_code = 6
        # adding every result
        result = date + x + no_of_year + no_of_leap_year + year_code
        # getting remainder to check date
        final_result = result % 7
        # assigning value to day
        Day = print(f'Day on {date}/{month}/{year} is {day[final_result]}')
    elif year in range(100, 200) or year in range(500, 600) or year in range(900, 1000) or year in range(1300, 1400) or year in range(1700, 1800) or year in range(2100, 2200) or year in range(2500, 2600) or year in range(2900, 3000):
        year_code = 4
        result = date + x + no_of_year + no_of_leap_year + year_code
        final_result = result % 7
        Day = print(f'Day on {date}/{month}/{year} is {day[final_result]}')
    elif year in range(200, 300) or year in range(600, 700) or year in range(1000, 1100) or year in range(1400, 1500) or year in range(1800, 1900) or year in range(2200, 2300) or year in range(2600, 2700) or year in range(3000, 3100):
        year_code = 2
        result = date + x + no_of_year + no_of_leap_year + year_code
        final_result = result % 7
        Day = print(f'Day on {date}/{month}/{year} is {day[final_result]}')
    elif year in range(300, 400) or year in range(700, 800) or year in range(1100, 1200) or year in range(1500, 1600) or year in range(1900, 2000) or year in range(2300, 2400) or year in range(2700, 2800) or year in range(3100, 3200):
        year_code = 0
        result = date + x + no_of_year + no_of_leap_year + year_code
        final_result = result % 7
        Day = print(f'Day on {date}/{month}/{year} is {day[final_result]}')

# ------------------------------------------------------------START-------------------------------------------------



while True:
    start=input("Enter check to start checking.... :\t").lower().strip()
    if start=="check":
        start=True
        break
    else:
        print("wrong input..")

        
while start==True:
    print('Enter date of any year to know the day on that particular date')
    # Taking input from user
    date, month, year = input(
    'Enter the [DD/MM/YYYY] in the same format:-\t ').split("/")

    # Converting them to integer
    date, month, year = int(date), int(month), int(year)

    if year > 0 and month < 13 and date < 32:

        # if year is a leap year
        if year % 4 == 0:

            # Checking wether user had entered correct month
            if month not in months:
                print("Please input correct month")

            # Checking weather user had entered correct date
            elif (month in months_having_30days and date >= 31 or date == 0) or (month in months_having_31days and date >= 32 or date == 0) or (month == 2 and date >= 30 or date == 0):
                print('Please enter correct date')

            # If user had entered every thing correct then else part will be executed
            else:
                program()
        # If not a leap year
        else:
        # Checking wether user had entered correct month
            if month not in months:
                print("Please input correct month")

        # Checking weather user had entered correct date
            elif (month in months_having_30days and date >= 31 or date == 0) or (month in months_having_31days and date >= 32 or date == 0) or (month == 2 and date >= 29 or date == 0):
                print('Please enter correct date')

        # If user had entered every thing correct then else part will be executed
            else:
                program()
    else:
        start=False
