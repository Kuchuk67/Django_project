# Django_project
проект  интернет-магазина на фрейморке Django 
#### Django + PostgreSQL + bootstrap-5 + XML + Redis 

## Установка Интернет-магазина
Проект работает с зависимостями под управлением poetry 
### Установка виртуального окружения
```
poetry shell
poetry install
```
### Файл .env
Создание файла .env на основе примера: файл example_env

### БД и Миграции
Создание БД в PostgreSQL 
```
CREATE database catalog_shop;
CREATE USER user_catalog WITH PASSWORD '**********';
```
Подключится к данной БД и выполнить
```
ALTER DATABASE catalog_shop OWNER TO user_catalog;
```
Выполнить миграции 
```
 python manage.py migrate
```
### Создание пользователя для админпанели
для создания и редактированиязаписей необходима автоизация
```
 python manage.py createsuperuser
```

### Загрузка демоданных
Загрузка данных происходит из фида для Яндекс-Маркета feed-yml.xml
```
/catalog/management/commands/feed-yml.xml
```
Обновление данных (старые данные удаляются) выполняется командой
```
python manage.py add_products
python manage.py add_articles

```


# приложение Catalog

Созданы страницы:
* /home/
* /contacts/
* /category/
* /product/...


## templates
### head.html
Шапка \<head>...\</head> сайта с методанными
### menu.html
меню сайта
### home.html
Главаная страница
### contacts.html
Страница контактов 
Форма отправки POST-запроса, вывод сообщения об успешной отправке 
### category.html
Страница вывода категорий 
### product_one_category.html
Страница вывода продуктов одной категории
### page_links.html
Блок вывода пагонации страниц
### product_single.html
Страница вывода карточки продукта

# приложение Blog

Созданы страницы:
* /blog/
* blog/article/...
* blog/creat
* blog/article/.../update/
* blog/article/.../delete/

## templates
### article_confirm_delete.html
Подтверждение удаления статьи
### article_detail.html
Страница статьи
### article_form.html
Редактирование статьи
### article_list.html
Выводит список статей
### articles.html
Отображение одной статьи в списке


# приложение Users

Созданы страницы:
* user/signup/  
* user/login/
* user/logout/
* user/profile/

## templates
### login.html
Страница логина
### profile.html
Страница профайла пользователя (отключена)
### profile_edite.html
Страница Редактирования профайла
### register.html
Страница регистрации


