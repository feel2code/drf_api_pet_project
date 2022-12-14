# Проект YaMDb
![example workflow](https://github.com/feel2code/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
## Описание

Проект YaMDb собирает отзывы пользователей на различные произведения.

### Регистрация пользователей

1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на ```/api/v1/auth/signup/```.
2. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
3. Пользователь отправляет POST-запрос с параметрами username и confirmation_code на ```/api/v1/auth/token/```, в ответе на запрос ему приходит token (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на ```/api/v1/users/me/``` и заполняет поля в своём профайле (описание полей — в документации).

### Пользовательские роли

+ **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
+ **Аутентифицированный пользователь (user)** — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
+ **Модератор (moderator)** — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
+ **Администратор (admin)** — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
+ **Суперпользователь Django** — обладает правами администратора (admin)

## Основные технологии

+ Django
+ djangorestframework
+ djangorestframework-simplejwt
+ PyJWT

## Запуск проекта
- Клонируйте репозиторий
- Создайте `.env` файл в директории `infra/`, на основе `.env.example`
  >DB_ENGINE= # тип БД\
  >DB_NAME= # название БД\
  >POSTGRES_USER= # имя пользователя\
  >POSTGRES_PASSWORD= # пароль\
  >DB_HOST= # хост БД\
  >DB_PORT= # порт (по умолчанию 5432)
- Соберите образ
  `$ cd infra && docker-compose up -d --build`
- Примените миграции
  `$ docker-compose exec web python manage.py migrate`
- Создайте админа
  `$ docker-compose exec web python manage.py createsuperuser`
- Соберите статику
  `$ docker-compose exec web python manage.py collectstatic --no-input`

### Остановка проекта
- В терминале выполните команду:
  `$ docker-compose down -v`

### Наполнение и резервное копирование базы данных
- Создать резервную копию базы данных:
  `$ docker-compose exec web python manage.py dumpdata > fixtures.json`

- Наполнить базу данных из резервной копии:
  `$ docker-compose exec web python manage.py loaddata fixtures.json`

### Основной функционал API
[Документация проекта http://localhost:8000/redoc/](http://localhost:8000/redoc/)

Примеры запросов:

- Регистрация 
`POST`
> /auth/signup/

`Content type: application/json`
> {\
> "email": "string",\
> "username": "string"\
> }

- Получение JWT-токена
`POST`
> /auth/token/

`Content type: application/json`
> { \
> "username": "string",\
> "confirmation_code": "string"\
> }

- Получение списка всех категорий произведений
`GET`
> /categories/

Пример ответа: \
`Content type: application/json`
> { \
> "count": 0,\
> "next": "string",\
> "previous": "string",\
> "results": [{\
> "name": "string",\
> "slug": "string"\
> }]\
> }

Полные примеры запросов и ответов содержатся в [документации проекта](http://localhost:8000/redoc/).