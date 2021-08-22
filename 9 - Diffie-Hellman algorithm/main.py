from math import sqrt


class Diffie:
    def __init__(self):
        self.prime_number = 0

    def interface(self):
        base = ''
        while not base.isdigit():
            base = input("Podaj podstawę: ")
        base = int(base)
        while True:
            self.prime_number = input("Podaj liczbę pierwszą: ")
            if self.prime_number.isdigit():
                self.prime_number = int(self.prime_number)
                if self.is_prime_number():
                    break
        user1_number = ''
        user2_number = ''
        while not user1_number.isdigit():
            user1_number = input("Podaj liczbę pierwszego użytkownika: ")
        while not user2_number.isdigit():
            user2_number = input("Podaj liczbę drugiego użytkownika: ")
        user1_number = int(user1_number)
        user2_number = int(user2_number)
        a = pow(base, user1_number) % self.prime_number
        key = pow(a, user2_number) % self.prime_number
        print(key)

    def is_prime_number(self):
        for i in range(2, int(sqrt(self.prime_number))+1):
            if self.prime_number % i == 0:
                return False
        return True


obj = Diffie()
obj.interface()
