points = 174  # use this input to make your submission

# write your if statement here
if points <= 50: 
    result = print("No prize for you.")
elif points <= 150: 
    result = print("Congratulations! You won a wooden rabbit!")
elif points <= 180: 
    result = print("Congratulations! You won a wafer-thin mint")
else:
    result = print("Congratulations! You won a penguin")

print(result)