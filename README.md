# Коннектор spbu.timetable.ru и Google Calendar
Выгружает расписание с официального сайта расписания СПбГУ и воссоздает его в Google Calendar

## Настройка окружения:
1. Скачать зависимости `pip install -r requirements.txt`
2. Получить `credentials.json` в Google API (https://developers.google.com/calendar/api/quickstart/python)
3. Установите переменные окружения в `.env` в соответствии с `.example.env`
4. Запустите `scrap_schedule.py`, чтобы выгрузить расписание
5. Запустите `__csv.py`, чтобы выделить из него предметы в `subjects.csv`
6. Запустите `index.py`

## Структура:
* `index.py` - Основная точка входа. При исполнении выгружает расписание из timetable, начиная с понедельника, который указан в окружении как `START_DATE`, нужной группы (`GROUP_ID`) и в нужный календарь `CALENDAR_ID`. Цвета событий расставляются в соответствии с `subjects.csv`

* `scrap_schedule.py` - здесь хранится вся логика по выгрузке расписания из timetable.spbu.ru в формате excel, и парсинг этого расписания

* `_google.py` - Взаимодействие с API Google Календаря

* `__csv.py` - В ходе работы образуются бэкапы в виде csv файлов расписания. Здесь хранятся все функции для этого

* `_http.py` - Вспомогательные функции для работы с сетью

* `structures.py` - Типы и структуры данных, используемые в проекте

* `dateformat_utils.py` - Утилиты для работы с датой и временем

* `timtable_spbu.py` - Утилиты для timetable.spbu.ru

* `utils.py` - Общие утилиты
