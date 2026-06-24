# Каталог телефонов — Домашнее задание Netology (2.1)

Django-приложение для отображения каталога телефонов из CSV-файла.

## Возможности

- Список телефонов на странице `/catalog`
- Страница телефона по slug: `/catalog/iphone-x`
- Сортировка по названию, цене (по убыванию и возрастанию)
- Импорт данных из `phones.csv` в SQLite

## Структура проекта

```
phoneshop/
├── catalog/
│   ├── management/
│   │   └── commands/
│   │       └── import_phones.py   # команда импорта
│   ├── templates/
│   │   └── catalog/
│   │       ├── catalog.html       # список телефонов
│   │       └── phone.html         # карточка телефона
│   ├── models.py                  # модель Phone
│   ├── views.py                   # catalog, phone_detail
│   └── urls.py
├── phoneshop/
│   ├── settings.py
│   └── urls.py
├── phones.csv                     # данные для импорта
├── manage.py
└── requirements.txt
```

## Запуск

### 1. Клонировать репозиторий и перейти в папку проекта

```bash
git clone https://github.com/<ваш-логин>/<репозиторий>.git
cd <репозиторий>/phoneshop
```

### 2. Создать и активировать виртуальное окружение

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Применить миграции

```bash
python manage.py migrate
```

### 5. Импортировать данные из CSV

```bash
python manage.py import_phones
```

### 6. Запустить сервер

```bash
python manage.py runserver
```

Откройте браузер: [http://127.0.0.1:8000/catalog](http://127.0.0.1:8000/catalog)

## URL-адреса

| URL | Описание |
|-----|----------|
| `/catalog` | Каталог всех телефонов |
| `/catalog?sort=name` | Сортировка по названию |
| `/catalog?sort=min_price` | Сначала дешёвые |
| `/catalog?sort=max_price` | Сначала дорогие |
| `/catalog/<slug>` | Страница телефона |
