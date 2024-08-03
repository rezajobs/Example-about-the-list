vote_list = ['Alex','Sara','Max','Alex','max','sara','Alex','sara','Alex','Sara','Max','max','max','sara','Alex','sara']


while 'Alex' in vote_list:
    vote_list.remove('Alex')

print(f'New list is: {vote_list}')

counter_Sara = 0
counter_Max = 0 

for i in range(len(vote_list)):
    if vote_list[i].lower() == 'sara':
        counter_Sara += 1
    elif vote_list[i].lower() == 'max':
        counter_Max += 1


print(f'Count of "Sara": {counter_Sara}')
print(f'Count of "Max": {counter_Max}')

if counter_Max > counter_Sara:
    print('Winner is Max')
elif counter_Sara > counter_Max:
    print('Winner is Sara')
else:
    print('It is a tie')
