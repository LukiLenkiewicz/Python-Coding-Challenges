MALE_BMI_RANGE = {
    24: [20, 25, 30, 40],
    34: [21, 26, 31, 41],
    44: [22, 27, 32, 42],
    54: [23, 28, 33, 43],
    64: [24, 29, 34, 44],
    120: [25, 30, 35, 45]

}

def bmi_calc():
    age = int(input("Podaj swój wiek: "))
    height = float(input("Podaj swój wzrost w centymetrach: "))
    height /= 100
    mass = float(input("Podaj masę swojego ciała w kilogramach: "))
    bmi = round(mass/(height**2), 2)

    print(f"Twoje BMI wynosi {bmi}")
    if bmi < 18:
        print("Przy twoim wzroście oznacza to, że masz niedowagę.")
    elif bmi < 25:
        print("Przy twoim wzroście oznacza to, że twoja waga jest prawidłowa.")
    else:
        print("Przy twoim wzroście oznacza to, że masz nadwagę.")



bmi_calc()
