queuequeue = []

while True:
    customer = input('Write your number please (or type "check" to check your position, or "-1" to stop): ')
    if customer == -1:
        break
    elif customer == 'check':
        if len(queue)== 0:
            print('this queue is empty.')
        else:
            number_check = int(input('enteryour number to check your position :'))
            if number_check in queue:
                position = queue.index(number_check) + 1
                print(f'Your position in the queue is: {position}')
            else:
                print('Your number is not in the queue.')
    else:
        queue.append(int(customer))
        print('Added to queue:', queue)
