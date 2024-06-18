first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plus_symbol = '+'

# We will create a new list to store the result
result_list = []

# Iterate through the first_list
for i in range(len(first_list)):
    result_list.append(first_list[i])
    # Insert '+' after every element except the last one
    if i < len(first_list) - 1:
        result_list.append(plus_symbol)

print(result_list)
