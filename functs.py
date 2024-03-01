from sqlalchemy import (create_engine, select, and_, Table,
                        Column, Integer, String, MetaData)

from decorators import system_console
import config.config as cg
import re


engine = create_engine(cg.url)
metadata = MetaData()


BOOKS = Table(
    'books',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('title', String()),
    Column('author', String()),
    Column('year', Integer()),
    Column('amount', Integer()),
)


# --------- FUNCIONES COMPLEMENTARIAS --------- #


# usado en: update_book
def update_inf_bk(title, author, year, response, connection):
    row = response.fetchone()
    if row:
        old_tt, old_at, old_yr, old_am = row[0], row[1], row[2], row[3]

        query_update = BOOKS.update().values(
            title=title, author=author,
            year=year, amount=old_am) \
            .where(
                and_(BOOKS.c.title == old_tt,
                     BOOKS.c.author == old_at,
                     BOOKS.c.year == old_yr,
                     BOOKS.c.amount == old_am))

        connection.execute(query_update)
        connection.commit()
        return True


# usado en: update_book
def new_info():
    title = str(input('Inserte nuevo título del libro: ')).lower()
    author = str(input('Inserte nuevo autor del libro: ')).lower()
    year = int(input('Inserte nuevo año de publicación del libro: '))
    return title, author, year


# usado en: add_book
def validation_book(title, author, year, connection, amountDefault=1):
    query = BOOKS.insert().values(title=title, author=author,
                                  year=year, amount=amountDefault)
    connection.execute(query)
    connection.commit()
    return '>>> libro añadido exitosamente'


# usado en: add_book & add_many_books
def info_book():
    title = str(input('Inserte título del libro: ')).lower()
    author = str(input('Inserte autor del libro: ')).lower()
    year = int(input('Inserte año de publicación del libro: '))
    return title, author, year


# usado en: add_book & add_many_books
def str_values(value):
    patron = r'^[a-zA-Z\s]+$'

    if re.match(patron, value) and 2 <= len(value) <= 100:
        return True
    else:
        return False


# usado en: add_book & add_many_books
def val_yr(year):
    return year >= 1800 and year <= 2024


# --------- METODOS DEL "CRUD" --------- #
with engine.connect() as connection:
    @system_console
    def add_book(connection):
        """A)Registrar un libro"""
        title, author, year = info_book()
        tt, auth, yr = str_values(title), str_values(author), val_yr(year)

        if tt and auth and yr:
            validation_book(title, author, year, connection)
            print('>>> libro creado exitosamente')
        else:
            print('Ingresó valores incorrectos. Intente de nuevo')

    @system_console
    def add_many_books(connection):
        """B)Registrar multiples unidades de un libro"""
        try:
            title, author, year = info_book()
            tt, auth, yr = str_values(title), str_values(author), val_yr(year)

            if tt and auth and yr:
                n_bk = int(input('Inserte la cantidad de unidades: '))

                query = select().with_only_columns(BOOKS.c.title).where(
                    BOOKS.columns.title == title,
                    BOOKS.c.author == author,
                    BOOKS.c.year == year)
                response = connection.execute(query)

                if response.fetchone() is not None:
                    current_quantity = BOOKS.c.amount
                    new_quantity = current_quantity + n_bk
                    connection.execute(BOOKS.update().where(
                        BOOKS.c.title == title).values(amount=new_quantity))
                    connection.commit()
                    print(f"Se han agregado {n_bk} unidades del libro {title}")
                else:
                    connection.execute(BOOKS.insert(), [{'title': title,
                                                         'author': author,
                                                         'year': year,
                                                         'amount': n_bk}])
                    connection.commit()
                    print(f"Se agrego el libro '{title}' con {n_bk} unidades.")
            else:
                print('Ingresó valores incorrectos. Intente de nuevo')
        except ValueError:
            print('Ingresó valores incorrectos. Intente de nuevo')

    @system_console
    def list_books(connection):
        """C)Listar libros existentes"""
        try:
            selec_query = BOOKS.select()
            result = connection.execute(selec_query)
            for bk in result.fetchall():
                inf = f'{bk.title} - {bk.author} - {bk.year} - {bk.amount}'
                print(inf)
        except Exception as err:
            print('Ocurrió un error')
            print(err)

    @system_console
    def update_book(connection):
        """D)Actualizar libro"""
        titl_bk = input('Inserte nombre del libro a actializar: ').lower()
        query = select().with_only_columns(
            BOOKS.c.title, BOOKS.c.author, BOOKS.c.year, BOOKS.c.amount) \
            .where(BOOKS.c.title == titl_bk)
        response = connection.execute(query)

        if response.rowcount > 0:
            title, author, year = new_info()
            update_inf_bk(title, author, year, response, connection)
            print('>>> libro actualizado exitosamente')
        else:
            print('libro no encontrado')

    @system_console
    def delete_book(connection):
        """E)Eliminar libro"""
        title = input('Inserte el nombre del libro a eliminar:  ')
        query = select().with_only_columns(BOOKS.c.title).where(
            BOOKS.columns.title == title)
        response = connection.execute(query)

        if response.rowcount > 0:
            query_delete = BOOKS.delete().where(BOOKS.c.title == title)
            connection.execute(query_delete)
            connection.commit()
            print('>>> Libro eliminado exitosamente')
        else:
            print('libro no encontrado')

    def default(*args):
        print('Opcion no valida')
