import sys
USAGE_STRING = "Usage: python3 leap_years.py startyear numberofyearstoprint"

try:
    START_YEAR = int(sys.argv[1])
    print('start year:', sys.argv[1])
except ValueError:
    print("Error: start year must be a non-negative integer.")
    quit()
except IndexError:
    print(USAGE_STRING)
    quit()

try:
    NUMBER_OF_YEARS_TO_PRINT = int(sys.argv[2])
    print('number of years to print:', sys.argv[2])
except ValueError:
    print("Error: number of years must be a non-negative integer.")
    quit()
except IndexError:
    print(USAGE_STRING)
    quit()

number_of_years_printed = 0
i = START_YEAR

while number_of_years_printed < NUMBER_OF_YEARS_TO_PRINT:
    i += 1
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
        print(i)
        number_of_years_printed += 1

