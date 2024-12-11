# temperature_converter.py

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    Formula: (C × 9/5) + 32 = F
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    Formula: (F − 32) × 5/9 = C
    """
    return (fahrenheit - 32) * 5/9


def main():
    """
    Main function to run the program interactively.
    """
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid choice. Please choose 1 or 2.")
    

if __name__ == "__main__":
    main()
