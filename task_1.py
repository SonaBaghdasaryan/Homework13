# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник
# со сторонами отрицательной длины.


import sys
from builtins import print, super, staticmethod, Exception


class InvalidInputError(Exception):
    def __init__(self, input_value):
        self.input_value = input_value
        self.message = f"Invalid input: {input_value}"
        super().__init__(self.message)


class FibonacciCalculator:
    def __init__(self):
        pass

    @staticmethod
    def calculate(n):
        if n <= 0:
            raise InvalidInputError(n)

        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fibonacci.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        calculator = FibonacciCalculator()
        result = calculator.calculate(n)
        logging.info(f"Fibonacci({n}) = {result}")
        print(f"Fibonacci({n}) = {result}")
    except ValueError:
        input_value = sys.argv[1]
        logging.error(f"Invalid input: n should be an integer, received {input_value}")
        print("Error: Invalid input. n should be an integer.")
    except InvalidInputError as e:
        input_value = e.input_value
        logging.error(e.message)
        print(f"Error: {e.message}")

class AnimalCreationError(Exception):
    pass


class Animal:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Это неизвестное животное.")


class Fish(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def display_info(self):
        print(f"Это рыба по имени {self.name}. Она живет в {self.habitat}.")


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def display_info(self):
        print(f"Это птица по имени {self.name}. Ее размах крыльев составляет {self.wingspan}.")


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, **kwargs):
        if animal_type == "Fish":
            return Fish(name, kwargs.get("habitat"))
        elif animal_type == "Bird":
            return Bird(name, kwargs.get("wingspan"))
        elif animal_type == "Animal":
            return Animal(name)
        else:
            raise AnimalCreationError(f"Тип животного '{animal_type}' не поддерживается.")


try:
    fish = AnimalFactory.create_animal("Fish", "Немо", habitat="океане")
    fish.display_info()

    bird = AnimalFactory.create_animal("Bird", "Орел", wingspan="2 метра")
    bird.display_info()

    animal = AnimalFactory.create_animal("Animal", "Неизвестное животное")
    animal.display_info()

    unknown_animal = AnimalFactory.create_animal("Unknown", "Алиса")
    unknown_animal.display_info()

except AnimalCreationError as e:
    print(f"Ошибка при создании животного: {e}")