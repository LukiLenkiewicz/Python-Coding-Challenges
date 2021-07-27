import datetime
import time

REGULAR_MONTHS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

REGULAR_MONTHS = list(REGULAR_MONTHS)
REGULAR_YEAR = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_YEAR = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def calculate_time(today, not_today):
    days_passed = 0
    for i in range(today[0] - not_today[0]):
        if (not_today[0] + i) % 4 == 0 or (not_today[0] + i) % 400 == 0:
            days_passed += 366
        else:
            days_passed += 365

    if (today[0] + i + 1) % 4 == 0 or (today[0] + i + 1) % 400 == 0:
        for month in LEAP_YEAR[:today[1] - 1]:
            days_passed += month
    else:
        for month in REGULAR_YEAR[:today[1] - 1]:
            days_passed += month

    if (not_today[0] + i + 1) % 4 == 0 or (not_today[0] + i + 1) % 400 == 0:
        for month in LEAP_YEAR[:not_today[1] - 1]:
            days_passed -= month
    else:
        for month in REGULAR_YEAR[:not_today[1] - 1]:
            days_passed -= month

    days_passed = days_passed + today[2] - not_today[2]
    # days_passed += today[2]
    # days_passed -= not_today[2]
    return days_passed


def data_calculator():
    todays_time = list(time.localtime())[:6]
    print(todays_time)
    compared_date = input("Podaj datę od której chcesz policzyć czas w formacie dd-mm-rrrr: ")
    compared_date = compared_date.split('-')
    compared_date.reverse()
    # compared_hour = input("Podaj godzinę w formacie hh:mm: ")
    # compared_hour = list(compared_hour.split(':'))
    # compared_date.append(compared_hour[0])
    # compared_date.append(compared_hour[1])
    compared_date = list(map(int, compared_date))

    time_passed = calculate_time(todays_time, compared_date)
    print(time_passed)


data_calculator()
