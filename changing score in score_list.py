source_list = [10, 20, 11, 12, 6, 0, 7]

print(f'Student scores list is: {source_list}')

average = sum(source_list) / len(source_list)
print(f'The average score is: {average}')

for i in range(len(source_list)):
    if source_list[i] < 10:
        source_list[i] = 9.9

print(f'Updated student scores list: {source_list}')

average = sum(source_list) / len(source_list)
print(f'The new average score is: {average}')
