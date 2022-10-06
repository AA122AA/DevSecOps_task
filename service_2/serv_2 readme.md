## ТЗ
Веб-сервер, который на гет реквест идет в БД, берет там документ и возвращает его содержимое (в бд лежит Hello World)

## Как запустить 
Поднимается общим docker-compose файлом

## Как проверить
В файле requests.http написан запрос для проверки. 

## Полезная информация 
Подключение к postgresql 
`psql -h 127.0.0.1 -p 5432 -U artem serv_2`
[psql cheatsheet](https://postgrescheatsheet.com/#/tables)

Как посмотереть коллекцию в mongo 
`use serv_2_db`
`db.text.find()`

