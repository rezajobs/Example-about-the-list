list_city = input('Write name of the city :').split()
temperatures = list(map(int, input('Write a temperatures for each of them : ').split()))

for city, temp in zip(list_city,temperatures):
    #print(f'The temperature in {city} is {temp} C')
    
    if temp< 15:
        print(f"The temperature in {city} is {temp}°C - ***warm clothes***")
    elif temp>28:
         print(f"The temperature in {city} is {temp}°C - ***Warning hot weather***")

    else:
        print(f"The temperature in {city} is {temp}°C")
