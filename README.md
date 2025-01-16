# Django_project
проект  интернет-магазина на фрейморке Django 
#### Django + PostgreSQL + bootstrap-5 + XML

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
ALTER DATABASE catalog_shop OWNER TO user_catalog;
```
Выполнить миграции 
```
 python manage.py migrate
```
### Создание пользователя для админпанели
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

```


# приложение Catalog

Созданы страницы:
* /home/
* /contacts/

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



