print("Here are some questions about you and your measurements.")
print("First, what is your name?", end=' ')
name = input()
print(f"Hello {name}! How old are you?", end=' ')
age = input()
print("Great! How tall are you?", end=' ')
height = input("Please use feet/inches. ")
print("And your weight?", end=' ')
weight = input("Please use pounds. ")
print(f"Perfect! Now, {name}, let's get to measurements.")
print("What is your bust measurement?", end=' ')
bust = input("Please use inches. ")
print("What is your waist measurement?", end=' ')
waist = input("Please use inches. ")
print("What is your hip measurement?", end=' ')
hip = input("Please use inches. ")
print("Almost done! Just double-check to make sure it all looks correct.")

combined = f"""
{name}'s Measurements
\t*Age: {age}
\t*Height: {height}
\t*Weight: {weight} lbs
\t*Bust: {bust} in
\t*Waist: {waist} in
\t*Hip: {hip} in
"""

print(combined)
input("Does this look correct? ")

print("Thank you for your time!")
