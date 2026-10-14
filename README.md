# BookHub

BookHub — веб-приложение для управления каталогом книг, разработанное с использованием Django и Django REST Framework.

## Возможности

- Просмотр списка книг и подробной информации о каждой книге.
- Создание, редактирование и удаление книг.
- Поиск по названию книги, автору и описанию.
- Фильтрация книг по рейтингу.
- Пагинация списка книг.
- Управление книгами, авторами и тегами через Django Admin.
- REST API для книг, авторов и тегов.
- Проверка прав доступа к API.
- Оптимизация запросов к базе данных с помощью `select_related()` и `prefetch_related()`.
- Автоматические тесты.

## Технологии

- Python
- Django
- Django REST Framework
- SQLite
- HTML и CSS

## Установка

1. Создайте и активируйте виртуальное окружение.
2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` в корневой папке проекта и укажите настройки:

   ```env
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
   ```

4. Выполните миграции:

   ```bash
   python manage.py migrate
   ```

5. Запустите сервер:

   ```bash
   python manage.py runserver
   ```

## Основные адреса

- Веб-каталог: http://127.0.0.1:8000/
- Панель администратора: http://127.0.0.1:8000/admin/
- API книг: http://127.0.0.1:8000/api/books/
- API авторов: http://127.0.0.1:8000/api/authors/
- API тегов: http://127.0.0.1:8000/api/tags/

## Запуск тестов

```bash
python manage.py test core
```