import time

MONTHS_IN_REGULAR_YEAR = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTHS_IN_LEAP_YEAR = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

HOURS_IN_A_DAY = 24
MINUTES_IN_ONE_HOUR = 60
SECONDS_IN_A_MINUTE = 60

NR_OF_DATE_PARAMETERS = 3


def input_data():

    while True:
        compared_date = input("Podaj datę od której chcesz policzyć czas w formacie rrrr-mm-dd: ")
        compared_date = compared_date.split('-')
        error_message = ''
        if is_integer(compared_date):
            error_message += 'Data może zawierać tylko liczby całkowite.\n'
            print(error_message)
        if len(compared_date) != NR_OF_DATE_PARAMETERS:
            error_message += 'Niepoprawny zapis.\n'

        if len(error_message) == 0:
            return list(map(int, compared_date))
        else:
            print(error_message, " Spróbuj jeszcze raz.")


def is_integer(arr):
    for num in arr:
        if not num.isdigit():
            return True
    return False


def checking_month_correctness(year, month, day):
    if year % 4 == 0 or year % 400 == 0:
        if MONTHS_IN_LEAP_YEAR[month - 1] < day:
            return False
    else:
        if MONTHS_IN_REGULAR_YEAR[month - 1] < day:
            return False
    return True
# def checking_data_correctness(date):
#     date = date.split('-')
#     error_message = ''
#     if is_integer(date):
#         error_message += 'Data może zawierać tylko liczby całkowite.\n'
#         print(error_message)
#     if len(date) != NR_OF_DATE_PARAMETERS:
#         error_message += 'Niepoprawny zapis.\n'
#
#     return error_message
#
#
# def checking_month_correctness(year, month, day):
#     print(year)
#     print(month)
#     print(day)


def days_correction(today, given_day):
    correction = 0
    if today[0] % 4 == 0 or today[0] % 400 == 0:
        for month in MONTHS_IN_LEAP_YEAR[:today[1] - 1]:
            correction += month
    else:
        for month in MONTHS_IN_REGULAR_YEAR[:today[1] - 1]:
            correction += month
    if given_day[0] % 4 == 0 or given_day[0] % 400 == 0:
        for month in MONTHS_IN_LEAP_YEAR[:given_day[1] - 1]:
            correction -= month
    else:
        for month in MONTHS_IN_REGULAR_YEAR[:given_day[1] - 1]:
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
