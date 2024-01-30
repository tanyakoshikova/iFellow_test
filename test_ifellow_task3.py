
class BaseConverter:
    def convert(self, celsius, method):
        if method == 'Kelvin':
            return self.convert_celsius_in_kelvin(celsius)
        elif method == 'Fahrenheit':
            return self.convert_celsius_in_fahrenheit(celsius)

    def convert_celsius_in_fahrenheit(self, celsius):
        return (9 / 5) * celsius + 32

    def convert_celsius_in_kelvin(self, celsius):
        return celsius + 273.15



number = float(input('Введите число в градусах по Цельсию '))
method = input('Выберите конвертацию в "Kelvin" или "Fahrenheit" ')
print(f'Температура в {method}: {BaseConverter().convert(number, method)}')

