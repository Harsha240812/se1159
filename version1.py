# Predict temperature using user input

# Get coefficients from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Get time value from user
t = float(input("Enter the time (t): "))

# Quadratic formula: T = a*t^2 + b*t + c
T = a * t**2 + b * t + c

# Display result
print(f"Predicted temperature at t={t}: {T:.2f}°C")
