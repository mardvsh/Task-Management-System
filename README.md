# Task Management System

Task Management System — это backend-система для управления задачами, реализованная в виде набора сервисов с разделением ответственности и возможностью масштабирования.

Проект фокусируется на архитектуре backend-сервисов, обработке запросов и расширяемости системы.

---

## Архитектура (кратко)

Система построена по принципу разделения на сервисы:

api_gateway → маршрутизация запросов  
↓  
task_service → бизнес-логика задач  
user_service → пользователи и аутентификация  
notification_service → уведомления  
file_attachment_service → работа с файлами  
tag_service → теги  

Каждый сервис отвечает за свою зону ответственности и может масштабироваться независимо.

---

## Основные возможности

- CRUD-операции для задач
- управление пользователями и аутентификация
- система тегов
- загрузка и хранение файлов
- отправка уведомлений
- централизованная маршрутизация через API Gateway

---

## Технологии

- Backend: Python (REST API)
- Архитектура: service-based / microservices-ready
- База данных: PostgreSQL
- Контейнеризация: Docker, Docker Compose

---

## Как запустить

git clone https://github.com/mardvsh/Task-Management-System.git  
cd Task-Management-System  

docker compose up --build -d  

Проверить статус:  
docker compose ps  

---

## Остановка

docker compose stop  

docker compose down  

docker compose down -v  

---

## Полезные команды

docker compose logs -f  

docker compose logs -f task_service  

---

## Тестирование

pytest  

---

## Архитектурные решения

- Разделение на слои (handlers / services / storage)
- Изоляция бизнес-логики внутри сервисов
- Возможность горизонтального масштабирования
- Подготовка к внедрению:
  - кеширования (Redis)
  - асинхронной обработки (Kafka / очереди)
  - rate limiting

---

## Возможные улучшения

- Добавление Redis для кеширования
- Внедрение Kafka для событийной модели
- Расширение системы аутентификации (JWT refresh, RBAC)
- Мониторинг (Prometheus + Grafana)
- Логирование (ELK stack)

---

## English Quick Overview

Task Management System is a backend service-oriented application designed for managing tasks, users, and related entities.

It demonstrates:
- service decomposition
- REST API design
- scalable backend architecture

---

## Key Takeaway

This project focuses not only on functionality but on backend architecture, scalability, and system design, making it a foundation for production-grade services.
