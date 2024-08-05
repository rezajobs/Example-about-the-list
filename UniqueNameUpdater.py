name_list = ['shahram', 'mohammad', 'ali', 'sara', 'sara', 'reza', 'ali','sara']

name_count = {}  # Dictionary to keep track of the count of each name

for i in range(len(name_list)):
    name = name_list[i]
    if name in name_count:
        name_count[name] += 1
        name_list[i] = f'{name}{name_count[name]}'
    else:
        name_count[name] = 1

print(name_list)
