shop_list = []

while True:
    shop_input = input('Enter model and price (Ex: iphone,2000) or type "done" to finish: ')
    
    if shop_input.lower() == 'done':
        break
    
    model, price = shop_input.split(',')
    shop_list.append([model, int(price)])

print("List is:", shop_list)
