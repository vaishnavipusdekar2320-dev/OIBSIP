print("BMI Calculator")
print("----------------")

while True:
    try:
        # Get weight
        weight = float(input("Enter your weight in kg: "))

        # Get height
        height = float(input("Enter your height in meters: "))

        # Validate values
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be greater than 0.")
            continue

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Display BMI
        print("\nYour BMI is:", round(bmi, 2))

        # Classify BMI
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("Category:", category)

        # Ask whether user wants another calculation
        again = input("\nDo you want to calculate again? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the BMI Calculator!")
            break

    except ValueError:
        print("Error: Please enter numbers only.")