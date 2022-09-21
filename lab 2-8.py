#Create a Python file named lab_3-1.py
#2. A team needs to score 15 points to win a gold medal,
# between 12-14 points to win a silver medal,
# and between 9-11 point to win a bronze medal.
# A team does not earn a medal if they earn 8 or fewer points. 
# Write a program using nested if else statements 
# where a user can input the number of points a team scored 
# and the medal that they earned is displayed.

x = int(input("Enter number of points: ")) 
if x >= 15:
    print("Spectacular! You have earned a Gold Medal")
else:
    if x >= 12:
        print("Amazing! You have won a Silver Medal")
    else:
        if x >= 9:
            print("Good! You have won a Bronze Medal")
        else:
            if x <=8:
                print("Well Sucks to be you! No Medal")