# Task Management System

![Task Management](https://img.shields.io/badge/Task-Management-blue.svg) ![Microservices](https://img.shields.io/badge/Microservices-Architecture-green.svg) ![Docker](https://img.shields.io/badge/Docker-Compose-orange.svg)

Task Management System - это проект, разработанный для обеспечения эффективного управления задачами в различных контекстах.

## 📌 Модули

### 🚀 api_gateway
Модуль **api_gateway** отвечает за маршрутизацию API-запросов к другим микросервисам.

### ✅ task_service
Модуль **task_service** определяет маршруты для создания, чтения, обновления и удаления задач.

### 👤 user_service
Модуль **user_service** отвечает за создание и управление пользователями, а также за аутентификацию и выдачу токенов доступа.

### 🔔 notification_service
Модуль **notification_service** предоставляет функции для отправки уведомлений пользователям.

### 📂 file_attachment_service
Модуль **file_attachment_service** реализует загрузку и управление файлами.

### 🏷 tag_service
Модуль **tag_service** управляет добавлением и получением тегов для задач.

## 📁 Дополнительные файлы

- **📜 docker-compose.yml** - Конфигурация для запуска всех микросервисов с помощью Docker Compose.
- **🗄 init_db.sql** - Скрипт для инициализации базы данных.

## 🧪 Тестирование

В папке **tests/** находятся unit-тесты, предназначенные для проверки работоспособности API и его компонентов.

## ⚠️ Важно
Этот проект является примером и требует доработок для полноценного использования в продакшене. 🚀

