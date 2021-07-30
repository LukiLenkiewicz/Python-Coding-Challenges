import time

REGULAR_YEAR = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_YEAR = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

HOURS_IN_A_DAY = 24
MINUTES_IN_ONE_HOUR = 60
SECONDS_IN_A_MINUTE = 60

NR_OF_DATE_PARAMETERS = 3


def input_data():
    
    while True:
        compared_date = input("Podaj datę od której chcesz policzyć czas w formacie rrrr-mm-dd: ")
        compared_date = compared_date.split('-')
        error_message = ''
        if len(compared_date) != NR_OF_DATE_PARAMETERS:
            error_message += 'Niepoprawny zapis.\n'
        elif int(compared_date[2]) > 12 and int(compared_date[2]) < 1:
            error_message += 'Niepoprawna długość miesięcy.\n'
        else:
            return list(map(int, compared_date))

    


def days_correction(today, given_day):
    correction = 0
    if today[0] % 4 == 0 or today[0] % 400 == 0:
        for month in LEAP_YEAR[:today[1] - 1]:
            correction += month
    else:
        for month in REGULAR_YEAR[:today[1] - 1]:
            correction += month
    if given_day[0] % 4 == 0 or given_day[0] % 400 == 0:
        for month in LEAP_YEAR[:given_day[1] - 1]:
            correction -= month
    else:
        for month in REGULAR_YEAR[:given_day[1] - 1]:
            correction -= month
    return correction + today[2] - given_day[2]


def calculate_days(today, given_day):
    days_passed = 0
    for i in range(today[0] - given_day[0]):
        if (given_day[0] + i) % 4 == 0 or (given_day[0] + i) % 400 == 0:
            days_passed += 366
        else:
            days_passed += 365
    days_passed += days_correction(today, given_day)
    return days_passed


def data_calculator():
    todays_time = list(time.localtime())[:6]
    compared_date = input_data()
    time_passed = calculate_days(todays_time, compared_date)
    print(f"Od wybranej daty minęło {time_passed} dni.")
    time_passed = time_passed*HOURS_IN_A_DAY + todays_time[3]
    print(f"Jest to {time_passed} godzin.")
    time_passed = time_passed*MINUTES_IN_ONE_HOUR + todays_time[4]
    print(f"Lub {time_passed} minut.")
    time_passed = time_passed*SECONDS_IN_A_MINUTE + todays_time[5]
    print(f"Lub {time_passed} sekund.")


data_calculator()
