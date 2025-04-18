
import pytest



class TestBooksCollector:

    # 1. Тестируем добавление новых книг.
    @pytest.mark.parametrize('name',
        ['Гордость и предубеждение и зомби',
        'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_add_too_book(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.books_genre

    # 2. Тестируем, что книги без названия и с названием больше 40 символов не будут добавлены в словарь.
    @pytest.mark.parametrize('name', ['', 'В лесу родилась ёлочка, в лесу она росла, зимой и летом'])
    def test_add_new_book_more_not_name_and_more_forty_characters(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    # 3. Тестируем добавление новых книг и задание книгам жанров.
    @pytest.mark.parametrize('name, genre', [
        ['Последнее дело Холмса', 'Детективы'], 
        ['Тринадцать этажей', 'Ужасы'],
        ['Красная шапочка', 'Мультфильмы'], 
        ['Человек-невидимка', 'Фантастика'],
        ['Горе от ума', 'Комедии'],
        ])
    def test_set_book_genre_adding_new_books_and_setting_genres(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    # 4. Тестируем получение жанра книги по её имени.
    def test_get_book_genre_return_genre_for_name(self, collector):
        collector.add_new_book('Последнее дело Холмса')
        collector.set_book_genre('Последнее дело Холмса', 'Детективы')
        assert collector.get_book_genre('Последнее дело Холмса') == 'Детективы'

    # 5. Тестируем вывод списка книг по определённым жанрам.
    def test_get_books_with_specific_genre_output_of_books_by_genre(self, collector):
        collector.add_new_book('Человек-невидимка')
        collector.set_book_genre('Человек-невидимка', 'Фантастика')
        assert 'Человек-невидимка' in collector.get_books_with_specific_genre('Фантастика') 

    # 6. Тестируем, что нельзя вывести книгу по жанру, если у добавленной книги нет жанра.
    def test_get_books_with_specific_genre_book_cannot_displayed_if_not_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert not collector.get_books_with_specific_genre('Ужасы')

    # 7. Тестируем, что выводится словарь и наличие добавленных книг в словаре.
    def test_get_books_genre_dict_and_add_books_displayed(self, collector):
        books = ['Последнее дело Холмса',
                 'Тринадцать этажей',
                 'Красная шапочка',
                 'Человек-невидимка',
                 'Горе от ума']
        for name in books:
            collector.add_new_book(name)
        assert type(collector.get_books_genre()) == dict
        for book in books:
            assert book in collector.get_books_genre()

    # 8. Тестируем, что в списке с книгами есть только книги с рейтингом для детей.
    def test_get_books_for_children_only_books_for_children(self, collector):
        books = {'Человек-невидимка': 'Фантастика',
                 'Гордость и предубеждение и зомби': 'Ужасы', 
                 'Последнее дело Холмса': 'Детективы', 
                 'Красная шапочка': 'Мультфильмы', 
                 'Горе от ума': 'Комедии'}
        for book, genre in books.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        for book_for_children in collector.get_books_for_children():
            assert collector.books_genre.get(book_for_children) not in collector.genre_age_rating

    # 9. Тестируем, что книга добавленная в Избранное, есть в Избранном.
    def test_add_book_in_favorites_the_book_in_favorites(self, collector):
        collector.add_new_book('Тринадцать этажей')'Что делать, если ваш кот хочет вас убить'
        collector.add_book_in_favorites('Тринадцать этажей')
        assert 'Тринадцать этажей' in collector.favorites

    # 10. Тестируем, что нельзя добавить книгу в Избранное, если её нет в словаре.
    def test_add_book_in_favorites_the_book_not_in_favorites(self, collector):
        collector.add_book_in_favorites()
        assert 'Что делать, если ваш кот хочет вас убить' not in collector.favorites

    # 11. Тестируем удаление книги из Избранного.
    def test_delete_book_from_favorites_deleting_book_from_favorites(self, collector):
        collector.add_new_book('Последнее дело Холмса')
        collector.add_book_in_favorites('Последнее дело Холмса')
        collector.delete_book_from_favorites('Последнее дело Холмса')
        assert 'Последнее дело Холмса' not in collector.favorites

    # 12. Тестируем наличие списка книг, добавленных в Избранное.
    def test_get_list_of_favorites_books_list_books_add_favorites(self, collector):
        books = ['Тринадцать этажей',
                 'Человек-невидимка',
                 'Гордость и предубеждение и зомби']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        for book in books:
            assert book in collector.favorites
