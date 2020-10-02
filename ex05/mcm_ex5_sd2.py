name = 'Zed A. Shaw'
age = 35 # not a lie
height_inches = 74
weight_lbs = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

in_to_cm = 2.54
lbs_to_kg = 0.453592

height_cm = height_inches * in_to_cm
weight_kg = weight_lbs * lbs_to_kg

print(f"Let's talk about {name}.")
print(f"He's {height_inches} inches tall.")
print(f"He's also {height_cm} centimeters tall.")
print(f"He's {weight_lbs} pounds heavy.")
print(f"He's also {weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height_inches + weight_lbs
print(f"If I add {age}, {height_inches}, and {weight_lbs}, I get {total}.")
