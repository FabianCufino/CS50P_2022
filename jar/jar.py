class Jar:
    def __init__(self, capacity=12):

        self.capacity = int(capacity)
        self.q_cookies = 0

    def __str__(self):
        self.cap_1 = "🍪" * int(self.q_cookies)
        return f"{self.cap_1}"

    def deposit(self, n):
        if int(n) > self.capacity - self.q_cookies :
            raise ValueError("cantidad de galletas superior a la capacidad")
        else:
            self.q_cookies = self.q_cookies + int(n)
            return self.q_cookies
            #print("cantidad de galletas actuales son", self.q_cookies)

    def withdraw(self, n):
            if int(n) > self.q_cookies :
                raise ValueError("cantidad de galletas a comer son mayores a las que hay")
            else:
                self.q_cookies = self.q_cookies - int(n)
                return self.q_cookies
            #print("cantidad de galletas actuales son", self.q_cookies)


    @property
    def capacity(self):
       return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError("capacidad del tarro negativa")
        self._capacity = int(capacity)

    @property
    def size(self):
       return self.q_cookies



def main():
    capacity = input("capacity: ")
    jar = Jar(capacity)
    deposit_1 = input("deposit:")
    jar.deposit(deposit_1)
    print(str(jar))
    print("la cantidad de galletas actuales son", jar.size)
    deposit_2 = input("deposit:")
    jar.deposit(deposit_2)
    print("la capacidad del tarro es", jar.capacity)
    withdraw_1 = input("withdraw:")
    jar.withdraw(withdraw_1)
    withdraw_2 = input("withdraw:")
    jar.withdraw(withdraw_2)

    #print(type(Jar(capacity)))

    return Jar(capacity)

