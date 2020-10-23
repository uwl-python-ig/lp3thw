# Why did you use a while-loop?
    # Try rewriting i twith a for-loop and see if that's easier

# Gotta have some empty lines in my stdout to make it easier on my eyes
print("\n")

bmrList = ['chair', 'desk', 'pizza', 42, 100]
print(f"I'll start with a list of 5 things:\n{bmrList}.\n")

fiveList = ['jambalaya', 'of course', 99, 'hot sauce', 'nachos']
print(f"Here's another list, it has five more things:\n{fiveList}.\n")

lotsList = ['speedway', 'turtle', 'bird', 'plane', 'math', 2500, 9263, 'house plant', 'board game', 'puzzle', 'sweater', 'pasta', 'maple tree']
print(f"Okay, just one more list to consider--this one will come into play just a bit later:\n{lotsList}\n")

# Try just a for-loop, but make sure my additional list has just enough items in it to make my desired total
print("The for-loop: Adding everything in both lists.")
for i in fiveList:
    print(f"Now adding {i}.")
    bmrList.append(i)
    print(f"Here's what the list looks like now:\n{bmrList}.")

print("Alright, we added all of the second list to the first list.")

print("Oh, I need to reduce 'bmrList' back down to just five items before proceeding. How to do that?")
del bmrList[5:10]
print("Did it work?\n", bmrList, "\nOkay, good.")

# Try a for-loop with a while-loop inside (??)***, so that my additional list can have any number of items in it but I can take just only as many as I need to make my desired total
# But really, this means that I couldn't acheive the task with (only) a for-loop
print("The for > while loop attempt: Adding everything in the first list with only enough from the third list to reach a desired total number of objects in the list.")
for i in lotsList:
    if len(bmrList) < 10:
        print(f"Now adding {i}.")
        bmrList.append(i)
        print(f"Here's what the list looks like now:\n{bmrList}")
    else:
        pass

print("Alright, I *think* we added just enough from the second list to make the first list total ten items...")

# *** HA! Funny.
    # Putting the while inside the for meant that I added the same list item again and again
    # For the first list item add the first list item, over and over again, to the list until the length equals 10
