class Car:
    def __init__(self, model=str, vin_number=int, numbers=int):
        self.model = model
        self.__vin = vin_number
        self.__numbers = numbers

    def __is_valid_vin(vin_number):
        if not vin_number == int:
            raise IncorrectVinNumber("Некорректный тип vin номер")
        elif vin_number not in range(100000,9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(numbers):
        if not numbers == str:
            raise IncorrectCarNumbers('Некорректный тип данных для номера')
        elif not len(numbers) == 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True
class IncorrectVinNumber (Exception):
    def __init__(self, message=str):
        self.message = message


class IncorrectCarNumbers (Exception):
    def __init__(self, message=str):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')