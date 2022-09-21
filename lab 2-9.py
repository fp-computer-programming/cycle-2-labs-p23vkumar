#1. Create a copy of lab_2-8.py and rename it lab_2-9.py
#2. Change the program written previously to use chained 
# conditional statements instead of nested conditional statements.

x = int(input("Welcome. Please Enter the Number: "))
if x <= 8:
    print("Well Sucks to be you! No Medal") 
elif x <= 11:
    print("Good! You have won a Bronze Medal")
elif x <= 14:
    print("Amazing! You have won a Silver Medal")
else:
    print("Spectacular! You have earned a Gold Medal")