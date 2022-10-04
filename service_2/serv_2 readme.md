## ТЗ
Веб-сервер, который на гет реквест идет в БД, берет там документ и возвращает его содержимое (в бд лежит Hello World)

## Как запустить 
`python hello.py`

## Как проверить

## Полезная информация 
Подключение к postgresql 
`psql -h 127.0.0.1 -p 5432 -U artem serv_2`
[psql cheatsheet](https://postgrescheatsheet.com/#/tables)

создание пользователя mongo
 `db.command("createUser", "artem", pwd="0000", roles=["readWrite"])`
