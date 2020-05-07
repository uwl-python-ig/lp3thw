
def formula2(arg1):
    half2 = arg1 / 2
    triple3 = half2 * 3
    plus4 = triple3 + 4
    return half2, triple3, plus4

theArg = int(input("Input the arg: "))

# here's the thing again--see bmr_ex24_sd1.py LINE 37
half2, triple3, plus4 = formula2(theArg)

print(f"""
Here's your first method of formatting a string
    with variables--using the var names in curly braces.
{half2}
{triple3}
{plus4}
""")

# Okay, now can I reproduce the method used to get the function output from
    # the end of the ex24 script?
results = formula2(theArg)
print("""
Here's a second method of formatting this string.
Instead of the \'f\"string\" method, I'm using
\'.format(*var)\' following the string.
The asterisk is significant, I think.
Now all I need to do is include curly braces,
    which of course will be replaced by the three vars returned
    by the function.
Okay, so there are three results of the function 'formula2'.
1. {}
2. {}
3. {}
""".format(*results))
# I did it.
    # Still don't know if I could explain it concisely in words...

# LINES I STILL DON'T FULLY UNDERSTAND: 23, 36
