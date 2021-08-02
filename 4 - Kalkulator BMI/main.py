from math import inf

MALE_BMI_RANGE = {
    24: [20, 25, 30, 40],
    34: [21, 26, 31, 41],
    44: [22, 27, 32, 42],
    54: [23, 28, 33, 43],
    64: [24, 29, 34, 44],
    inf: [25, 30, 35, 45]

}

FEMALE_BMI_RANGE = {
    24: [19, 24, 29, 39],
    34: [20, 25, 30, 40],
    44: [21, 26, 31, 41],
    54: [22, 27, 32, 42],
    64: [23, 28, 33, 43],
    inf: [24, 29, 34, 44],
}

SEX_MALE = "male"
SEX_FEMALE = "female"


def return_table_of_values():
    while True:
        sex = input(f"Podaj swoją płeć({SEX_MALE}/{SEX_FEMALE}): ")
        if sex.lower() == SEX_MALE:
            return MALE_BMI_RANGE
        elif sex.lower() == SEX_FEMALE:
            return FEMALE_BMI_RANGE
        else:
            print("Podano nieprawidłową wartość!")


def return_list_of_values():
    values = return_table_of_values()
    age = input_age()
    for key in values.keys():
        if age <= key:
            return list(values)


def input_age():
    while True:
        age = input("Podaj swój wiek: ")
        if age.isdigit() and age != '0':
            return int(age)
        else:
            print("Wiek musi być dodatnią liczbą całkowitą.")


def calculate_bmi():
    while True:
        height = input("Podaj swój wzrost w centymetrach: ")
        mass = input("Podaj masę swojego ciała w kilogramach: ")
        if height.isdigit() and mass.isdigit():
            return round(float(mass) / (float(height) ** 2), 2)
        else:
            print("Niepoprawny wzrost lub masa. Spróbuj ponownie.")


def bmi_calc():
    list_of_values = return_list_of_values()
    bmi = calculate_bmi()

    print(f"Twoje BMI wynosi {bmi}.")
    if bmi < list_of_values[0]:
        print("Przy twoim wzroście oznacza to, że masz niedowagę.")
    elif bmi < list_of_values[1]:
        print("Przy twoim wzroście oznacza to, że twoja waga jest prawidłowa.")
    elif bmi < list_of_values[2]:
        print("Przy twoim wzroście oznacza to, że masz nadwagę.")
    elif bmi < list_of_values[3]:
        print("Przy twoim wzroście oznacza to, że jesteś otyły.")
    else:
        print("Przy twoim wzroście oznacza to, że jesteś bardzo otyły.")


bmi_calc()
