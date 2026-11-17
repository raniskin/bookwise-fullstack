# Bookwise — React + Django REST booking app

Полноценное демо онлайн-записи в барбершоп: интерфейс выбора услуги, даты и времени, REST API и база SQLite. Интерфейс React и сервер Django. **Демонстрация: настоящих оплат нет.**

## Функции
- Список услуг из backend
- Форма записи с валидацией имени, email, времени
- Проверка пересечения записей и запрет прошедших дат
- Подтверждение успешной записи
- Управление услугами и записями через Django Admin
- Адаптивный интерфейс

## Запуск backend (терминал №1)
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_services
python manage.py runserver
```
API: `http://127.0.0.1:8000/api/services/`, `POST /api/appointments/`.

Для доступа в админку: `python manage.py createsuperuser`, затем http://127.0.0.1:8000/admin/.

## Запуск frontend (терминал №2)
```bash
cd frontend
npm install
npm run dev
```
Страница: http://localhost:5173. При необходимости создайте `.env` с `VITE_API_BASE=http://127.0.0.1:8000/api`.

## Тесты
`cd backend && python manage.py test`.

## Важно перед реальным внедрением
- Проект — портфолио-демо, **не готовый продакшен**: API создания записей открыт, не реализованы аутентификация администратора в клиентском интерфейсе, rate limiting, email-уведомления, политика хранения персональных данных, ограничения запросов и согласия на обработку данных.
- Проверка конфликтов на SQLite не защищает от всех конкурентных запросов. Для продакшена нужны PostgreSQL, транзакционные блокировки или специализированное ограничение уникальности слотов.
- `DEBUG=1`, локальный `SECRET_KEY`, `ALLOWED_HOSTS` только для разработки. Перед развёртыванием настройте HTTPS, секреты из env, разрешённые CORS origins и резервные копии.
