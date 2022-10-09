# Разработка системы проверки здоровья контейнеров
## Техническое задание 
Необходимо поднять несколько тестовых микросервисов в docker контейнерах: 
- [x] веб-сервер, который на гет реквест возвращает Hello World 
- [x] веб-сервер, который на гет реквест идет в БД, берет там документ и возвращает его содержимое (в бд лежит Hello World)
- [x] веб-сервер, который на гет реквест создает задачу (Hello World) и публикует ее в брокер сообщений (RabbitMQ, Kafka, etc.); клиент получает из брокера сообщений задачу и кладет ее в бд

Затем разработать систему проверки здоровья контейнеров, которая позволяет узнать не только системные характеристики контейнера (память, загрузка процессора и т.д.), но и работоспособность сервисов, запущенных внутри контейнера (например, веб-сервер все еще живой и слушает такой-то порт).

Система проверки здоровья контейнеров:
- [x] Узнавать системные характеристики
  - [x] Память
  - [x] Загрузка процессора
  - [ ] Занятое дисковое пространство
  - [ ] Net I/O
- [x] Работоспособность сервисов

Требования к системе Система проверки здоровья:
- [x] Проверка должна запускаться периодически
- [x] Результат проверки должен сохраняться в Кибану.
- [x] Можно настроить фильтры на кибане для лучшей визуализации результатов.
