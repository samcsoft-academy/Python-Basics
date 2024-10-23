# Full Temperature Converter with menu
def temperature_converter():
    print("Welcome to the Temperature Converter!")
    print("Choose the conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C is equal to {kelvin:.2f}K")
    
    else:
        print("Invalid choice! Please select a valid option.")

# Run the temperature converter
if __name__ == "__main__":
    temperature_converter()
