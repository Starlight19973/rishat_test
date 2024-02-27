# Stripe-Test

Тестовое задание по подключению Stripe.

## Начало работы

Эти инструкции помогут тебе получить копию проекта и запустить его на локальной машине для разработки и тестирования.

### Предварительные требования

Что нужно установить на ПК для использования:

- Python (версия 3.6 или выше)
- pip (менеджер пакетов Python)

### Установка

Пошаговый процесс установки и настройки окружения для разработки:

1. **Клонирование репозитория**

   ```bash
   git clone git@github.com:Starlight19973/rishat_test.git
   cd yourprojectname
Создание и активация виртуального окружения

Для пользователей Unix/Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
Для пользователей Windows:


python -m venv venv
.\venv\Scripts\activate
Установка зависимостей


pip install -r requirements.txt
Настройка базы данных

Выполни миграции:



python manage.py migrate
Запуск сервера разработки


python manage.py runserver
После этого ты сможешь открыть http://127.0.0.1:8000/ в браузере.
