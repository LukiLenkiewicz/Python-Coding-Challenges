import time

REGULAR_YEAR = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_YEAR = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

HOURS_IN_A_DAY = 24
SECONDS_IN_A_MINUTE = 60
SECONDS_IN_ONE_HOUR = 3600


def input_data():
    compared_date = input("Podaj datę od której chcesz policzyć czas w formacie rrrr-mm-dd: ")
    compared_date = compared_date.split('-')
    return list(map(int, compared_date))


def calculate_days(today, not_today):
    days_passed = 0
    for i in range(today[0] - not_today[0]):
        if (not_today[0] + i) % 4 == 0 or (not_today[0] + i) % 400 == 0:
            days_passed += 366
        else:
            days_passed += 365
    if today[0] % 4 == 0 or today[0] % 400 == 0:
        for month in LEAP_YEAR[:today[1] - 1]:
            days_passed += month
    else:
        for month in REGULAR_YEAR[:today[1] - 1]:
            days_passed += month

    if not_today[0] % 4 == 0 or not_today[0] % 400 == 0:
        for month in LEAP_YEAR[:not_today[1] - 1]:
            days_passed -= month
    else:
        for month in REGULAR_YEAR[:not_today[1] - 1]:
            days_passed -= month
    days_passed = days_passed + today[2] - not_today[2]
    return days_passed


def data_calculator():
    todays_time = list(time.localtime())[:6]
    compared_date = input_data()
    time_passed = calculate_days(todays_time, compared_date)
    print(f"Od wybranej daty minęło {time_passed} dni.")
    time_passed = time_passed*HOURS_IN_A_DAY + todays_time[3]
    print(f"Jest to {time_passed} godzin.")
    time_passed = time_passed*SECONDS_IN_ONE_HOUR + todays_time[4]*SECONDS_IN_A_MINUTE + todays_time[5]
    print(f"LUB {time_passed} sekund.")


data_calculator()
