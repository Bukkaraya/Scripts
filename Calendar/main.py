DAYS = ['Monday', 'Tuesday', 'Wednesday', 
        'Thursday', 'Friday', 'Saturday', 'Sunday']
YEAR = 2001



def getLeapYears(year1, year2):
    num = 0
    
    for i in range(year1, year2):
        if i % 4 == 0:
            num += 1
    
    return num



def getDate(user_year):
    diff = abs(YEAR - user_year)
    num_leap_years = 0
    
    if user_year >= YEAR:
        num_leap_years = getLeapYears(YEAR, user_year)
    else:
        num_leap_years = getLeapYears(user_year, YEAR)
    
    num_days = (diff + num_leap_years) % 7
    
    if user_year >= YEAR:
        print("The day is {}".format(DAYS[num_days]))
    else:
        if num_days == 0:
            print("The day is {}".format(DAYS[num_days]))
        else:
            print("The day is {}".format(DAYS[len(DAYS) - num_days]))



def main():
    print('Please enter a year...')
    user_year = int(input('>'))
    getDate(user_year)



if __name__ == '__main__':
    main()