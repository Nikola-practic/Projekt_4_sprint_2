В проекте Projekt_4_sprint_21 я удалил виртуальное окружение и не смог его настроить заново. Создал новый проект Projekt_4_sprint_2, который направляю на проверку.

Копия замечаний по прошлому проекту:
tests.py
    # 1. Тестируем добавление новых книг.
    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_positiv(self, name):
        collector = BooksCollector()
@Ayantea1 Ayantea1 5 days ago
Можно улучшить: общее для всех тестов предусловие можно вынести в фикстуру


tests.py
        collector.add_new_book('Пятый элемент')
        collector.set_book_genre('Человек-невидимка', 'Фантастика')
        collector.set_book_genre('Пятый элемент', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика')
@Ayantea1 Ayantea1 5 days ago
Нужно исправить: с чем сравниваешь результат?
У тебя буду выведены все книги, лучше проверить, что выбираются только нужные


tests.py
    def test_add_new_book_positiv(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre[name] == ''
@Ayantea1 Ayantea1 5 days ago • 
Можно лучше: ты проверяешь не то, что книга добавлена, а то, что у нее нет жанра


tests.py
        for name in books:
            collector.add_new_book(name)
        random_books = random.choice(books)
        assert random_books in collector.get_books_genre()
@Ayantea1 Ayantea1 5 days ago
Можно лучше: эта проверка скорее подойдет для метода добавления книг. .get_books_genre() должен выводить словарь с добавленными книгами, проверь основную функцию


tests.py
            collector.set_book_genre(name, collector.genre[x])
            x += 1
        for rating in collector.genre_age_rating:
            assert rating not in collector.get_books_for_children()
@Ayantea1 Ayantea1 5 days ago
Нужно исправить: ты убедился, что рейтинговых жанров нет в названиях возвращенного списка книг. Метод не проверен


tests.py
        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books()
@Ayantea1 Ayantea1 5 days ago
Нужно исправить: с чем сравниваешь полученный результат?


