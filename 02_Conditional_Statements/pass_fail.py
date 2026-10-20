marks = float(input("Enter your marks: "))

if marks >= 35 and marks <= 100:
    print("Pass")
elif marks >= 0 and marks < 35:
    print("Fail")
else:
    print("Invalid marks")