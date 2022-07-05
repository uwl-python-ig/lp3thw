print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # What'd that do? It prints the string ten times ..........

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Watch that comma at the end. try removing it to see what happens
# So with the , end=' ' it prints "Cheese Burger" and without it, it prints "Cheese" and "Burger" in two separate lines
# So I guess it makes a space between the first print and the second without making them two separate lines
# If I write it as print(end1 + end2 + end3 + end4 + end5 + end6, end=' ' + end7 + end8 + end9 + end10 + end11 + end12)
# it does a weird thing where "Cheese Burger" is on the same line as where I enter my next command??
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
