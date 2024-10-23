def get_user_data():
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))
        return weight, height
    except ValueError:
        print("Please enter valid numbers for weight and height.")
        return get_user_data()  # Retry until valid

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "You are underweight."
    elif 18.5 <= bmi < 24.9:
        return "You have a healthy weight."
    elif 25 <= bmi < 29.9:
        return "You are overweight."
    else:
        return "You are obese."

def main():
    weight, height = get_user_data()
    bmi = calculate_bmi(weight, height)
    result = interpret_bmi(bmi)
    print(f"Your BMI is: {bmi:.2f}. {result}")

if __name__ == "__main__":
    main()
