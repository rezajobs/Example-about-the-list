game_list = ['apple', 'kabab', 'iphone', 'cellphone', 'tv']

print("Original list:")
print(game_list)

sorted_list = sorted(game_list)

print("Sorted list (for reference):")
print(sorted_list)

# Ask user to input the sorted list in a comma-separated format
user_input = input('Please enter the sorted list separated by commas (e.g., "apple, cellphone, iphone, kabab, tv"): ')

# Convert user input into a list of strings, stripping extra spaces
items = user_input.split(',')
user_input_list = [item.strip() for item in items]

# Compare the cleaned user input list with the sorted list
if user_input_list == sorted_list:
    print('Great!!! Good job!!!')
else:
    print('It is not correct, try again.')
