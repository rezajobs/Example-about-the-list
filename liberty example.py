book_list = ["1984", "Jang va Solh", "Anakarnina"]

new_book = input('Add new book: ')

new_item_index = int(input('What number should it be on the list? '))

book_list.insert(new_item_index, new_book)


print(f'book list is {book_list}')

