import csv


# Library program has two lists
# Genre
# Book Name

def get_genre():
    # open file
    # read file into reader
    # declare empty list genre
    # read each genre in the row
    # if the genre does not exist in the genre list
    #   add genre from row to the genre list
    genre = []
    with open('inventory.csv') as csvPointer:
        reader = csv.DictReader(csvPointer)
        for row in reader:
            if row["Genre"] not in genre:
                genre.append(row["Genre"])
    return genre


def get_book(genre):
    user_choice_genre = get_genre()[genre - 1]
    books = []
    with open('inventory.csv') as csvPointer:
        reader = csv.DictReader(csvPointer)
        for row in reader:
            if row['Genre'] == user_choice_genre:
                books.append(row['Title'])
    return books


def display_book(genre_index):
    genre_name = get_genre()[genre_index - 1]
    with open('inventory.csv') as csvPointer:
        reader = csv.DictReader(csvPointer)
        count = 1
        for row in reader:
            if row['Genre'] == genre_name:
                print(f"{count}. {row['Title']} by {row['Author']}")
                count += 1


def get_headers():
    field_names = []
    with open('inventory.csv') as csvPointer:
        reader = csv.reader(csvPointer)
        field_names = next(reader)
    return field_names


def checkout(genre_index, book_index):
    file_content = []
    genre_name = get_genre()[genre_index - 1]
    book_name = get_book(genre_index)[book_index - 1]
    row_count = 0
    book_exists = False
    field_names = get_headers()
    with open('inventory.csv') as csvPointer:
        reader = csv.DictReader(csvPointer)
        for row in reader:
            file_content.append(row)
            if row['Genre'] == genre_name and row['Title'] == book_name:
                print("Thanks for checking out {} by {}".format(book_name, row["Author"]))
                file_content[row_count]['Amount of Book'] = int(file_content[row_count]['Amount of Book']) - 1
                file_content[row_count]['Checked Out'] = int(file_content[row_count]['Checked Out']) + 1
                book_exists = True
            row_count += 1
    if book_exists:
        with open("inventory.csv", 'w') as csvPointer:
            w = csv.DictWriter(csvPointer, fieldnames=field_names)
            w.writeheader()
            w.writerows(file_content)
            # print('Thank you for checking out a book! Remember to return it when you finish reading!')


def return_bk(genre_index, book_index):
    """

    :rtype: object
    """
    file_content = []
    genre_name = get_genre()[genre_index - 1]
    book_name = get_book(genre_index)[book_index - 1]
    row_count = 0
    book_exists = False
    field_names = get_headers()
    with open('inventory.csv') as csvPointer:
        reader = csv.DictReader(csvPointer)
        for row in reader:
            file_content.append(row)
            if row['Genre'] == genre_name and row['Title'] == book_name:
                print("Thanks for returning {} by {}".format(book_name ,row["Author"]))
                file_content[row_count]['Amount of Book'] = int(file_content[row_count]['Amount of Book']) + 1
                file_content[row_count]['Checked Out'] = int(file_content[row_count]['Checked Out']) - 1
                book_exists = True
            row_count += 1
    if book_exists:
        with open("inventory.csv", 'w') as csvPointer:
            w = csv.DictWriter(csvPointer, fieldnames=field_names)
            w.writeheader()
            w.writerows(file_content)
            # print('Thank you for checking out a book! Remember to return it when you finish reading!')

# Num Chart
# Fantasy - 1
# Mystery - 2
# Realistic Fiction - 3
# How-To - 4
# Miscellaneous Nonfiction - 5

def available(book_param):
    int_count = 1
    str_count = ''
    for count in range(0, number_of_rows()):
        if count < number_of_rows() - 1:
            str_count += str(int_count) + ','
            int_count += 1
            print(str_count)
        str_count += str(int_count)
        int_count += 1
        print(str_count)
    if book_param in str_count:
        print('Book available.')
        return True
    print("Book not available.")


def number_of_rows():
    count = 0
    with open('inventory.csv') as csvPointer:
        reader = csv.DictReader(csvPointer)
        for _ in reader:
            count = count + 1
    return count


def choose():
    book_list = []
    genre_exists = False
    with open('inventory.csv') as csvPointer:
        user_genre = input('Pick a genre:' +
                           '\n1. Fantasy' +
                           '\n2. Mystery' +
                           '\n3. Realistic Fiction' +
                           '\n4. How-To' +
                           '\n5. Miscellaneous Nonfiction' +
                           '\n(1-5): ')
    file_content = []
    row_count = 0
    flag = 0
    count = 1
    with open('inventory.csv') as csvPointer:
        reader = csv.DictReader(csvPointer)
        for row in reader:
            file_content.append(row)
            if user_genre in file_content[row_count]['Genre']:
                book_list.append(file_content[row_count]['Title'])
                genre_exists = True
            row_count += 1
        if genre_exists:
            while flag < len(book_list):
                print(f'{count}. {book_list[flag]}')
                flag += 1
                count += 1
            user_book = input('Choose a book (1-...: ')
            checkout(user_book)
        else:
            print('Your genre does not exist')


