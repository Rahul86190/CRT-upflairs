'''Write a program that asks the user to enter their marks and displays 
their grade: 
• 90-100: A
• 80-89: B 
• 70-79: C 
• 60-69: D 
• Below 60: F '''
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")