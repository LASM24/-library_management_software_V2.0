from functs import (add_book, update_book, list_books,
                    delete_book, default, add_many_books,
                    engine, metadata)


if __name__ == '__main__':
    metadata.create_all(engine)

    options = {
        'a': add_book,
        'b': add_many_books,
        'c': list_books,
        'd': update_book,
        'e': delete_book
    }

    with engine.connect() as connection:
        while True:
            for function in options.values():
                print(function.__doc__)

            print('"quit" o "q" para salir')
            option = input('Seleccione una opcion valida: ').lower()
            if option == 'quit' or option == 'q':
                break

            function = options.get(option, default)
            function(connection)
