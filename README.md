Тестовое задание для стажёра QA в Авито
Описание
Автоматизированные тесты для API микросервиса объявлений Авито.

Структура проекта
avito-internship-task/
README.md                 
TESTCASES.md              
bug_report.md             
requirements.txt          
tests/
    test_api.py           

Предварительные требования
- Python 3.7 или выше
- pip (пакетный менеджер Python)

Установка и запуск
1. Клонирование репозитория
git clone https://github.com/alinairmukhametova/avito-internship-task.git
cd avito-internship-task

2. Установка зависимостей
pip install -r requirements.txt

3. Запуск тестов
Запуск всех тестов
pytest tests/test_api.py -v
Запуск с подробным выводом
pytest tests/test_api.py -v -s
Запуск конкретного теста
pytest tests/test_api.py::TestAvitoAPI::test_create_item_success -v

4. Альтернативный способ запуска
python tests/test_api.py

Что тестируется
- Создание объявлений
- Получение объявлений по ID
- Получение всех объявлений продавца
- Обработка ошибок (невалидные данные)
- Доступность сервера

5. Результаты тестирования
Все тесты должны завершиться успешно. В случае обнаружения багов, они будут записаны в файл BUGS.md.
