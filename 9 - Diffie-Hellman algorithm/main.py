from math import sqrt


class DiffieHellmanAlgorithm:
    def __init__(self):
        self.prime_number = 0
        self.user1_number = ''
        self.user2_number = ''
        self.base = ''

    def interface(self):
        self.input_public_data()
        self.input_secret_data()
        key = self.calculate_secret_key()
        print(f"Wygenerowany sekretny klucz: {key}")

    def input_secret_data(self):
        while not self.user1_number.isdigit():
            self.user1_number = input("Podaj sekrtetną liczbę całkowitą pierwszego użytkownika: ")
        while not self.user2_number.isdigit():
            self.user2_number = input("Podaj sekretną liczbę drugiego użytkownika: ")

    def input_public_data(self):
        while not self.base.isdigit():
            self.base = input("Podaj podstawę (liczbę całkowitą): ")
        while True:
            self.prime_number = input("Podaj liczbę pierwszą: ")
            if self.prime_number.isdigit():
                self.prime_number = int(self.prime_number)
                if self.is_prime_number():
                    break
                else:
                    print("Podana liczba musi być liczbą pierwszą")
            else:
                print("Musisz podać liczbę całkowitą")

    def calculate_secret_key(self):
        sent_value = pow(int(self.base), int(self.user1_number)) % self.prime_number
        key = pow(sent_value, int(self.user2_number)) % self.prime_number
        return key

    def is_prime_number(self):
        if self.prime_number == 1:
            return False
        else:
            for i in range(2, int(sqrt(self.prime_number))+1):
                if self.prime_number % i == 0:
                    return False
            return True


obj = DiffieHellmanAlgorithm()
obj.interface()
