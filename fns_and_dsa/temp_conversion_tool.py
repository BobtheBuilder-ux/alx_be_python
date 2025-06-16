# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_FREEZING_POINT = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius."""
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return celsius
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_FREEZING_POINT
        return fahrenheit
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    try:
        temperature = input("Enter the temperature to convert: ")
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        if unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{float(temperature)}°C is {result}°F")
        elif unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{float(temperature)}°F is {result}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()