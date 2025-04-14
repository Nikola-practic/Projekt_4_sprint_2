from main import BooksCollector


import pytest


class TestBooksCollector:

    # 1. Тестируем добавление новых книг.
    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_positiv(self, collector, name):
        collector.add_new_book(name)
        assert collector.books_genre[name] == 'Гордость и предубеждение и зомби' or 'Что делать, если ваш кот хочет вас убить'

    # 2. Тестируем, что книги без названия и с названием больше 40 символов не будут добавлены в словарь.
    @pytest.mark.parametrize('name', ['', 'В лесу родилась ёлочка, в лесу она росла, зимой и летом'])
    def test_add_new_book_more_negativ_sizes(self, collector, name):
        assert not collector.add_new_book(name)

    # 3. Тестируем добавление новых книг и задание книгам жанров.
    @pytest.mark.parametrize('name, genre', [['Последнее дело Холмса', 'Детективы'], ['Тринадцать этажей', 'Ужасы'],
                                             ['Цветик-семицветик', 'Мультфильмы'], ['Человек-невидимка', 'Фантастика'],
                                             ['Горе от ума', 'Комедии']])
    def test_set_book_genre_add_new_books_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    # 4. Тестируем получение жанра книги по её имени.
    def test_get_book_genre_return_genre(self, collector):
        collector.add_new_book('Последнее дело Холмса')
        collector.set_book_genre('Последнее дело Холмса', 'Детективы')
        assert collector.get_book_genre('Последнее дело Холмса') == 'Детективы'

    # 5. Тестируем  вывод списка книг по определённым жанрам.
    def test_get_books_with_specific_genre_when_genre(self, collector):
        collector.add_new_book('Человек-невидимка')
        collector.add_new_book('Пятый элемент')
        collector.set_book_genre('Человек-невидимка', 'Фантастика')
        collector.set_book_genre('Пятый элемент', 'Фантастика')
        fantastic = collector.get_books_with_specific_genre('Фантастика')
        assert 'Человек-невидимка' and 'Пятый элемент' in fantastic

    # 6. Тестируем, что нельзя вывести книгу по жанру, если у добавленной книги нет жанра.
    def test_get_books_with_specific_genre_not_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert not collector.get_books_with_specific_genre('Ужасы')

    # 7. Тестируем, что выводится словарь и наличие добавленных книг в словаре.
    def test_get_books_genre_add_dict(self, collector):
        books = ['Последнее дело Холмса', 'Тринадцать этажей', 'Цветик-семицветик', 'Человек-невидимка', 'Горе от ума']
        for name in books:
            collector.add_new_book(name)
        new_dict = collector.get_books_genre()
        assert type(collector.get_books_genre()) == dict
        assert 'Последнее дело Холмса' and 'Тринадцать этажей' and 'Цветик-семицветик' and 'Человек-невидимка' and 'Горе от ума' in new_dict

    # 8. Тестируем, что в списке с книгами есть только книги с рейтингом для детей.
    def test_get_books_for_children_genre_children(self, collector):
        books = ['Последнее дело Холмса', 'Тринадцать этажей', 'Человек-невидимка', 'Гордость и предубеждение и зомби']
        x = 0
        for name in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, collector.genre[x])
            x += 1
        for rating in collector.genre_age_rating:
            assert rating == 'Ужасы' or 'Детективы' not in collector.get_books_for_children()
            assert rating == 'Фантастика' or 'Мультфильмы' or 'Комедии' in collector.get_books_for_children()

    # 9. Тестируем, что книга добавленная в Избранное, есть в Избранном.
    def test_add_book_in_favorites_when_books_in_list(self, collector):
        books = ['Тринадцать этажей', 'Цветик-семицветик', 'Человек-невидимка']
        for name in books:
            collector.add_new_book(name)
        collector.add_book_in_favorites('Тринадцать этажей')
        assert 'Тринадцать этажей' in collector.favorites

    # 10. Тестируем, что нельзя добавить книгу в Избранное, если её нет в словаре.
    def test_add_book_in_favorites_when_books_not_in_list(self, collector):
        books = ['Человек-невидимка', 'Горе от ума', 'Гордость и предубеждение и зомби']
        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
        assert not collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

    # 11. Тестируем удаление книги из Избранного.
    def test_delete_book_from_favorites_list(self, collector):
        books = ['Последнее дело Холмса', 'Цветик-семицветик', 'Гордость и предубеждение и зомби']
        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites('Последнее дело Холмса')
        assert 'Последнее дело Холмса' not in collector.favorites

    # 12. Тестируем наличие списка книг, добавленных в Избранное.
    def test_get_list_of_favorites_books_list(self, collector):
        books = ['Тринадцать этажей', 'Человек-невидимка', 'Гордость и предубеждение и зомби']
        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
            favorites = collector.get_list_of_favorites_books()
        assert 'Тринадцать этажей' and 'Человек-невидимка' and  'Гордость и предубеждение и зомби' in favorites
