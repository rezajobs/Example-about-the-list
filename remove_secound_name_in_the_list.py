mylist = ['Alex','Sara','Max','Alex','Joy','Tim','Alex','Jack']
print(f'fisrt  list is : {mylist}')

counter_Alex = 0

secound_Alex_index_number  = False

for i in range(len(mylist)):
    if mylist[i] == 'Alex':
        counter_Alex += 1
    if counter_Alex == 2:
        secound_Alex_index_number = i
        break

if secound_Alex_index_number == False:
    print(f'we can not find secound Alex in the {mylist}' )
else:
    print('postion of secound Alex number :',secound_Alex_index_number)
    mylist.pop(secound_Alex_index_number)
print(f'update the list is : {mylist}')
