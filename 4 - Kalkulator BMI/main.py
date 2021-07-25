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


def return_table_of_values():
    while True:
        sex = input("Podaj swoją płeć(male/female): ")
        if sex == "male":
            return MALE_BMI_RANGE
        elif sex == "female":
            return FEMALE_BMI_RANGE
        else:
            print("Podano nieprawidłową wartość!")


def return_list_of_values(values):
    age = int(input("Podaj swój wiek: "))
    for key in values.keys():
        if age <= key:
            return values
        

def calculate_bmi():
    height = float(input("Podaj swój wzrost w centymetrach: "))
    height /= 100
    mass = float(input("Podaj masę swojego ciała w kilogramach: "))
    return round(mass/(height**2), 2)


def bmi_calc():
    table_of_values = return_table_of_values()
    list_of_values = return_list_of_values(table_of_values)
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
