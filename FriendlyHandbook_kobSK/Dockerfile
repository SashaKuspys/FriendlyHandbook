# Використовуйте офіційний образ Python
FROM python:3.11-rc-slim

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME

# Встановіть залежності
RUN pip install prompt_toolkit

# Скопіюйте файли у контейнер
COPY main.py /app/main.py
COPY adbook.py /app/adbook.py
COPY note_book.py /app/note_book.py
COPY sort_folder.py /app/sort_folder.py
COPY calculator.py /app/calculator.py
COPY prompt_tool.py /app/prompt_tool

# Запустіть ваш додаток
CMD ["python", "main.py"]
